import typing
import PyQt5
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QWidget
import sys

from main import main
from student import student
from study import study, Mentor_Mentee, Study_Group

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("My Application")
        self.move(300,300)
        self.resize(400,400)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())