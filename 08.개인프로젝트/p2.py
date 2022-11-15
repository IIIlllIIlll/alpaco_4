from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys
import requests
import json
import openpyxl

UI_PATH=r'C:\Users\kjk42\OneDrive\문서\Python Scripts\alpa_4\08.개인프로젝트\naver_re.ui'

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
        sub_keys = list('ㄱㄴㄷㄹㅁㅂㅅㅇㅈㅊㅋㅌㅍㅎ')
        a = 1
        self.save=[]
        self.state.setText(f'{self.key_word}연관검색어 찾는중')
        QApplication.processEvents()
        header = {
            'User-Agent' : 'Mozila/5.0',
            'referer': 'https://www.naver.com/'
        }
        for sub_key in sub_keys:
            key = self.key_word + ' '+ sub_key
            response = requests.get(f'https://ac.search.naver.com/nx/ac?q={key}&con=0&frm=nv&ans=2&r_format=json&r_enc=UTF-8&r_unicode=0&t_koreng=1&run=2&rev=4&q_enc=UTF-8&st=100')
            data = json.loads(response.text)
            results = data['items'][0]
            
            for result in results:
                res = result[0]
                self.textBrowser.append(f'{a}{res}')
                QApplication.processEvents()
                self.save.append([a,res])
                a+=1
        self.state.setText('연관검색어 추출이 완료되었습니다.')
                

    def reset_(self):
        self.keyword.setText("")
        self.textBrowser.setText("")
        self.state.setText('상태메시지')

    def save_(self):
        wb = openpyxl.Workbook()
        ws = wb.active #활성화된 시트 선택
        ws.title = self.key_word #시트이름 변경
        ws.append(['검색어연관키워드 추출 결과'])
        ws.append(['순번','연관키워드'])    
        for i in self.save:
            ws.append(i)
        wb.save(f'{self.key_word}.xlsx')

        self.state.setText('저장완료')

    def close_(self):
        sys.exit()



QApplication.setStyle('fusion')
app = QApplication(sys.argv)
main_dialog = MainDialog()
main_dialog.show()
sys.exit(app.exec_())