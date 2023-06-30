import time
import serial
import serial.tools.list_ports as sp
from serial import Serial
from PySide6.QtCore import QThread, QObject, Signal


class SerialThread(QThread):
  rxd_sig = Signal(bytes)

  def __init__(self, port):
    super().__init__()
    self.working = True    
    self.is_enable = True
    self.is_next_enable = True
    self.serial_port = port

  def __del__(self):
    pass
    
  def run(self):
    while self.working:
      if self.is_enable:
        if self.serial_port.is_open == True:                
          read_data = self.serial_port.read()
          self.rxd_sig.emit(read_data)
        else:  
          self.sleep(0.001)
      else:
        self.sleep(0.001)

      self.is_enable = self.is_next_enable

  def setEnableThread(self, value):
    self.is_next_enable = value
    while self.is_next_enable is not self.is_enable:
      self.msleep(10)

  def setRxdSignal(self, receive_func):
    self.rxd_sig.connect(receive_func)

  def stop(self):
    self.working = False


class Uart:

  def __init__(self):
    self.is_init = False
    self.is_open = False
    
    self.baud_list = [9600, 57600, 115200, 1000000, 2000000, 4000000]
    self.port = ""
    self.baud = 0
    self.is_read = False
    self.is_write = False
    self.uart_port = None
    self.rxd_thread = SerialThread(self)    
    self.rxd_thread.start()    

  def __del__(self):
    print('uart exit')
    if self.is_open == True:
      self.close()
    self.rxd_thread.stop()

  def open(self, port, baud):
    if self.is_open == True:
      self.close()

    self.port = port
    self.baud = baud
    try :
      self.uart_port = serial.Serial(port, baud, timeout=None)      
      self.is_open = True
      #self.uart_port.timeout = 0.1
      print('Uart::open() OK')
    except :
      self.is_open = False
      print('Uart::open() Fail')

    return self.is_open

  def close(self):  
    if self.uart_port is not None:
      if self.uart_port.is_open == True:
        self.is_open = False

        self.uart_port.cancel_read()
        self.uart_port.cancel_write() 
        timeout_cnt = 0
        while self.is_read:
          time.sleep(0.01)
          timeout_cnt += 1
          if (timeout_cnt > 100):
            break

        timeout_cnt = 0 
        while self.is_write:
          time.sleep(0.01)
          timeout_cnt += 1
          if (timeout_cnt > 100):
            break

        self.uart_port.close()        
        print('Uart::close()')

  def quit(self):
    self.close()
    self.rxd_thread.stop()

  def isOpen(self):
    return self.is_open

  def available(self):
    if self.is_open is True:
      return self.uart_port.inWaiting()
    else:
      return 0

  def read(self, size=1):
    if self.is_open is True:
      self.is_read = True
      ret = self.uart_port.read(size)
      self.is_read = False
      return ret
    else:
      return 0

  def write(self, data):
    if self.is_open is True:
      self.is_write = True
      self.uart_port.write(data)
      self.is_write = False
      
  def flush(self):
    if self.is_open is True:
      self.uart_port.flush()
      self.uart_port.reset_input_buffer()
      self.uart_port.reset_output_buffer()

  def getBaudList(self):
    return sorted(self.baud_list)

  def getPortList(self):
    return sorted(sp.comports())

  def setRxdSignal(self, rxd_func):
    self.rxd_thread.setRxdSignal(rxd_func)
