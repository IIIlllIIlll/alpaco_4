from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys
import requests
from bs4 import BeautifulSoup
import openpyxl

UI_PATH=r'C:\Users\kjk42\OneDrive\문서\Python Scripts\alpa_4\07.GUI\naver.ui'

class MainDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self,None)
        uic.loadUi(UI_PATH,self)

        self.start_btn.clicked.connect(self.start_)
        self.reset_btn.clicked.connect(self.reset_)
        self.save_btn.clicked.connect(self.save_)
        self.close_btn.clicked.connect(self.close_)

    def start_(self):
        self.key_word = self.keyword.text()
        pages = int(self.page.text())
        a = 0
        self.save=[]
        for page in range(1,pages+1):
            self.textBrowser.append(f'{page}페이지 크롤링중')
            QApplication.processEvents()

            response = requests.get(f'https://kin.naver.com/search/list.naver?query={self.key_word}&page={page}')
            html = response.text
            soup = BeautifulSoup(html, 'html.parser')
            li = soup.select('.basic1 > li')
            
            for j in li:    
                anchor = j.select_one('._searchListTitleAnchor')
                title = anchor.text
                url = anchor.attrs['href']
                date = j.select_one('dt+dd').text
                con = j.select_one('dt+dd+dd').text
                a+=1
                self.textBrowser.append(f'{a} : {title}\n{url}\n{date}\n{con}')
                QApplication.processEvents()
                self.save.append([a,title,url,date,con])
                

    def reset_(self):
        self.keyword.setText("")
        self.page.setText("")
        self.textBrowser.setText("")

    def save_(self):
        wb = openpyxl.Workbook()
        ws = wb.active #활성화된 시트 선택
        ws.title = self.key_word #시트이름 변경
        ws.append(['순번','제목','링크','날짜','내용'])
        for i in self.save:
            ws.append(i)
        wb.save(f'{self.key_word}.xlsx')

        self.textBrowser.append('저장완료')

    def close_(self):
        sys.exit()



QApplication.setStyle('fusion')
app = QApplication(sys.argv)
main_dialog = MainDialog()
main_dialog.show()
sys.exit(app.exec_())



