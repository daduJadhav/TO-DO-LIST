from PyQt5.QtWidgets import *
from PyQt5 import QtCore,QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

class Window(QMainWindow):
    def __init__(self):

        # Main Body 
        super().__init__()
        self.setWindowTitle("TO-DO-LIST")
        self.setGeometry(500,200,800,750)
        self.setStyleSheet("Background-color : whitesmoke ")    
        self.setFont(QFont("Poppin",14))          #styling can only be done one (1)self.setStyleSheet
        self.uiComponents()
        self.show()

    def uiComponents(self):
        self.flag = False

        # Brand Name 
        self.lable = QLabel(self)
        self.lable.setFont(QFont('',30))
        self.lable.setGeometry(10,10,800,100)
        self.lable.setText(str('Mackamlin...'))
        self.lable.setStyleSheet("color : red ")
        self.lable.setAlignment(Qt.AlignCenter)

        # Typing line 
        self.grabtext = QLineEdit(self)
        self.grabtext.setGeometry(10,115,520,50) 
        self.grabtext.setStyleSheet("")
        self.grabtext.setFont(QFont('Poppin',12))

        self.ADD_btn = QPushButton("Add",self,clicked = lambda:self.ADD())
        # self.ADD_btn.clicked(lambda : self.ADD())
        self.ADD_btn.setGeometry(540,115,250,50)
        self.ADD_btn.setStyleSheet("background-color : #A9FF33; border-radius: 10px;")
        self.ADD_btn.setFont(QFont('Poppin',13))

        self.del_btn = QPushButton("Delete",self, clicked = lambda: self.Del())
        # self.del_btn.pressed.connect(self.s_Del())
        self.del_btn.setGeometry(10,185,380,50)
        self.del_btn.setStyleSheet("background-color : red; border-radius: 10px;")
        self.del_btn.setFont(QFont('Poppin',13))

        self.clear_btn = QPushButton("Clear All",self,clicked = lambda : self.Clear())
        self.clear_btn.setGeometry(410,185,380,50)
        # self.clear_btn.pressed.connect(self.s_clear())
        self.clear_btn.setStyleSheet("background-color : red; border-radius: 10px;")
        self.clear_btn.setFont(QFont('Poppin',13))
        
        self.checkBox = QListWidget(self)
        self.checkBox.setGeometry(10,265,780,400)
        self.checkBox.setFont(QFont("Poppin",16))
        self.checkBox.setStyleSheet("background-color : #85929E; border-radius : 10px ; margin-left : 5px")

        self.check_btn = QPushButton("Save to file",self, clicked = lambda : self.save_item())
        # self.check_btn.pressed.connect(self.s_check())
        self.check_btn.setGeometry(10,680,780,50)
        self.check_btn.setStyleSheet("background-color : yellow ; border-radius: 10px;")
        self.check_btn.setFont(QFont('Poppin',13))


    def ADD(self):
        
        # grabing item 
        item = self.grabtext.text()

        # putting item 
        self.checkBox.addItem(item)

        # setting text value blank
        self.grabtext.setText("")

    def Del(self):
        clicked = self.checkBox.currentRow()

        self.checkBox.takeItem(clicked)

    
    def Clear(self):
        self.checkBox.clear()
    
    def save_item(self):
        file = []
        for index in range(self.checkBox.count()):
            file.append(self.checkBox.item(index))

        for files in file:
            f = open("Saved_data.txt",'a+')
            f.write(str(files.text())+"\n")
            f.close()

App  = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
