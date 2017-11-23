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
        self.next_joke = "Short"
        self.setup()

    def setup(self):
        self.pic = QLabel('', self)
        self.set_picture(self.pic)
        self.b = QPushButton('New Joke', self)
        self.b.move(300, 10)
        self.l = QLabel('', self)
        self.l.move(20, 50)
        self.l.setWordWrap(True)
        self.l.setGeometry(QRect(70, 50, 500, 500))
        self.setGeometry(400, 200, 800, 550)
        self.setWindowTitle('Joke Generator')
        self.cBox = QComboBox(self)
        self.cBox.move(420, 12)
        self.cBox.addItem("Short")
        self.cBox.addItem("Medium")
        self.cBox.addItem("Long")
        self.b.clicked.connect(self.new_click)
        self.cBox.activated[str].connect(self.onActivated)
        self.show()

    def set_picture(self, pic):
        pixmap = QPixmap('bg.png')
        pic.setPixmap(pixmap)

    def new_click(self):
        if (self.next_joke == "Short"):
            rand = random.randint(0, len(jg.short) - 1)
        elif (self.next_joke == "Medium"):
            rand = random.randint(0, len(jg.medium) - 1)
        elif (self.next_joke == "Long"):
            rand = random.randint(0, len(jg.long) - 1)

        title, old_text = jg.get_joke(rand, self.next_joke)
        self.l.setText(title + "\n\n" + old_text)

    def onActivated(self, text):
        self.next_joke = text

app = QApplication(sys.argv)
a_window = Window()
app.exec_()

