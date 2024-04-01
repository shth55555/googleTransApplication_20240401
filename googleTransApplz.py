import sys

import googletrans

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic

form_class = uic.loadUiType("uiDirectory/googleTrans.ui")[0]
#디자인한 외부 ui파일 불러와서 저장

class GoogleTrans(QMainWindow,form_class):
    def __init__(self):
        super().__init__()  #부모 클래스 생성자 호출
        self.setupUi(self)  #불러온 ui파일을 연결


        self.setWindowTitle("구글 한줄 번역기")  #윈도우 타이틀
        self.setWindowIcon(QIcon("icon/icon.png")) #윈도우 아이콘
        self.statusBar().showMessage("Google Trans App v1.0 Made by abc") #윈도우 상태표시줄

        self.trans_btn.clicked.connect(self.trans_action)  #시그널...괄호 빼고





    def trans_action(self):   #번역 실행 함수   ->slot 함수
        korText = self.kor_input.text()  #kor_input에 입력된 한글 텍스트 가져오기

        trans = googletrans.Translator()  #구글트랜스 모듈의 객체 선언
        #print(googletrans.LANGUAGES  ㅂ번역 언어 약자 dest 찾기

        engText = trans.translate(korText,dest="en") #영어번역 결과를 가져옴
        japText = trans.translate(korText, dest="ja")
        chnText = trans.translate(korText, dest="zh-cn")

        self.en_input.append(engText.text) #번역된 영어 텍스트를 en_input에 출력
        self.ja_input.append(japText.text)
        self.chn_input.append(chnText.text)

if __name__ == "__main__":
    app =  QApplication(sys.argv)
    googleWIN = GoogleTrans()
    googleWIN.show()
    sys.exit(app.exec_())