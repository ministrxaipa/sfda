from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import*
from second_win import*
class TOOWin (QWidget):
    def __init__(self):
        super().__init__()
        self.initUT()
        self.connects()
        self.set_appear()
        self.show()
    def initUT(self):
        self.btn_next=QPushButton('txt_next',self)
        self.xp=QLabel('сюдааа')
        self.ovr=QLabel('тудааа')
        self.layout_line=QVBoxLayout()
        self.layout_line.addWidget(self.xp,alignment=Qt.AlignLeft)
        self.layout_line.addWidget(self.ovr,alignment=Qt.AlignLeft)
        self.layout_line.addWidget(self.btn_next,alignment=Qt.AlignLeft)
        self.setLayout(self.layout_line)
    def next_click(self):
        self.tw=TOOWin()
        self.hide()
    def connects (self):
        self.btn_next.clicked.connect(self.next_click)
    def set_appear(self):
        win_x,win_y=200,100
        win_width,win_height=1000,600
        self.setWindowTitle('txt_title')
        self.resize(win_width,win_height)
        self.move (win_x,win_y)
