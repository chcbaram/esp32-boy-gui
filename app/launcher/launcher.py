import sys
import serial
import serial.tools.list_ports as sp
import os
import subprocess
import time
import csv
from os import path
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog
from PySide6.QtCore import QFile, QProcess
from PySide6.QtGui import *
from app.launcher.lib.log import LogWidget


try:
    import esptool
    import espefuse
except ImportError:
    need_to_install_package_err()


if __package__ is None:
    sys.path.append(path.dirname( path.dirname( path.abspath(__file__) ) ))
    from ui.ui_launcher import *
else:
    from .ui.ui_launcher import *

sys.path.append(path.dirname( path.dirname( path.abspath(__file__) ) ))
app_path = path.dirname( path.abspath(__file__)).split('launcher')[0]




class MainWindow(QMainWindow):
  def __init__(self):
    super(MainWindow, self).__init__()
    self.ui = Ui_Launcher()
    self.ui.setupUi(self)

    self.is_force_quit = False
    self.run_count = 0    
    self.baud_list = [460800]
    self.is_thread = False

    self.log = LogWidget(self.ui.log)

    self.setClickedEvent(self.ui.btn_scan, self.btnScan)    
    self.setClickedEvent(self.ui.btn_flash, self.btnFlash)    
    self.setClickedEvent(self.ui.btn_browse, self.btnBrowse)   
    
    self.path_cwd  = os.getcwd() + '/init/'
    self.path_part = app_path + "data/init/partition-table.bin"
    self.path_boot = app_path + "data/init/bootloader.bin"
    self.path_ota  = app_path + "data/init/ota_data_initial.bin"
    self.path_firm = os.getcwd() + '/'


    if os.path.exists(self.path_cwd + 'partitions.csv'):
      self.path_csv = self.path_cwd + 'partitions.csv'
    else:
      self.path_csv = app_path + 'data/init/partitions.csv'
    
    if os.path.exists(self.path_cwd + 'partition-table.bin'):
      self.path_part = self.path_cwd + 'partition-table.bin'
    
    if os.path.exists(self.path_cwd + 'bootloader.bin'):
      self.path_boot = self.path_cwd + 'bootloader.bin'
    
    if os.path.exists(self.path_cwd + 'ota_data_initial.bin'):
      self.path_ota = self.path_cwd + 'ota_data_initial.bin'

    self.log.println(self.path_csv)
    self.log.println(self.path_part)
    self.log.println(self.path_boot)
    self.log.println(self.path_ota)

    self.part_list = []
    self.file_list = []

    # Partition List 
    if os.path.exists(self.path_csv) == True:
      f = open(self.path_csv,'r')
      rdr = csv.reader(f)
      
      for line in rdr:
        if len(line) > 3:
          if 'app' in line[1]:
            self.part_list.append(line)
      f.close()
    else:
      self.log.println("No partitions.csv")

    for part in self.part_list:
      self.ui.combo_part.addItem('%-10s' % part[0].strip() + "a : " + '%-5s' % part[3].strip() + "  s : " + '%-5s' % part[4].strip())

    # Firmware List
    self.updateFileList()

    self.btnScan()
    
  def handle_stderr(self, process_obj):
    data = process_obj.readAllStandardError()
    stderr = bytes(data).decode("utf8")
    self.log.print(stderr)

  def handle_stdout(self, process_obj):
    data = process_obj.readAllStandardOutput()
    stdout = bytes(data).decode("utf8")
    self.log.print(stdout)

  def updateFileList(self):
    files = os.listdir(self.path_firm)
    for file in files:
      if file.endswith(".bin"):
        f = open(self.path_firm + file,'rb')
        bin_header = int.from_bytes(f.read(1), byteorder='little')
        if bin_header == 0xE9:
          print(file)      
          self.file_list.append(self.path_firm + file)
          self.ui.combo_file.addItem(file)  
        f.close()

  def processFinished(self, button, process_obj):
    print('Finished : ' + button.text())
    process_obj = None      
    button.setEnabled(True)
    if self.run_count > 0:
      self.run_count -= 1  

  def setClickedEvent(self, event_dst, event_func):
    event_dst.clicked.connect(lambda: self.btnClicked(event_dst, event_func))    

  def btnClicked(self, button, event_func):
    print(button.text())
    event_func()
    # self.btnUpdate()

  def btnScan(self):
    ports = sorted(sp.comports())

    self.ui.combo_port.clear()
    self.ui.combo_baud.clear()

    for i in ports :
      print(str(i) + " \t" + str(i.usb_info()))
      if i.vid == 0x303A:
        self.ui.combo_port.addItem(i.device)      
        item_tip_str = i.manufacturer
        if i.description is None:
          item_tip_str = item_tip_str + ' ' +  i.description
        self.ui.combo_port.setItemData(self.ui.combo_port.count()-1, item_tip_str, Qt.ToolTipRole)

    for baud in self.baud_list:
      self.ui.combo_baud.addItem(str(baud))
        
  def btnBrowse(self):
    path = QFileDialog.getExistingDirectory()
    if len(path) > 0:
      self.path_firm = path + '/'
      self.updateFileList()

  def btnFlash(self):
    if self.ui.combo_file.count() == 0:
      self.log.println("No File")
      return
    if self.ui.combo_port.count() == 0:
      self.log.println("No Port")
      return

    print('btnFlash()')
    if self.run_count == 0:
      self.log.clear()
      self.ui.btn_flash.setEnabled(False)
      process_obj = QProcess()  
      process_obj.finished.connect(lambda: self.processFinished(self.ui.btn_flash, process_obj))
      process_obj.setProcessChannelMode(QProcess.MergedChannels)
      process_obj.readyReadStandardOutput.connect(lambda: self.handle_stdout(process_obj))
      process_obj.readyReadStandardError.connect(lambda: self.handle_stderr(process_obj))


      cmd_args = ""

      cmd_addr = self.part_list[self.ui.combo_part.currentIndex()][3].strip()
      self.log.print(cmd_addr)
      cmd_file = self.file_list[self.ui.combo_file.currentIndex()].strip()
      self.log.print(cmd_file)

      cmd_args += "--chip esp32s3" 
      cmd_args += " -p" + self.ui.combo_port.currentText()
      cmd_args += " -b" + self.ui.combo_baud.currentText()
      cmd_args += " --before=default_reset"
      cmd_args += " --after=hard_reset write_flash"
      cmd_args += " --flash_mode dio"
      cmd_args += " --flash_freq 80m"
      cmd_args += " --flash_size detect 0x0 " + self.path_boot
      cmd_args += " 0x8000 " + self.path_part
      cmd_args += " 0xd000 " + self.path_ota  
      cmd_args += " " + cmd_addr + " " + cmd_file

      process_obj.start("esptool.py", cmd_args.split(' '))      
      self.run_count += 1   

  def closeEvent(self, QCloseEvent):

    if self.run_count > 0 and self.is_force_quit == False:
      self.msg = QMessageBox.warning(self,'경고', '다른 프로그램이 실행중입니다.\n 먼저 종료해 주세요.')
      QCloseEvent.ignore() 
      return

    if self.is_force_quit == True:
      self.re = QMessageBox.question(self, "강제 종료", "강제로 종료 하시겠습니까?",
                                QMessageBox.Yes|QMessageBox.No,
                                defaultButton=QMessageBox.No)
    else:
      self.re = QMessageBox.question(self, "종료 확인", "종료 하시겠습니까?",
                                QMessageBox.Yes|QMessageBox.No,
                                defaultButton=QMessageBox.No)

    if self.re == QMessageBox.Yes:
      QCloseEvent.accept()
    else:
      QCloseEvent.ignore()     



def main():
  app = QApplication(sys.argv)

  QFontDatabase().addApplicationFont(app_path + 'data/fonts/D2Coding.ttf')    
  app.setFont(QFont('D2Coding'))
  print(app_path)
  window = MainWindow()

  center = QScreen.availableGeometry(QApplication.primaryScreen()).center()
  geo = window.frameGeometry()
  geo.moveCenter(center)
  window.move(geo.topLeft())  
  window.show()

  buf_arg = 0
  if sys.version_info[0] == 3:
      os.environ['PYTHONUNBUFFERED'] = '1'
      buf_arg = 1
  sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', buf_arg)
  sys.stderr = os.fdopen(sys.stderr.fileno(), 'w', buf_arg)

  sys.exit(app.exec())


if __name__ == "__main__":
  main()
