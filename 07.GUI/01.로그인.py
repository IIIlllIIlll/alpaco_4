from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys

UI_PATH=r'C:\Users\kjk42\OneDrive\문서\Python Scripts\alpa_4\07.GUI\login.ui'

class MainDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self,None)
        uic.loadUi(UI_PATH,self)

        self.login_button.clicked.connect(self.login_start)

    def login_start(self):
        input_id = self.ID.text()
        input_pw = self.PW.text()
        print(f'ID:{input_id} PW:{input_pw}')



QApplication.setStyle('fusion')
app = QApplication(sys.argv)
main_dialog = MainDialog()
main_dialog.show()
sys.exit(app.exec_())