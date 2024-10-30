from PySide6 import QtGui,QtCore
from PySide6.QtWidgets import (QApplication,QMainWindow,QHBoxLayout,QCheckBox,QButtonGroup,
    QWidget,QFrame,QGridLayout,QPushButton,QSizePolicy,QLabel,QRadioButton,
    QMessageBox,QHeaderView)
from PySide6.QtGui import QFont, QFontMetrics,QStandardItemModel,QStandardItem,QPixmap,Qt
from PySide6.QtCore import Qt,Signal,QTimer
import sys
from new_widget import Set_question
import pymysql.cursors
from ui_main import Ui_MainWindow
from ui_login import Ui_Login
from ui_exam import Ui_Exam
from ui_check_answer import Ui_Check
from ui_register import Ui_Register_Form
from ui_setting import Ui_Setting
import threading
import qianfan
import pymysql
from functools import partial
import datetime
from configparser import ConfigParser

CONFIG_FILE = "config.ini"

selection_text = ["A","B","C","D"]

SINGLE_NUMBER = 10
MULTI_NUMBER = 5
SINGLE_SCORE = 3
MULTI_SCORE = 5
EXAM_TIME = 20*60


CONNECT_DICT = {
    "host":"localhost",
    "port":3306,
    "user":"root",
    "password":"0000",
    "database":"teaching"
}


def excute_SQL(SQL:str,args,many_flag=False):
    data = None
    
    try:
        conn = pymysql.connect(**CONNECT_DICT)
    except:
        return data
    
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    
    try:
        if not many_flag:
            cursor.execute(SQL,args)
        else:
            cursor.executemany(SQL,args)
        conn.commit()
        data = cursor.fetchall()
    except:
        conn.rollback()
        data = None
    finally:
        cursor.close()
        conn.close()

    return data


class SettingWindow(QWidget,Ui_Setting):
    def __init__(self,login,parent=None):
        super(SettingWindow, self).__init__(parent)
        self.setupUi(self)
        
        self.login = login
        
        self.pushButton.clicked.connect(self.update_connect_dict)
        self.pushButton_2.clicked.connect(self.close)
        
        config = ConfigParser()
        config.read(CONFIG_FILE)
        if config.get("mysql","first") != "true":
            self.lineEdit_3.setText(CONNECT_DICT["user"])
            self.lineEdit_4.setText(CONNECT_DICT["password"])
        
    def update_connect_dict(self):
        if not (self.lineEdit.text() and self.lineEdit_2.text() and self.lineEdit_3.text() and self.lineEdit_4.text()):
            box = QMessageBox()
            box.setWindowTitle(" ")
            box.setIcon(QMessageBox.Warning)
            box.setText("字段不能为空")
            box.addButton("确定",QMessageBox.ButtonRole.AcceptRole)
            box.exec()
            return

        _dict = {
            "host":self.lineEdit.text(),
            "port":int(self.lineEdit_2.text()),
            "user":self.lineEdit_3.text(),
            "password":self.lineEdit_4.text(),
        }
        
        CONNECT_DICT.update(_dict)
        try:
            conn = pymysql.connect(**CONNECT_DICT)
            conn.close()
        except Exception as e:
            box = QMessageBox()
            box.setWindowTitle("连接错误")
            box.setIcon(QMessageBox.Warning)
            box.setText(str(e))
            box.addButton("确定",QMessageBox.ButtonRole.AcceptRole)
            box.exec()
        else:
            box = QMessageBox()
            box.setWindowTitle(" ")
            box.setIcon(QMessageBox.Warning)
            box.setText("连接成功！")
            box.addButton("确定",QMessageBox.ButtonRole.AcceptRole)
            box.exec()
            
            config = ConfigParser()
            config.read(CONFIG_FILE)
            config.set("mysql","first","false")
            for k,v in CONNECT_DICT.items():
                config.set("mysql",k,str(v))
            
            with open(CONFIG_FILE, "w+") as config_file:
                config.write(config_file)

            self.close()
        
    def closeEvent(self,event):
        self.login.show()
        self.deleteLater()


class LoginWindow(QWidget,Ui_Login):
    def __init__(self,main,parent=None):
        super(LoginWindow, self).__init__(parent)
        self.setupUi(self)
        self.main_window = main
        
        self.pushButton.clicked.connect(self.login)
        self.pushButton_3.clicked.connect(self.register)
        self.pushButton_2.clicked.connect(self.quit)
        self.pushButton_4.clicked.connect(self.open_setting)
        
        config = ConfigParser()
        config.read(CONFIG_FILE)
        if config.get("mysql","first") == "true":
            self.open_setting()
        else:
            self.show()
        
    def open_setting(self):
        self.hide()
        self.setting = SettingWindow(self)
        self.setting.show()


    
    def quit(self):
        self.deleteLater()
        self.main_window.deleteLater()
        
    def register(self):
        self.hide()
        self.reg = RegisterWindow(self)
        self.reg.show()

    
    def login(self):
        name = self.lineEdit.text()
        password = self.lineEdit_2.text()
        
        if not (name and password):
            box = QMessageBox()
            box.setWindowTitle(" ")
            box.setIcon(QMessageBox.Warning)
            box.setText("姓名或密码不能为空！")
            box.addButton("确定",QMessageBox.ButtonRole.AcceptRole)
            box.exec()
            return
        
        SQL = "select student_id,student_password from student_info where student_name=%s"
        result = excute_SQL(SQL,name)
        
        if result is None:
            box = QMessageBox()
            box.setWindowTitle(" ")
            box.setIcon(QMessageBox.Warning)
            box.setText(f"不存在的用户：{name}！")
            box.addButton("确定",QMessageBox.ButtonRole.AcceptRole)
            box.exec()
            return
        elif result[0]["student_password"] != password:
            box = QMessageBox()
            box.setWindowTitle(" ")
            box.setIcon(QMessageBox.Warning)
            box.setText(f"密码错误！")
            box.addButton("确定",QMessageBox.ButtonRole.AcceptRole)
            box.exec()
            return
        else:
            self.hide()
            self.main_window.set_name(name,result[0]["student_id"])
            self.main_window.show()
            self.main_window.setup_table()


class RegisterWindow(QWidget,Ui_Register_Form):
    def __init__(self,login,parent=None):
        super(RegisterWindow, self).__init__(parent)
        self.setupUi(self)
        
        self.login = login
        
        self.pushButton.clicked.connect(self.register)
        self.pushButton_2.clicked.connect(self.close)
    
    
    def register(self):
        if not (self.lineEdit.text() and self.lineEdit_2.text() and self.lineEdit_3.text()):
            box = QMessageBox()
            box.setWindowTitle(" ")
            box.setIcon(QMessageBox.Warning)
            box.setText(f"字段不能为空！")
            box.addButton("确定",QMessageBox.ButtonRole.AcceptRole)
            box.exec()
            return
        
        SQL = "insert into student_info(student_id,student_name,student_password) values(%s,%s,%s)"
        insert_data = [int(self.lineEdit_2.text()),self.lineEdit.text(),self.lineEdit_3.text()]
        res = excute_SQL(SQL,insert_data)
        
        self.close()

        
    def closeEvent(self,event):
        self.login.show()
        self.deleteLater()
        

class ExamWindow(QWidget,Ui_Exam):
    def __init__(self, main,chapter,parent=None):
        super(ExamWindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.main_window = main
        
        self.chapter = chapter
        self.student_name = self.main_window.student_name
        self.student_id = self.main_window.student_id
        
        # self.label.setAlignment(Qt.AlignTop)
        self.label_6.setText(f"姓名：{self.student_name:^10}学号：{self.student_id:^10}")

        self.current_question=0

        self.pushButton_3.clicked.connect(lambda:self.update_question(self.current_question-1))
        self.pushButton_4.clicked.connect(lambda:self.update_question(self.current_question+1))
        self.pushButton_5.clicked.connect(self.click_upload)
        self.pushButton_6.clicked.connect(self.click_exit)
        
        self.single_num=SINGLE_NUMBER
        self.multi_num=MULTI_NUMBER
        self.exam_time = EXAM_TIME
        
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.display_time)
        
        self.single_score = SINGLE_SCORE
        self.multi_score = MULTI_SCORE
        
        self.show()
        self._init_selection_layout()
        self.start_exam()
        
    def _init_selection_layout(self):
        self.selection_layout = QHBoxLayout()
        _font = QFont()
        _font.setPointSize(10)

        self.single_buttons = QButtonGroup(self)
        for _i in range(4):
            _b = QRadioButton(self.right_frame)
            _b.setFont(_font)
            self.single_buttons.addButton(_b,_i)
            self.selection_layout.addWidget(_b)
            _b.hide()
        
        self.single_buttons.buttonClicked.connect(self.update_single_answer)
        
        self.multi_buttons = QButtonGroup(self)
        self.multi_buttons.setExclusive(False)
        for _i in range(4):
            _b = QCheckBox(self.right_frame)
            _b.setFont(_font)
            self.multi_buttons.addButton(_b,_i)
            self.selection_layout.addWidget(_b)
            _b.hide()
        self.multi_buttons.buttonClicked.connect(self.update_multi_answer)

        self.gridLayout.addLayout(self.selection_layout,4,0,1,4)

    def display_time(self):
        time_string = f"{self.exam_time//60:0>2d}:{self.exam_time%60:0>2d}"
        self.label_4.setText(time_string)
        self.exam_time-=1
        
        if self.exam_time == 0:
            self.timer.stop()
            
            box = QMessageBox()
            box.setWindowTitle(" ")
            box.setIcon(QMessageBox.Information)
            box.setText("时间到，考试结束。")
            yes = box.addButton("确定",QMessageBox.ButtonRole.AcceptRole)
            
            _timer = QTimer(self)
            _timer.singleShot(5000,yes.click)
            _timer.start()
            
            box.exec()
        
            self.upload_answer()
            self.deleteLater()
            self.main_window.show()



    def closeEvent(self,event):
        self.main_window.show()
        self.hide()
        
    def start_exam(self):
        #add sql questions
        if self.chapter == 0:
            SQL = "select * from questions where question_type='single' order by rand() limit %s"
            self.single_questions = excute_SQL(SQL,self.single_num)
            
            SQL = "select * from questions where question_type='multi' order by rand() limit %s"
            self.multi_questions = excute_SQL(SQL,self.multi_num)
        else:
            SQL = "select * from questions where question_type='single' and question_chapter=%s order by rand() limit %s"
            self.single_questions = excute_SQL(SQL,[self.chapter,self.single_num])
            
            SQL = "select * from questions where question_type='multi' and question_chapter=%s order by rand() limit %s"
            self.multi_questions = excute_SQL(SQL,[self.chapter,self.single_num])

        
        self.exam_data = self.single_questions+self.multi_questions
        self.answers = {}
        
        self.question_num = len(self.exam_data)
        
        
        single_frame = QFrame(self.left_frame)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        single_frame.setSizePolicy(sizePolicy)
        grid_layout = QGridLayout(single_frame)
        
        self.shortcut_buttons = QButtonGroup(self)
        for _i in range(len(self.single_questions)):
            _b = QPushButton(single_frame)
            _b.setFixedSize(20,20)
            _b.setStyleSheet("color: red;")
            _b.setText(str(_i+1))
            grid_layout.addWidget(_b,_i//4,_i%4,1,1)
            
            _b.clicked.connect(partial(self.update_question,_i))
            self.shortcut_buttons.addButton(_b,_i)

        self.verticalLayout.insertWidget(self.verticalLayout.indexOf(self.verticalSpacer),QLabel(u"单选题",self.left_frame))
        self.verticalLayout.insertWidget(self.verticalLayout.indexOf(self.verticalSpacer),single_frame)


        multi_frame = QFrame(self.left_frame)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        multi_frame.setSizePolicy(sizePolicy)
        grid_layout = QGridLayout(multi_frame)
        
        for _i in range(len(self.multi_questions)):
            _b = QPushButton(multi_frame)
            _b.setFixedSize(20,20)
            _b.setStyleSheet("color: red;")
            _b.setText(str(_i+1))
            grid_layout.addWidget(_b,_i//4,_i%4,1,1)
            
            _b.clicked.connect(partial(self.update_question,_i+len(self.single_questions)))
            self.shortcut_buttons.addButton(_b,_i+len(self.single_questions))


        self.verticalLayout.insertWidget(self.verticalLayout.indexOf(self.verticalSpacer),QLabel(u"多选题",self.left_frame))
        self.verticalLayout.insertWidget(self.verticalLayout.indexOf(self.verticalSpacer),multi_frame)

        self.update_question(0)
        self.timer.start(1000)


    def update_question(self,index):
        self.current_question = index
        if self.current_question == 0:
            self.pushButton_3.setDisabled(True)
            self.pushButton_4.setEnabled(True)
        elif self.current_question == self.question_num-1:
            self.pushButton_4.setDisabled(True)
            self.pushButton_3.setEnabled(True)
        else:
            self.pushButton_3.setEnabled(True)
            self.pushButton_4.setEnabled(True)
        
        for _i in range(self.selection_layout.count()):
            self.selection_layout.itemAt(_i).widget().hide()


        data = self.exam_data[index]
        question_id = data["question_id"]
        
        _img = QPixmap()
        _img.loadFromData(data['question_text'])
        # _s = _img.size()
        if _img.height() < _img.width():
            _img = _img.scaledToWidth(self.label.width())
        else:
            _img = _img.scaledToHeight(self.label.height())
        self.label.setPixmap(_img)
        
        if data['question_type'] == "single":
            options = data['question_option'].split("#")
            for _i,_o in enumerate(options):
                self.single_buttons.button(_i).setText(selection_text[_i]+". "+_o)
                self.single_buttons.button(_i).show()
                self.single_buttons.setExclusive(False)
                self.single_buttons.button(_i).setChecked(False)
                self.single_buttons.setExclusive(True)

            if question_id in self.answers:
                self.single_buttons.button(selection_text.index(self.answers[question_id])).setChecked(True)
            
        elif data['question_type'] == "multi":
            options = data['question_option'].split("#")
            for _i,_o in enumerate(options):
                self.multi_buttons.button(_i).setText(selection_text[_i]+". "+_o)
                self.multi_buttons.button(_i).show()
                self.multi_buttons.button(_i).setChecked(False)
                
            if question_id in self.answers:
                for _c in self.answers[question_id]:
                    self.multi_buttons.button(selection_text.index(_c)).setChecked(True)
            
        _string = f"题目：{index+1:>2}/{self.question_num:>2}"
        self.label_5.setText(_string)

    def update_single_answer(self,btn:QRadioButton):
        _answer = {}
        question_id = self.exam_data[self.current_question]["question_id"]
        _answer[question_id] = btn.text()[0]
        self.answers.update(_answer)
        
        self.shortcut_buttons.button(self.current_question).setStyleSheet("color: black;")


    def update_multi_answer(self,btn:QCheckBox):
        _answer = {}
        selections = []
        for _b in self.multi_buttons.buttons():
            if _b.isChecked():
                selections.append(_b.text()[0])
        selections = "".join(selections)
                
        question_id = self.exam_data[self.current_question]["question_id"]
        _answer[question_id] = selections
        self.answers.update(_answer)

        self.shortcut_buttons.button(self.current_question).setStyleSheet("color: black;")



    def upload_answer(self):
                
        questions = [_d["question_id"] for _d in self.exam_data]

        answers = ["0"]*len(questions)
        for i,q in enumerate(questions):
            if q in self.answers:
                answers[i] = self.answers[q] if self.answers[q] else "0"

        questions = "#".join(list(map(str,questions)))
        answers = "#".join(answers)
        
        score = 0
        for k,v in self.answers.items():
            for _d in self.exam_data:
                if k == _d["question_id"] and v in _d["question_answer"]:
                    if _d["question_type"] == "single":
                        score += self.single_score
                    elif _d["question_type"] == "multi":
                        if v == _d["question_answer"]:
                            score += self.multi_score
                        else:
                            score += self.multi_score-3
                    break
        _datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        data = [self.student_id,self.student_name,questions,answers,score,_datetime,self.chapter]
        SQL = "insert into exam_result(student_id,student_name,questions,answers,score,exam_time,exam_chapter) values(%s,%s,%s,%s,%s,%s,%s)"
        excute_SQL(SQL,data)
        

    def click_upload(self):
        if len(self.answers) < len(self.exam_data):
            box = QMessageBox()
            box.setWindowTitle(" ")
            box.setIcon(QMessageBox.Question)
            box.setText("您还有未完成的题目，确认交卷吗？")
            yes = box.addButton("是",QMessageBox.ButtonRole.YesRole)
            box.addButton("否",QMessageBox.ButtonRole.NoRole)
            
            box.exec()
        
            if  box.clickedButton() == yes:
                self.upload_answer()
                self.deleteLater()
                self.main_window.show()
            else:
                pass
        else:
            box = QMessageBox()
            box.setWindowTitle(" ")
            box.setIcon(QMessageBox.Question)
            box.setText("确认交卷吗？")
            yes = box.addButton("是",QMessageBox.ButtonRole.YesRole)
            box.addButton("否",QMessageBox.ButtonRole.NoRole)
            
            box.exec()
        
            if  box.clickedButton() == yes:
                self.upload_answer()
                self.deleteLater()
                self.main_window.show()
            else:
                pass


    def click_exit(self):
        box = QMessageBox()
        box.setWindowTitle(" ")
        box.setIcon(QMessageBox.Question)
        box.setText("退出考试无法保存结果，确认退出吗？")
        yes = box.addButton("是",QMessageBox.ButtonRole.YesRole)
        box.addButton("否",QMessageBox.ButtonRole.NoRole)
        
        box.exec()
        
        if  box.clickedButton() == yes:
            self.deleteLater()
            self.main_window.show()
        else:
            pass


    def close(self):
        self.deleteLater()
        self.main_window.show()


class CheckWindow(QWidget,Ui_Check):
    def __init__(self,main,exam_id,parent=None):
        super(CheckWindow, self).__init__(parent)
        self.setupUi(self)
        self.exam_id = exam_id
        self.main_window = main

        SQL = "select questions,answers from exam_result where exam_id=%s"
        result = excute_SQL(SQL,self.exam_id)[0]
        
        self.questions = list(map(int,result["questions"].split("#")))
        self.user_answers = result["answers"].split("#")
        
        self.single_questions = []
        self.multi_questions = []
        
        SQL = f"select * from questions where question_id in ({",".join(list(map(str,self.questions)))})"
        result = excute_SQL(SQL,None)
        
        self.correct_answers = {}
        for d in result:
            self.correct_answers[d["question_id"]] = d["question_answer"]
            if d["question_type"] == "single":
                self.single_questions.append(d)
            elif d["question_type"] == "multi":
                self.multi_questions.append(d)
        
        self.exam_data = []
        for q in self.questions:
            for r in result:
                if r["question_id"] == q:
                    self.exam_data.append(r)
                    break
        self.question_num = len(self.exam_data)

        self.show()
        self._init_shortcut_buttons()
        self._init_selection_layout()
        self.update_question(0)
        
        self.current_question = 0
        self.pushButton_3.clicked.connect(lambda:self.update_question(self.current_question-1))
        self.pushButton_4.clicked.connect(lambda:self.update_question(self.current_question+1))
        self.pushButton_6.clicked.connect(self.deleteLater)
    
    def _init_selection_layout(self):
        self.selection_layout = QHBoxLayout()
        _font = QFont()
        _font.setPointSize(10)

        self.single_buttons = QButtonGroup(self)
        for _i in range(4):
            _b = QRadioButton(self.right_frame)
            _b.setFont(_font)
            self.single_buttons.addButton(_b,_i)
            self.selection_layout.addWidget(_b)
            _b.hide()
                
        self.multi_buttons = QButtonGroup(self)
        self.multi_buttons.setExclusive(False)
        for _i in range(4):
            _b = QCheckBox(self.right_frame)
            _b.setFont(_font)
            self.multi_buttons.addButton(_b,_i)
            self.selection_layout.addWidget(_b)
            _b.hide()

        self.gridLayout.addLayout(self.selection_layout,3,0,1,4)
        
    def _init_shortcut_buttons(self):
        
        single_frame = QFrame(self.left_frame)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        single_frame.setSizePolicy(sizePolicy)
        grid_layout = QGridLayout(single_frame)
        
        self.shortcut_buttons = QButtonGroup(self)
        for _i in range(len(self.single_questions)):
            _b = QPushButton(single_frame)
            _b.setFixedSize(20,20)
            if self.correct_answers[self.questions[_i]] != self.user_answers[_i]:
                _b.setStyleSheet("color: red;")
            _b.setText(str(_i+1))
            grid_layout.addWidget(_b,_i//4,_i%4,1,1)
            
            _b.clicked.connect(partial(self.update_question,_i))
            self.shortcut_buttons.addButton(_b,_i)

        self.verticalLayout.insertWidget(self.verticalLayout.indexOf(self.verticalSpacer),QLabel(u"单选题",self.left_frame))
        self.verticalLayout.insertWidget(self.verticalLayout.indexOf(self.verticalSpacer),single_frame)


        multi_frame = QFrame(self.left_frame)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        multi_frame.setSizePolicy(sizePolicy)
        grid_layout = QGridLayout(multi_frame)
        
        for _i in range(len(self.multi_questions)):
            _i += len(self.single_questions)
            _b = QPushButton(multi_frame)
            _b.setFixedSize(20,20)
            if self.correct_answers[self.questions[_i]] != self.user_answers[_i]:
                _b.setStyleSheet("color: red;")
            _b.setText(str(_i+1))
            grid_layout.addWidget(_b,_i//4,_i%4,1,1)
            
            _b.clicked.connect(partial(self.update_question,_i))
            self.shortcut_buttons.addButton(_b,_i)


        self.verticalLayout.insertWidget(self.verticalLayout.indexOf(self.verticalSpacer),QLabel(u"多选题",self.left_frame))
        self.verticalLayout.insertWidget(self.verticalLayout.indexOf(self.verticalSpacer),multi_frame)



    def update_question(self,index):
        self.current_question = index
        if self.current_question == 0:
            self.pushButton_3.setDisabled(True)
            self.pushButton_4.setEnabled(True)
        elif self.current_question == self.question_num-1:
            self.pushButton_4.setDisabled(True)
            self.pushButton_3.setEnabled(True)
        else:
            self.pushButton_3.setEnabled(True)
            self.pushButton_4.setEnabled(True)
        

        data = self.exam_data[index]
        question_id = data["question_id"]
        
        _img = QPixmap()
        _img.loadFromData(data['question_text'])
        # _s = _img.size()
        if _img.height() < _img.width():
            _img = _img.scaledToWidth(self.label_6.width())
        else:
            _img = _img.scaledToHeight(self.label_6.height())
        self.label_6.setPixmap(_img)
        
        
        if data['question_type'] == "single":
            options = data['question_option'].split("#")
            for _i,_o in enumerate(options):
                self.single_buttons.button(_i).setText(selection_text[_i]+". "+_o)
                self.single_buttons.button(_i).show()
                self.single_buttons.setExclusive(False)
                self.single_buttons.button(_i).setChecked(False)
                self.single_buttons.setExclusive(True)

            if question_id in self.user_answers:
                self.single_buttons.button(selection_text.index(self.user_answers[question_id])).setChecked(True)
            
        elif data['question_type'] == "multi":
            options = data['question_option'].split("#")
            for _i,_o in enumerate(options):
                self.multi_buttons.button(_i).setText(selection_text[_i]+". "+_o)
                self.multi_buttons.button(_i).show()
                self.multi_buttons.button(_i).setChecked(False)
                
            if question_id in self.user_answers:
                for _c in self.user_answers[question_id]:
                    self.multi_buttons.button(selection_text.index(_c)).setChecked(True)
        
        
        user_answer = "无" if self.user_answers[index] == "0" else self.user_answers[index]
        self.label_3.setText(user_answer)
        self.label_4.setText(self.correct_answers[question_id])

        _string = f"题目：{index+1:>2}/{self.question_num:>2}"
        self.label_5.setText(_string)

class MainWindow(QMainWindow,Ui_MainWindow):
    assistant_signal = Signal(str)
    def __init__(self,parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.frame_4.hide()
        self.enter_frame.hide()
        self.current_page = 'ai'

        self.sum = 0
        self.widgetlist = []                                        #记录气泡
        self.icon = QtGui.QPixmap("user.png")                          # 头像
        #设置聊天窗口样式 隐藏滚动条
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        
        # 信号与槽
        self.pushButton.clicked.connect(self.create_user_widget)         #创建气泡
        self.plainTextEdit.undoAvailable.connect(self.Event)        #监听输入框状态
        scrollbar = self.scrollArea.verticalScrollBar()
        scrollbar.rangeChanged.connect(self.adjustScrollToMaxValue) #监听窗口滚动条范围

        self.pushButton_2.clicked.connect(self.click_assist)
        self.pushButton_4.clicked.connect(self.click_check)
        self.pushButton_3.clicked.connect(self.click_exam)
        self.pushButton_5.clicked.connect(self.deleteLater)
        self.pushButton_7.clicked.connect(self.start_exam)


        self.setup_qianfan()
        
        self.assistant_signal.connect(self.create_assist_widget)
        
    
    
    def setup_table(self):
        self.model = QStandardItemModel(1,3)
        self.model.setHorizontalHeaderLabels(("姓名","时间","章节","成绩",""))
        self.tableView.setModel(self.model)
        
        SQL = "select exam_id,exam_time,exam_chapter,score from exam_result where student_id=%s"
        result = excute_SQL(SQL,self.student_id)

        if result is None:
            self.model.setItem(0,0,QStandardItem("暂无成绩"))
        else:
            for _i,_r in enumerate(result):
                self.model.setItem(_i,0,QStandardItem(self.student_name))
                self.model.setItem(_i,1,QStandardItem(str(_r["exam_time"])))
                self.model.setItem(_i,2,QStandardItem(str(_r["exam_chapter"]) if _r["exam_chapter"] != 0 else "综合"))
                self.model.setItem(_i,3,QStandardItem(str(_r["score"])))
                _button = QPushButton("查看")
                _button.clicked.connect(partial(self.open_check,_r["exam_id"]))
                self.tableView.setIndexWidget(self.model.index(_i,4),_button)

        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
    
    def open_check(self,exam_id):
        check = CheckWindow(self,exam_id)
        check.show()
        pass
    
        
    def set_name(self, name,stu_id):
        self.student_name = name
        self.student_id = stu_id
        

    def setup_qianfan(self):
        qianfan.AccessKey("YourAccessKey")
        qianfan.SecretKey("YourSecretKey")

        self.chat_comp = qianfan.ChatCompletion()
        self.history_message=[]
        self.qianfan_model = "model"

    def click_check(self):
        self.enter_frame.hide()
        self.frame_3.hide()
        self.frame_4.show()
        self.current_page = 'check'
        self.setup_table()

    def click_assist(self):
        self.enter_frame.hide()
        self.frame_4.hide()
        self.frame_3.show()
        self.current_page = 'ai'

    def click_exam(self):
        self.enter_frame.show()
        self.frame_3.hide()
        self.frame_4.hide()
        self.current_page = 'exam'
        
    def start_exam(self):
        
        if self.comboBox.currentText() == "综合":
            chapter = 0
        else:
            chapter = self.comboBox.currentIndex()+1
        
        exam = ExamWindow(self,chapter)
        exam.show()
        self.hide()

    # 回车绑定发送
    def Event(self):
        if self.current_page == 'ai' and not self.plainTextEdit.isEnabled():  #这里通过文本框的是否可输入
            self.plainTextEdit.setEnabled(True)
            self.pushButton.click()
            self.plainTextEdit.setFocus()

    def send_message(self,message):
        self.history_message.append({
            "role": "user",
            "content": message
        })
        
        resp = self.chat_comp.do(model=self.qianfan_model,messages=self.history_message)
        
        assistant_message = {
            "role":"assistant",
            "content":resp["body"]["result"]
        }
        self.history_message.append(assistant_message)
        
        self.assistant_signal.emit(assistant_message["content"])
        
    #创建气泡
    def create_user_widget(self):
        self.sum+=1
        self.text=self.plainTextEdit.toPlainText()
        self.plainTextEdit.setPlainText("")
        Set_question.set_return(self, self.icon,self.text,QtCore.Qt.RightToLeft)    # 调用new_widget.py中方法生成左气泡
        QApplication.processEvents()                                # 等待并处理主循环事件队列

        self._t = threading.Thread(target=self.send_message,args=[self.text])
        self._t.start()
        
        self.set_widget()


    def create_assist_widget(self,text):
        self.sum+=1
        self.text = text
        Set_question.set_return(self, self.icon,self.text,QtCore.Qt.LeftToRight)   # 调用new_widget.py中方法生成右气泡
        QApplication.processEvents()                                # 等待并处理主循环事件队列
        self.set_widget()


    # 修改气泡长宽
    def set_widget(self):
        font = QFont()
        font.setPointSize(16)
        fm = QFontMetrics(font)
        text_width = 25*len(self.text)+115    #根据字体大小生成适合的气泡宽度
        if self.sum != 0:
            if text_width>632:                  #宽度上限
                text_width=int(self.textBrowser.document().size().width())+100  #固定宽度
            self.widget.setMinimumSize(text_width,int(self.textBrowser.document().size().height())+ 40) #规定气泡大小
            self.widget.setMaximumSize(text_width,int(self.textBrowser.document().size().height())+ 40) #规定气泡大小
            self.scrollArea.verticalScrollBar().setValue(10)


    # 窗口滚动到最底部
    def adjustScrollToMaxValue(self):
        scrollbar = self.scrollArea.verticalScrollBar()
        scrollbar.setValue(scrollbar.maximum())



if __name__ == "__main__":
    app = QApplication()

    win = MainWindow()
    win.hide()
    
    login = LoginWindow(win)

    sys.exit(app.exec())
