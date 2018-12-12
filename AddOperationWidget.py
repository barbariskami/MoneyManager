# -*- coding: utf-8 -*-

# self implementation generated from reading ui file 'AddOperationWidget.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Operation_Add_Widget(object):
    def setupUi(self, date):
        # self.setObjectName("self")
        # self.resize(540, 443)
        self.PlusButton = QtWidgets.QRadioButton(self)
        self.PlusButton.setGeometry(QtCore.QRect(210, 30, 100, 20))
        self.PlusButton.setObjectName("PlusButton")
        self.MinusButton = QtWidgets.QRadioButton(self)
        self.MinusButton.setGeometry(QtCore.QRect(210, 60, 100, 20))
        self.MinusButton.setObjectName("MinusButton")
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(40, 10, 60, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(290, 10, 60, 16))
        self.label_2.setObjectName("label_2")
        self.dateEdit = QtWidgets.QDateEdit(self)
        self.dateEdit.setGeometry(QtCore.QRect(290, 30, 110, 24))
        self.dateEdit.setObjectName("dateEdit")
        self.dateEdit.setDate(date)
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(30, 120, 91, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(30, 170, 141, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self)
        self.label_5.setGeometry(QtCore.QRect(30, 310, 201, 16))
        self.label_5.setObjectName("label_5")
        self.SaveButton = QtWidgets.QPushButton(self)
        self.SaveButton.setGeometry(QtCore.QRect(390, 380, 121, 41))
        self.SaveButton.setObjectName("SaveButton")
        self.SumEdit = QtWidgets.QLineEdit(self)
        self.SumEdit.setGeometry(QtCore.QRect(30, 30, 171, 71))
        self.SumEdit.setObjectName("SumEdit")
        self.NameEdit = QtWidgets.QLineEdit(self)
        self.NameEdit.setGeometry(QtCore.QRect(30, 140, 491, 21))
        self.NameEdit.setObjectName("NameEdit")
        self.CommentEdit = QtWidgets.QLineEdit(self)
        self.CommentEdit.setGeometry(QtCore.QRect(30, 190, 491, 111))
        self.CommentEdit.setObjectName("CommentEdit")
        self.CategoriesEdit = QtWidgets.QLineEdit(self)
        self.CategoriesEdit.setGeometry(QtCore.QRect(30, 330, 491, 21))
        self.CategoriesEdit.setObjectName("CategoriesEdit")

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "self"))
        self.PlusButton.setText(_translate("self", "+"))
        self.MinusButton.setText(_translate("self", "-"))
        self.label.setText(_translate("self", "Сумма"))
        self.label_2.setText(_translate("self", "Дата"))
        self.label_3.setText(_translate("self", "Название"))
        self.label_4.setText(_translate("self", "Комментарий"))
        self.label_5.setText(_translate("self", "Категории (через запятую)"))
        self.SaveButton.setText(_translate("self", "Сохранить"))
