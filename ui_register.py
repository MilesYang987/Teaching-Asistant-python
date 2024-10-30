# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'registereByWeH.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Register_Form(object):
    def setupUi(self, Register_Form):
        if not Register_Form.objectName():
            Register_Form.setObjectName(u"Register_Form")
        Register_Form.resize(266, 310)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Register_Form.sizePolicy().hasHeightForWidth())
        Register_Form.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(Register_Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(Register_Form)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(12)
        self.label.setFont(font)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.lineEdit = QLineEdit(Register_Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setFont(font)

        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)

        self.label_2 = QLabel(Register_Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(Register_Form)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setFont(font)

        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)

        self.label_3 = QLabel(Register_Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.lineEdit_3 = QLineEdit(Register_Form)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setEchoMode(QLineEdit.EchoMode.Password)

        self.gridLayout.addWidget(self.lineEdit_3, 2, 1, 1, 1)

        self.pushButton = QPushButton(Register_Form)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy1)
        self.pushButton.setFont(font)

        self.gridLayout.addWidget(self.pushButton, 3, 0, 1, 1)

        self.pushButton_2 = QPushButton(Register_Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy1.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy1)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.gridLayout.addWidget(self.pushButton_2, 3, 1, 1, 1)


        self.retranslateUi(Register_Form)

        QMetaObject.connectSlotsByName(Register_Form)
    # setupUi

    def retranslateUi(self, Register_Form):
        Register_Form.setWindowTitle(QCoreApplication.translate("Register_Form", u"\u6ce8\u518c", None))
        self.label.setText(QCoreApplication.translate("Register_Form", u"\u59d3\u540d\uff1a", None))
        self.label_2.setText(QCoreApplication.translate("Register_Form", u"\u5b66\u53f7\uff1a", None))
        self.label_3.setText(QCoreApplication.translate("Register_Form", u"\u5bc6\u7801\uff1a", None))
        self.pushButton.setText(QCoreApplication.translate("Register_Form", u"\u6ce8\u518c", None))
        self.pushButton_2.setText(QCoreApplication.translate("Register_Form", u"\u8fd4\u56de", None))
    # retranslateUi

