import sys
import re
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
        self.init_input.clicked.connect(self.init1_action)
        self.kor_reset.clicked.connect(self.init2_action)

    # 넣는 것 text, 빼는 건 subtext

    # def is_english_text(self, text): # 한글만 나오게 하는 방법
    #     pattern = r'^[0-9\s,.!?가-힣]*$'  # 숫자, 공백, 한글, 특정 특수 문자만 허용
    #     return re.match(pattern, text) is not None

    def trans_action(self):   #번역 실행 함수   ->slot 함수
        korText = self.kor_input.text()  #kor_input에 입력된 한글 텍스트 가져오기
        reg = re.compile(r'[a-zA-Z]')  #한글만 찾는 정규표현식    ^ <-제외 문자
        if korText == "":
            print("공백테스트")
            QMessageBox.warning(self, "입력오류!","한글 입력란에 번역할 문장을 넣어주세요.")
                                        #입력오류 제목, 나머지 내요

        elif reg.search(korText):  #한글인지 아닌지 여부확인(숫자 또는 영어로만 입력시 경고장 출력)
            print("한글아닌 문자 입력")
            QMessageBox.warning(self,"입력오류","입력한에 한글만 넣어주세요")

        else:
            print("정상변역결과 출력")
            trans = googletrans.Translator()  #구글트랜스 모듈의 객체 선언
            #print(googletrans.LANGUAGES  ㅂ번역 언어 약자 dest 찾기

            engText = trans.translate(korText,dest="en") #영어번역 결과를 가져옴
            japText = trans.translate(korText, dest="ja")
            chnText = trans.translate(korText, dest="zh-cn")

            self.en_input.append(engText.text) #번역된 영어 텍스트를 en_input에 출력
            self.ja_input.append(japText.text)
            self.chn_input.append(chnText.text)


    def init1_action(self):  #초기화 버튼 함수
        self.kor_input.clear()   #입력내용 지우기
        self.ja_input.clear()
        self.chn_input.clear()
        self.en_input.clear()



    def init2_action(self):
        self.kor_input.clear()


if __name__ == "__main__":
    app =  QApplication(sys.argv)
    googleWIN = GoogleTrans()
    googleWIN.show()
    sys.exit(app.exec_())