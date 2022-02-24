import sys
import googletrans
from PyQt5 import uic
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *

form_class = uic.loadUiType('ui/calculator.ui')[0]  # ui 불러오기

class CalculatorApp(QMainWindow, form_class):
    def __init__(self):  # 초기화자
        super().__init__()
        self.setupUi(self)  # 만들어 놓은 test.ui 연결
        self.setWindowTitle('계산기')  # 윈도우 제목 설정
        self.setWindowIcon(QIcon('img/google_logo.png'))  # 윈도우 아이콘 설정
        self.statusBar().showMessage('Google Trans Applicatioin Ver 1.0')  # 윈도우 상태표시줄 입력
        self.result_button.clicked.connect(self.trans_Button_clicked)



    def result_button_clicked(self):





cal = ''

num1 = input('첫번째클릭한숫자:')
cal = cal + num1
print(cal)
oper1 = input('사칙연산자:')
cal = cal + oper1
print(cal)
num2 = input('두번째클릭한숫자:')
cal = cal + num2

print(cal)

result = eval(cal)
print(f"{cal}={result}")


app = QApplication(sys.argv)
window = CalculatorApp()
window.show()
app.exec_()