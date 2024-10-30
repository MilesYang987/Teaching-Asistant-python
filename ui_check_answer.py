# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'check_answereFcpTL.ui'
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
    QLabel, QLayout, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_Check(object):
    def setupUi(self, Check):
        if not Check.objectName():
            Check.setObjectName(u"Check")
        Check.resize(793, 509)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Check.sizePolicy().hasHeightForWidth())
        Check.setSizePolicy(sizePolicy)
        self.gridLayout_2 = QGridLayout(Check)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.exam_frame = QFrame(Check)
        self.exam_frame.setObjectName(u"exam_frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.exam_frame.sizePolicy().hasHeightForWidth())
        self.exam_frame.setSizePolicy(sizePolicy1)
        self.exam_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.exam_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.exam_frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.left_frame = QFrame(self.exam_frame)
        self.left_frame.setObjectName(u"left_frame")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.left_frame.sizePolicy().hasHeightForWidth())
        self.left_frame.setSizePolicy(sizePolicy2)
        self.left_frame.setMinimumSize(QSize(0, 0))
        self.left_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.left_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.left_frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.left_frame)

        self.right_frame = QFrame(self.exam_frame)
        self.right_frame.setObjectName(u"right_frame")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.right_frame.sizePolicy().hasHeightForWidth())
        self.right_frame.setSizePolicy(sizePolicy3)
        self.right_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.right_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.right_frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton_3 = QPushButton(self.right_frame)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.pushButton_3, 1, 4, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 5, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 100, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.gridLayout.addItem(self.verticalSpacer_2, 2, 4, 1, 1)

        self.label_4 = QLabel(self.right_frame)
        self.label_4.setObjectName(u"label_4")
        font = QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)

        self.gridLayout.addWidget(self.label_4, 5, 2, 1, 1)

        self.pushButton_4 = QPushButton(self.right_frame)
        self.pushButton_4.setObjectName(u"pushButton_4")
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.pushButton_4, 3, 4, 1, 1)

        self.label_3 = QLabel(self.right_frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.gridLayout.addWidget(self.label_3, 4, 2, 1, 1)

        self.pushButton_6 = QPushButton(self.right_frame)
        self.pushButton_6.setObjectName(u"pushButton_6")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy4)

        self.gridLayout.addWidget(self.pushButton_6, 5, 4, 1, 1)

        self.label = QLabel(self.right_frame)
        self.label.setObjectName(u"label")
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label, 4, 1, 1, 1)

        self.label_2 = QLabel(self.right_frame)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setFamilies([u"Microsoft YaHei UI"])
        font1.setPointSize(12)
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_2, 5, 1, 1, 1)

        self.label_5 = QLabel(self.right_frame)
        self.label_5.setObjectName(u"label_5")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy5)
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(True)
        self.label_5.setFont(font2)

        self.gridLayout.addWidget(self.label_5, 0, 1, 1, 2)

        self.horizontalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout.addItem(self.horizontalSpacer, 4, 4, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 4, 0, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 4, 3, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_5, 5, 3, 1, 1)

        self.label_6 = QLabel(self.right_frame)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 1, 0, 3, 4)


        self.horizontalLayout.addWidget(self.right_frame)

        self.right_frame.raise_()
        self.left_frame.raise_()

        self.gridLayout_2.addWidget(self.exam_frame, 0, 0, 1, 1)


        self.retranslateUi(Check)

        QMetaObject.connectSlotsByName(Check)
    # setupUi

    def retranslateUi(self, Check):
        Check.setWindowTitle("")
        self.pushButton_3.setText(QCoreApplication.translate("Check", u"\u4e0a\u4e00\u9898", None))
        self.label_4.setText("")
        self.pushButton_4.setText(QCoreApplication.translate("Check", u"\u4e0b\u4e00\u9898", None))
        self.label_3.setText("")
        self.pushButton_6.setText(QCoreApplication.translate("Check", u"\u9000\u51fa", None))
        self.label.setText(QCoreApplication.translate("Check", u"\u4f60\u7684\u7b54\u6848\uff1a", None))
        self.label_2.setText(QCoreApplication.translate("Check", u"\u6b63\u786e\u7b54\u6848\uff1a", None))
        self.label_5.setText("")
        self.label_6.setText("")
    # retranslateUi

