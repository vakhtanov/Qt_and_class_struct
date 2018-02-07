# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'in_out_form.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DialogWindow(object):
    def setupUi(self, DialogWindow):
        DialogWindow.setObjectName("DialogWindow")
        DialogWindow.resize(588, 397)
        self.buttonBoxOkCancel = QtWidgets.QDialogButtonBox(DialogWindow)
        self.buttonBoxOkCancel.setGeometry(QtCore.QRect(50, 350, 501, 32))
        self.buttonBoxOkCancel.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBoxOkCancel.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBoxOkCancel.setCenterButtons(True)
        self.buttonBoxOkCancel.setObjectName("buttonBoxOkCancel")
        self.pushButtonPushme = QtWidgets.QPushButton(DialogWindow)
        self.pushButtonPushme.setGeometry(QtCore.QRect(90, 140, 111, 23))
        self.pushButtonPushme.setCheckable(False)
        self.pushButtonPushme.setObjectName("pushButtonPushme")
        self.textEdit = QtWidgets.QTextEdit(DialogWindow)
        self.textEdit.setGeometry(QtCore.QRect(280, 80, 181, 191))
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(DialogWindow)
        QtCore.QMetaObject.connectSlotsByName(DialogWindow)

    def retranslateUi(self, DialogWindow):
        _translate = QtCore.QCoreApplication.translate
        DialogWindow.setWindowTitle(_translate("DialogWindow", "Форма для проверки работы кнопок"))
        self.pushButtonPushme.setText(_translate("DialogWindow", "Нажми меня"))

