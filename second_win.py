from PyQt5.QtCore import Qt, QTimer,QTime,QLocale
from PyQt5.QtWidgets import*
from PyQt5.QtGui import *
from final_win import*
from instr import*
class TestWin (QWidget):
    def __init__(self):
        super().__init__()
        self.initUT()
        self.connects()
        self.set_appear()
        self.show()
    def initUT(self):
        self.btn_next=QPushButton(txt_next,self)
        self.hello_text=QLabel('Введите Ф.И.О.')
        self.instruction=QLabel('Полных лет')
        self.deb=QLineEdit()
        self.vosrat=QLineEdit()
        self.info=QLabel(txt_test1)
        self.wsd=QPushButton('начать тест',self)
        self.rap=QLineEdit()
        self.hu=QLabel(txt_test2)
        self.vs=QLineEdit()
        self.rep=QLabel('дорогие друзья')
        self.wer=QPushButton('начать финальный тест',self)
        self.ger=QLineEdit()
        self.dwe=QLineEdit()
        self.layout_line=QVBoxLayout()
        self.layout_line.addWidget(self.hello_text,alignment=Qt.AlignLeft)
        self.layout_line.addWidget(self.deb,alignment=Qt.AlignLeft)
        self.layout_line.addWidget(self.instruction,alignment=Qt.AlignLeft)
        self.layout_line.addWidget(self.vosrat,alignment=Qt.AlignLeft)
        self.layout_line.addWidget(self.info,alignment=Qt.AlignLeft)
        self.layout_line.addWidget(self.wsd, alignment=Qt.AlignLeft)
        self.layout_line.addWidget(self.rap,alignment=Qt.AlignLeft )
        self.layout_line.addWidget(self.hu, alignment=Qt.AlignLeft)
        self.layout_line.addWidget(self.vs,alignment=Qt.AlignLeft)
        self.layout_line.addWidget(self.rep,alignment=Qt.AlignLeft)
        self.layout_line.addWidget(self.wer, alignment=Qt.AlignLeft)
        self.layout_line.addWidget(self.btn_next,alignment=Qt.AlignLeft)
        self.layout_line.addWidget(self.ger, alignment=Qt.AlignLeft)
        self.layout_line.addWidget(self.dwe, alignment=Qt.AlignLeft)
        self.text_timer=QLabel(txt_timer)
        self.text_timer.setFont(QFont('Times',36,QFont.Bold))
        self.layout_line.addWidget(self.text_timer,alignment=Qt.AlignRight)
        self.setLayout(self.layout_line)
    def next_click(self):
        self.tw=TOOWin()
        self.hide()
    def timer_test1(self):
        global time 
        time=QTime(0,0,15)
        self.timer=QTimer()
        self.timer.timeout.connect(self.timer1Event)
        self.timer.start(1000)
    def timer1Event(self):
        global time
        time=time.addSecs(-1)
        self.text_timer.setText(time.toString("hh:mm:ss"))
        self.text_timer.setFont(QFont('Times',36,QFont.Bold))
        self.text_timer.setStyleSheet('color:rgb(0,0,0)')
        if time.toString('hh:mm:ss')=='00:00:00':
            self.timer.stop()
    def timer_test2(self):
        global time 
        time=QTime(0,0,45)
        self.timer=QTimer()
        self.timer.timeout.connect(self.timer1Event)
        self.timer.start(1000)
    def timer2Event(self):
        global time
        time=time.addSecs(-1)
        self.text_timer.setText(time.toString("hh:mm:ss"))
        self.text_timer.setFont(QFont('Times',36,QFont.Bold))
        self.text_timer.setStyleSheet('color:rgb(0,0,0)')
        if time.toString('hh:mm:ss')=='00:00:00':
            self.timer.stop()
    def connects (self):
        self.btn_next.clicked.connect(self.next_click)
        self.wsd.clicked.connect(self.timer_test1)
        self.wer.clicked.connect(self.timer_test2)
    def set_appear(self):
        win_x,win_y=200,100
        win_width,win_height=1000,600
        self.setWindowTitle('txt_title')
        self.resize(win_width,win_height)
        self.move (win_x,win_y)
