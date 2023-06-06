from PyQt5.QtWidgets import *
import sys
from PyQt5.QtCore import Qt,QSize
from PyQt5.QtGui import QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Practice")
        lab = QLabel("hello")
        lab.setPixmap((QPixmap("login.png")))
        lab.setScaledContents(True)
        self.setCentralWidget(lab)
       
       
    
        

app = QApplication(sys.argv)
widget = MainWindow()
widget.show()


app.exec_()