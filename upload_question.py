import os
import sys
import pymysql
from PySide6.QtWidgets import (QMainWindow,QFileDialog,QApplication,QMessageBox)
from PySide6.QtCore import QStringListModel
from ui_upload_question import Ui_Upload


class Upload(QMainWindow,Ui_Upload):
    def __init__(self, parent=None):
        super(Upload, self).__init__(parent)
        self.setupUi(self)
        
        self.cwd = os.getcwd()
        
        self.dir = ''
        self.files=[]
        
        self.pushButton.clicked.connect(self.open_dir)
        self.pushButton_2.clicked.connect(self.upload)
        
        
    def open_dir(self):
        self.dir = QFileDialog.getExistingDirectory(self,"选取文件夹",self.cwd) # 起始路径

        self.files = os.listdir(self.dir)
        self.model = QStringListModel()
        self.model.setStringList(self.files)
        self.listView.setModel(self.model)

    def upload(self):
        if not(self.lineEdit.text() and self.lineEdit_2.text() and self.lineEdit_3.text() and self.lineEdit_4.text() and self.lineEdit_5.text()):
            QMessageBox.information(self,"提示","数据库信息不能为空！")
            return
        elif not (self.dir and self.files):
            QMessageBox.information(self,"提示","未选中题目数据！")
            return


        root = self.dir
        files = os.listdir(root)
        try:
            for f in files:
                f = os.path.join(root,f)
                if f.endswith((".png",".PNG",".jpg")):

                    with open(f,"rb") as img:
                        raw = img.read()
                        _,q_type,q_options,q_answer,q_chapter = f.split("\\")[-1].split(".")[0].split("_")
                        
                        insert_data = [raw,q_type,q_options,q_answer,q_chapter]

                        SQL = "insert into questions(question_text,question_type,question_option,question_answer,question_chapter) values (%s,%s,%s,%s,%s)"


                        conn = pymysql.connect(
                            host=self.lineEdit.text(),
                            port=int(self.lineEdit_2.text()),
                            user=self.lineEdit_3.text(),
                            password=self.lineEdit_4.text(),
                            database=self.lineEdit_5.text()
                        )

                        cursor = conn.cursor(pymysql.cursors.DictCursor)
                        

                        cursor.execute(SQL,insert_data)

                        conn.commit()
                        cursor.close()
            QMessageBox.information(self,"提示","上传成功！")
        except Exception as e:
            conn.rollback()
            QMessageBox.information(self,"出现错误",e)
            
        finally:
            conn.close()


if __name__ == "__main__":
    app = QApplication()

    win = Upload()
    win.show()

    sys.exit(app.exec())