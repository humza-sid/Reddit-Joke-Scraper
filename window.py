import sys
import joke as j
import textwrap
from PyQt5 import QtWidgets

jg = j.Joke_Gen('jokes')
jg.get_jokes()

class Window(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.b = QtWidgets.QPushButton('Get a Joke')
        self.l = QtWidgets.QLabel('')

        h_box = QtWidgets.QHBoxLayout()
        h_box.addWidget(self.l)

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.b)
        v_box.addLayout(h_box)

        self.setGeometry(400, 200, 600, 500)
        self.setLayout(v_box)
        self.setWindowTitle('Joke Generator')
        self.show()
        self.b.clicked.connect(self.btn_click)
        self.l.setWordWrap(True)

    def btn_click(self):
        title, old_text = jg.get_joke()
        self.l.setText(title
        + "\n---------------------------------------------" + 
        "-------------------------------------------------"
         + "\n\n" + old_text)


app = QtWidgets.QApplication(sys.argv)
a_window = Window()
app.exec_()

