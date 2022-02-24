import sys
import googletrans
from PyQt5 import uic
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *

form_class = uic.loadUiType('ui/google_trans.ui')[0]  # ui 불러오기


class TransApp(QMainWindow, form_class):
    def __init__(self):  # 초기화자
        super().__init__()
        self.setupUi(self)  # 만들어 놓은 test.ui 연결
        self.setWindowTitle('한줄 번역기')  # 윈도우 제목 설정
        self.setWindowIcon(QIcon('img/google_logo.png'))  # 윈도우 아이콘 설정
        self.statusBar().showMessage('Google Trans Applicatioin Ver 1.0')  # 윈도우 상태표시줄 입력
        self.trans_Button.clicked.connect(self.trans_Button_clicked)
        self.clear_Button.clicked.connect(self.clear_button)

    def trans_Button_clicked(self):
        trans_txt = self.kor_input.text() # 입력된 문자열 가져오기
        trans = googletrans.Translator()
        ret1 = trans.translate(trans_txt, dest='en') # 영어 번역 결과
        ret2 = trans.translate(trans_txt, dest='ja') # 일본어 번역 결과
        ret3 = trans.translate(trans_txt, dest='zh-cn') # 중국어 번역 결과

        self.eng_result.setText(ret1.text)
        self.jp_result.setText(ret2.text)
        self.cha_result.setText(ret3.text)

    def clear_button(self):
        self.eng_result.clear()
        self.jp_result.clear()
        self.cha_result.clear()
        self.kor_input.clear()


app = QApplication(sys.argv)
window = TransApp()
window.show()
app.exec_()
