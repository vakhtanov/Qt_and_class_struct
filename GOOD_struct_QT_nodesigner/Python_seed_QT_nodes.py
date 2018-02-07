#!/usr/bin/python
# coding=UTF-8
import sys
from PyQt5.QtWidgets import (QWidget, QToolTip, QPushButton, QApplication)
from PyQt5.QtGui import QFont    
#класс наследуем от QApplication
class HelloApplication(QWidget):
    def __init__(self):
        """
            В конструкторе мы делаем всё, что необходимо для запуска нашего приложения, которое
            создаёт QApplication в __init__ методе, затем добваляет наши виджеты и, наконец,
            запускает exec_loop
        """
        super().__init__()
        self.addWidgets()
        #self.exec_loop()        
    def addWidgets(self):
        """ В этом методе мы добавляем виджеты и присоединяем обработчики сигналов.
            Обработчик сигнала для виджета так же называется "слотом"
        """
        self.hellobutton = QPushButton("Say 'Hello, World!'",None)
        self.hellobutton.clicked.connect(self.slotSayHello)
        #self.hellobutton.setMainWidget(self.hellobutton)
        self.hellobutton.show()
    def slotSayHello(self):
        """
            Это пример слота - метода, который вызывается, когда приходит сигнал.
        """
        print ("Hello, World!")
# Этот скрипт должен выполняться только отдельно, так что мы должны проверить это,
# но мы также должны иметь возможность подключать эту программу без запуска какого-либо кода
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ha=HelloApplication()
    sys.exit(app.exec_())