from PySide6 import *
from PySide6 import QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv) #инициализируем приложение
window = QtWidgets.QWidget() # создаём окно
window.setWindowTitle("Вход") # заголовок окна
window.resize(400, 300) #размер

btn = QtWidgets.QPushButton("Close")

window.show()