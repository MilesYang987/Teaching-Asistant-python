# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'upload_questionEkLoLa.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication,QMetaObject)
from PySide6.QtWidgets import (QGridLayout, QLabel, QLineEdit,QListView,QPushButton, QSizePolicy,
    QWidget)

class Ui_Upload(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(492, 364)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout.addWidget(self.pushButton_2, 0, 2, 1, 1)

        self.listView = QListView(self.centralwidget)
        self.listView.setObjectName(u"listView")

        self.gridLayout.addWidget(self.listView, 1, 0, 5, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)

        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout.addWidget(self.lineEdit, 1, 2, 1, 1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 2, 1, 1, 1)

        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout.addWidget(self.lineEdit_2, 2, 2, 1, 1)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 3, 1, 1, 1)

        self.lineEdit_3 = QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.gridLayout.addWidget(self.lineEdit_3, 3, 2, 1, 1)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 4, 1, 1, 1)

        self.lineEdit_4 = QLineEdit(self.centralwidget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.gridLayout.addWidget(self.lineEdit_4, 4, 2, 1, 1)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 5, 1, 1, 1)

        self.lineEdit_5 = QLineEdit(self.centralwidget)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.gridLayout.addWidget(self.lineEdit_5, 5, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u9898\u76ee\u4e0a\u4f20", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u6587\u4ef6\u5939", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u4e0a\u4f20", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u5730\u5740\uff1a", None))
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"localhost", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u7aef\u53e3\uff1a", None))
        self.lineEdit_2.setText(QCoreApplication.translate("MainWindow", u"3306", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u7528\u6237\uff1a", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u5bc6\u7801\uff1a", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u6570\u636e\u5e93\uff1a", None))
        self.lineEdit_5.setText(QCoreApplication.translate("MainWindow", u"teaching", None))
    # retranslateUi

