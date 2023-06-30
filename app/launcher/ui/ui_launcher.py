# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_launcher.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QMainWindow, QMenuBar, QPlainTextEdit,
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_Launcher(object):
    def setupUi(self, Launcher):
        if not Launcher.objectName():
            Launcher.setObjectName(u"Launcher")
        Launcher.resize(733, 643)
        Launcher.setContextMenuPolicy(Qt.NoContextMenu)
        self.centralwidget = QWidget(Launcher)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QSize(0, 160))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame)
        self.verticalLayout_5.setSpacing(7)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(12, 3, -1, 12)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)

        self.horizontalLayout_2.addWidget(self.label)

        self.combo_port = QComboBox(self.frame)
        self.combo_port.setObjectName(u"combo_port")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.combo_port.sizePolicy().hasHeightForWidth())
        self.combo_port.setSizePolicy(sizePolicy2)
        self.combo_port.setMinimumSize(QSize(300, 0))

        self.horizontalLayout_2.addWidget(self.combo_port)

        self.btn_scan = QPushButton(self.frame)
        self.btn_scan.setObjectName(u"btn_scan")
        sizePolicy2.setHeightForWidth(self.btn_scan.sizePolicy().hasHeightForWidth())
        self.btn_scan.setSizePolicy(sizePolicy2)
        self.btn_scan.setSizeIncrement(QSize(0, 0))
        self.btn_scan.setBaseSize(QSize(0, 0))

        self.horizontalLayout_2.addWidget(self.btn_scan)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout_5.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)

        self.horizontalLayout_4.addWidget(self.label_2)

        self.combo_baud = QComboBox(self.frame)
        self.combo_baud.setObjectName(u"combo_baud")
        sizePolicy2.setHeightForWidth(self.combo_baud.sizePolicy().hasHeightForWidth())
        self.combo_baud.setSizePolicy(sizePolicy2)
        self.combo_baud.setMinimumSize(QSize(300, 0))

        self.horizontalLayout_4.addWidget(self.combo_baud)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)


        self.verticalLayout_5.addLayout(self.horizontalLayout_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.label_3)

        self.combo_file = QComboBox(self.frame)
        self.combo_file.setObjectName(u"combo_file")

        self.horizontalLayout.addWidget(self.combo_file)

        self.btn_browse = QPushButton(self.frame)
        self.btn_browse.setObjectName(u"btn_browse")
        sizePolicy2.setHeightForWidth(self.btn_browse.sizePolicy().hasHeightForWidth())
        self.btn_browse.setSizePolicy(sizePolicy2)

        self.horizontalLayout.addWidget(self.btn_browse)


        self.verticalLayout_5.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        sizePolicy1.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy1)

        self.horizontalLayout_3.addWidget(self.label_4)

        self.combo_part = QComboBox(self.frame)
        self.combo_part.setObjectName(u"combo_part")
        sizePolicy2.setHeightForWidth(self.combo_part.sizePolicy().hasHeightForWidth())
        self.combo_part.setSizePolicy(sizePolicy2)
        self.combo_part.setMinimumSize(QSize(300, 0))

        self.horizontalLayout_3.addWidget(self.combo_part)

        self.btn_flash = QPushButton(self.frame)
        self.btn_flash.setObjectName(u"btn_flash")

        self.horizontalLayout_3.addWidget(self.btn_flash)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)


        self.verticalLayout_5.addLayout(self.horizontalLayout_3)


        self.verticalLayout_4.addWidget(self.frame)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.log = QPlainTextEdit(self.frame_2)
        self.log.setObjectName(u"log")

        self.verticalLayout_6.addWidget(self.log)


        self.verticalLayout_4.addWidget(self.frame_2)

        Launcher.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Launcher)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 733, 24))
        Launcher.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Launcher)
        self.statusbar.setObjectName(u"statusbar")
        Launcher.setStatusBar(self.statusbar)

        self.retranslateUi(Launcher)

        QMetaObject.connectSlotsByName(Launcher)
    # setupUi

    def retranslateUi(self, Launcher):
        Launcher.setWindowTitle(QCoreApplication.translate("Launcher", u"ESP32-BOY-GUI", None))
        self.label.setText(QCoreApplication.translate("Launcher", u"PORT", None))
        self.btn_scan.setText(QCoreApplication.translate("Launcher", u"SCAN", None))
        self.label_2.setText(QCoreApplication.translate("Launcher", u"BAUD", None))
        self.label_3.setText(QCoreApplication.translate("Launcher", u"FILE", None))
        self.btn_browse.setText(QCoreApplication.translate("Launcher", u"Browse", None))
        self.label_4.setText(QCoreApplication.translate("Launcher", u"PART", None))
        self.btn_flash.setText(QCoreApplication.translate("Launcher", u"FLASH", None))
    # retranslateUi

