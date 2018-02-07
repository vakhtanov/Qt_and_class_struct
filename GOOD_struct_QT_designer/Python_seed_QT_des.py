#!/usr/bin/python3
# coding=utf-8
import random
import string
from in_out_form import Ui_DialogWindow
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
class Qt_des_buttons(QMainWindow, Ui_DialogWindow):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.pushButtonPushme.clicked.connect(self.buttonClicked) #События по нажатию на кнопку
		
	def generate_pins(self, size=6, chars=string.digits): #Функция для генерации ключей
		return ''.join(random.choice(chars) for x in range(size))
		
	def buttonClicked(self): # функция которая вешается на кнопку
		self.textEdit.append(self.generate_pins(10))
if __name__ == "__main__":
	app = QApplication(sys.argv)
	form=Qt_des_buttons()
	form.show()
	app.exec()
