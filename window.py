import sys
import joke as j
import random
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QRect

jg = j.Joke_Gen('jokes')
class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.setup()

    def setup(self):
        self.pic = QLabel('', self)
        self.set_picture(self.pic)
        self.b = QPushButton('New Joke', self)
        self.b.move(10, 10)
        self.l = QLabel('', self)
        self.l.move(20, 50)
        self.l.setWordWrap(True)
        self.l.setGeometry(QRect(70, 80, 500, 400))
        self.setGeometry(400, 200, 800, 550)
        self.setWindowTitle('Joke Generator')
        self.cBox = QComboBox(self)
        self.cBox.move(130, 12)
        
        self.b.clicked.connect(self.new_click)
        self.show()
        # self.show()
        # radiobutton = QRadioButton("Brazil")
        # radiobutton.setChecked(True)
        # radiobutton.country = "Brazil"
        # radiobutton.toggled.connect(self.on_radio_button_toggled)
        # layout.addWidget(radiobutton, 0, 0)

        # radiobutton = QRadioButton("Argentina")
        # radiobutton.country = "Argentina"
        # radiobutton.toggled.connect(self.on_radio_button_toggled)
        # layout.addWidget(radiobutton, 0, 1)

        # radiobutton = QRadioButton("Ecuador")
        # radiobutton.country = "Ecuador"
        # radiobutton.toggled.connect(self.on_radio_button_toggled)
        # layout.addWidget(radiobutton, 0, 2)

    # def on_radio_button_toggled(self):
    #     radiobutton = self.sender()

    #     if radiobutton.isChecked():
    #         print("Selected country is %s" % (radiobutton.country))

    #def init_ui(self):
        # h_box = q.QHBoxLayout()
        # h_box.addWidget(self.l)
        # h_box.addWidget(self.pic)

        # v_box = q.QVBoxLayout()
        # v_box.addWidget(self.b1)
        # v_box.addLayout(h_box)

        
        # self.setLayout(v_box)
        
        #self.set_picture()
        
    def set_picture(self, pic):
        pixmap = QPixmap('dadjoke.png')
        pic.setPixmap(pixmap)

    def new_click(self):
        rand = random.randint(0, len(jg.jokes) - 1)
        title, old_text = jg.get_all(rand)
        self.l.setText(title
        # + "\n---------------------------------------------" + 
        # "-------------------------------------------------"
        + "\n\n" + old_text)

app = QApplication(sys.argv)
a_window = Window()
app.exec_()

