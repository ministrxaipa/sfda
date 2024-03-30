from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import*
class TestWin (QWidget):
    def __init__(self):
        super().__init__()
        self.initUT()
        self.connects()
        self.set_appear()
        self.show()
    def initUT(self):
        self.btn_next=QPushButton('txt_next',self)
        self.hello_text=QLabel('Введите Ф.И.О.')
        self.instruction=QLabel('Полных лет')
        self.deb=QLineEdit()
        self.vosrat=QLineEdit()
        self.info=QLabel('ochen vasno')
        self.wsd=QPushButton('начать тест',self)
        self.hu=QLabel('другая важная информация')
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
        self.layout_line.addWidget(self.hu, alignment=Qt.AlignLeft)
        self.layout_line.addWidget(self.wer, alignment=Qt.AlignLeft)
        self.layout_line.addWidget(self.btn_next,alignment=Qt.AlignLeft)
        self.layout_line.addWidget(self.ger, alignment=Qt.AlignLeft)
        self.layout_line.addWidget(self.dwe, alignment=Qt.AlignLeft)
        self.setLayout(self.layout_line)
        self.layout_line.addWidget(self.btn_next,alignment=Qt.AlignLeft)
    def next_click(self):
        self.tw=TestWin()
        self.hide()
    def connects (self):
        self.btn_next.clicked.connect(self.next_click)
    def set_appear(self):
        win_x,win_y=200,100
        win_width,win_height=1000,600
        self.setWindowTitle('txt_title')
        self.resize(win_width,win_height)
        self.move (win_x,win_y)
app=QApplication([])
mw=TestWin()
app.exec()