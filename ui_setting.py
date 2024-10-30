# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settingUuYWBE.ui'
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
    QPushButton, QSizePolicy, QSpacerItem, QWidget)

class Ui_Setting(object):
    def setupUi(self, Setting):
        if not Setting.objectName():
            Setting.setObjectName(u"Setting")
        Setting.resize(272, 244)
        self.gridLayout = QGridLayout(Setting)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(Setting)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_4 = QLabel(Setting)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.pushButton = QPushButton(Setting)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 4, 0, 1, 1)

        self.pushButton_2 = QPushButton(Setting)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout.addWidget(self.pushButton_2, 4, 2, 1, 1)

        self.label_2 = QLabel(Setting)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.label_3 = QLabel(Setting)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 4, 1, 1, 1)

        self.lineEdit_4 = QLineEdit(Setting)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setEchoMode(QLineEdit.EchoMode.Password)

        self.gridLayout.addWidget(self.lineEdit_4, 3, 1, 1, 2)

        self.lineEdit_3 = QLineEdit(Setting)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.gridLayout.addWidget(self.lineEdit_3, 2, 1, 1, 2)

        self.lineEdit_2 = QLineEdit(Setting)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 2)

        self.lineEdit = QLineEdit(Setting)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 2)


        self.retranslateUi(Setting)

        QMetaObject.connectSlotsByName(Setting)
    # setupUi

    def retranslateUi(self, Setting):
        Setting.setWindowTitle(" ")
        self.label.setText(QCoreApplication.translate("Setting", u"\u5730\u5740\uff1a", None))
        self.label_4.setText(QCoreApplication.translate("Setting", u"\u5bc6\u7801\uff1a", None))
        self.pushButton.setText(QCoreApplication.translate("Setting", u"\u786e\u5b9a", None))
        self.pushButton_2.setText(QCoreApplication.translate("Setting", u"\u53d6\u6d88", None))
        self.label_2.setText(QCoreApplication.translate("Setting", u"\u7aef\u53e3\uff1a", None))
        self.label_3.setText(QCoreApplication.translate("Setting", u"\u7528\u6237\u540d\uff1a", None))
        self.lineEdit_2.setText(QCoreApplication.translate("Setting", u"3306", None))
        self.lineEdit.setText(QCoreApplication.translate("Setting", u"localhost", None))
    # retranslateUi

