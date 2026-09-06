from PySide6 import *
from PySide6 import QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv) #инициализируем приложение
window = QtWidgets.QWidget() # создаём окно
window.setWindowTitle("Вход") # заголовок окна
window.resize(900, 500) #размер


window.show() # отображение океа
sys.exit(app.exec_()) # чтобы окно не закрывалось