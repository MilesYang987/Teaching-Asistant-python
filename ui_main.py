# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_mainZVFUdX.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QFrame,
    QHBoxLayout, QHeaderView, QLabel, QMainWindow,
    QPlainTextEdit, QPushButton, QScrollArea, QSizePolicy,
    QTableView, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(874, 485)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.pushButton_2 = QPushButton(self.frame_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        font = QFont()
        font.setPointSize(13)
        self.pushButton_2.setFont(font)

        self.verticalLayout_3.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.frame_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setFont(font)

        self.verticalLayout_3.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.frame_2)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setFont(font)

        self.verticalLayout_3.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.frame_2)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setFont(font)

        self.verticalLayout_3.addWidget(self.pushButton_5)


        self.horizontalLayout_2.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy1)
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame = QFrame(self.frame_3)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(246, 246, 246);\n"
"border-radius:20px;\n"
"border:3px solid #34495e;\n"
"")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.scrollArea = QScrollArea(self.frame)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"border:initial;\n"
"border: 0px solid;")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 203, 365))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.scrollArea)


        self.verticalLayout_6.addWidget(self.frame)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.plainTextEdit = QPlainTextEdit(self.frame_3)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.plainTextEdit.sizePolicy().hasHeightForWidth())
        self.plainTextEdit.setSizePolicy(sizePolicy2)
        self.plainTextEdit.setMaximumSize(QSize(16777215, 50))
        self.plainTextEdit.setStyleSheet(u"QPlainTextEdit{\n"
"	border-radius:20px;\n"
"	border:3px solid #2c3e50;\n"
"	background-color: transparent;\n"
"	font: 12pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"	padding:5px;\n"
"}")

        self.horizontalLayout.addWidget(self.plainTextEdit)

        self.pushButton = QPushButton(self.frame_3)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMaximumSize(QSize(80, 16777215))
        font1 = QFont()
        font1.setPointSize(12)
        self.pushButton.setFont(font1)

        self.horizontalLayout.addWidget(self.pushButton)

        self.horizontalLayout.setStretch(1, 1)

        self.verticalLayout_6.addLayout(self.horizontalLayout)


        self.horizontalLayout_2.addWidget(self.frame_3)

        self.enter_frame = QFrame(self.centralwidget)
        self.enter_frame.setObjectName(u"enter_frame")
        sizePolicy1.setHeightForWidth(self.enter_frame.sizePolicy().hasHeightForWidth())
        self.enter_frame.setSizePolicy(sizePolicy1)
        self.enter_frame.setFrameShape(QFrame.Shape.Box)
        self.enter_frame.setFrameShadow(QFrame.Shadow.Plain)
        self.enter_frame.setLineWidth(2)
        self.enter_frame.setMidLineWidth(0)
        self.verticalLayout_5 = QVBoxLayout(self.enter_frame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label = QLabel(self.enter_frame)
        self.label.setObjectName(u"label")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy3)
        font2 = QFont()
        font2.setPointSize(21)
        self.label.setFont(font2)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.label)

        self.label_2 = QLabel(self.enter_frame)
        self.label_2.setObjectName(u"label_2")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy4)
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_2, 0, Qt.AlignmentFlag.AlignHCenter)

        self.comboBox = QComboBox(self.enter_frame)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        sizePolicy4.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy4)
        self.comboBox.setFont(font1)

        self.verticalLayout_5.addWidget(self.comboBox, 0, Qt.AlignmentFlag.AlignHCenter)

        self.pushButton_7 = QPushButton(self.enter_frame)
        self.pushButton_7.setObjectName(u"pushButton_7")
        sizePolicy4.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy4)
        self.pushButton_7.setFont(font1)

        self.verticalLayout_5.addWidget(self.pushButton_7, 0, Qt.AlignmentFlag.AlignHCenter)


        self.horizontalLayout_2.addWidget(self.enter_frame)

        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.tableView = QTableView(self.frame_4)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)

        self.verticalLayout_4.addWidget(self.tableView)


        self.horizontalLayout_2.addWidget(self.frame_4)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u300a\u7535\u8def\u7406\u8bba\u57fa\u7840\u300b\u8f85\u52a9\u6559\u5b66\u7cfb\u7edf", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u77e5\u8bc6\u54a8\u8be2", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u6a21\u62df\u4e60\u9898", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u9519\u9898\u5206\u6790", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"\u9000\u51fa", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u53d1\u9001", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u300a\u7535\u8def\u7406\u8bba\u57fa\u7840\u300b\u7ec3\u4e60\u9898", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u8bf7\u9009\u62e9\u7ae0\u8282\uff1a", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u7b2c\u4e00\u7ae0", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"\u7b2c\u4e8c\u7ae0", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"\u7b2c\u4e09\u7ae0", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"\u7b2c\u56db\u7ae0", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"\u7b2c\u4e94\u7ae0", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"\u7efc\u5408", None))

        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb", None))
    # retranslateUi

