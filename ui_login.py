# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loginRXFvaL.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Login(object):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName(u"Login")
        Login.resize(356, 370)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Login.sizePolicy().hasHeightForWidth())
        Login.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(Login)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(Login)
        self.frame.setObjectName(u"frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(13)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.label_2)


        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(Login)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy2)
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.frame_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        font1 = QFont()
        font1.setPointSize(13)
        self.label_3.setFont(font1)

        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)

        self.lineEdit = QLineEdit(self.frame_2)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setFont(font1)

        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)

        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(self.frame_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setFont(font1)
        self.lineEdit_2.setEchoMode(QLineEdit.EchoMode.Password)

        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(Login)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy3)
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_4 = QPushButton(self.frame_3)
        self.pushButton_4.setObjectName(u"pushButton_4")
        font2 = QFont()
        font2.setPointSize(10)
        self.pushButton_4.setFont(font2)
        self.pushButton_4.setFlat(False)

        self.horizontalLayout_2.addWidget(self.pushButton_4)

        self.pushButton_3 = QPushButton(self.frame_3)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setFont(font2)

        self.horizontalLayout_2.addWidget(self.pushButton_3)

        self.pushButton = QPushButton(self.frame_3)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setFont(font2)

        self.horizontalLayout_2.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.frame_3)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setFont(font2)

        self.horizontalLayout_2.addWidget(self.pushButton_2)


        self.verticalLayout.addWidget(self.frame_3)


        self.retranslateUi(Login)

        QMetaObject.connectSlotsByName(Login)
    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"\u6b22\u8fce\u4f7f\u7528\u300a\u7535\u8def\u7406\u8bba\u57fa\u7840\u300b\u667a\u80fd\u8f85\u52a9\u6559\u5b66\u7cfb\u7edf", None))
        self.label_2.setText(QCoreApplication.translate("Login", u"\u300a\u7535\u8def\u7406\u8bba\u57fa\u7840\u300b\u667a\u80fd\u8f85\u52a9\u6559\u5b66\u7cfb\u7edf", None))
        self.label_3.setText(QCoreApplication.translate("Login", u"\u7528\u6237\u540d\uff1a", None))
        self.label_4.setText(QCoreApplication.translate("Login", u"\u5bc6\u7801\uff1a", None))
        self.pushButton_4.setText(QCoreApplication.translate("Login", u"\u8bbe\u7f6e", None))
        self.pushButton_3.setText(QCoreApplication.translate("Login", u"\u6ce8\u518c", None))
        self.pushButton.setText(QCoreApplication.translate("Login", u"\u767b\u5f55", None))
        self.pushButton_2.setText(QCoreApplication.translate("Login", u"\u9000\u51fa", None))
    # retranslateUi

