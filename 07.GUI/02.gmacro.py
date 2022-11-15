from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys
import pyautogui as pyo
import time

UI_PATH=r'C:\Users\kjk42\OneDrive\문서\Python Scripts\alpa_4\07.GUI\gmacro.ui'

class MainDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self,None)
        uic.loadUi(UI_PATH,self)

        self.start_button.clicked.connect(self.start_move)

    def start_move(self):
        x = int(self.x_input.text())
        y= int(self.y_input.text())
        pyo.moveTo(x,y)

QApplication.setStyle('fusion')
app=QApplication(sys.argv)
main_dialog = MainDialog()
main_dialog.show()
sys.exit(app.exec_())