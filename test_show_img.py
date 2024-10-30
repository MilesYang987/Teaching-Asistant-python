# coding=utf-8
import sys
from PySide6.QtWidgets import (QWidget, QHBoxLayout, QLabel, QApplication)
from PySide6.QtGui import QPixmap,Qt


class Example (QWidget):
    def __init__(self):
        super ().__init__()
        self.initUI ()

    def initUI(self):
        hbox = QHBoxLayout (self)
        lbl = QLabel(self)
        lbl.setFixedSize(800,500)
        pixmap = QPixmap("./题目/1_single_选项1#选项2#选项3#选项4_A_1.PNG")  # 按指定路径找到图片
        pixmap = pixmap.scaledToWidth(lbl.width(),Qt.SmoothTransformation)
        lbl.setPixmap (pixmap)  # 在label上显示图片
        lbl.setScaledContents (False)  # 让图片自适应label大小
        # lbl.setPixmap(QPixmap(""))#移除label上的图片
        hbox.addWidget(lbl)

        self.setLayout (hbox)
        self.move (300, 200)
        self.setWindowTitle ('test_1')
        self.show ()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example ()
    sys.exit (app.exec())