# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'OperationList.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class OperationList(object):
    def setupUi(self, data):
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(20, 10, 271, 21))
        self.label.setObjectName("label")
        if not data:
            print('oooo')
            self.EmptyLabel = QtWidgets.QLabel(self)
            self.EmptyLabel.setGeometry(QtCore.QRect(20, 50, 201, 21))
            self.EmptyLabel.setObjectName("EmptyLabel")
            self.EmptyLabel.setText('Список Пуст')
        else:
            self.MainScrollArea = QtWidgets.QScrollArea(self)
            self.MainScrollArea.setGeometry(QtCore.QRect(20, 40, 561, 431))
            self.MainScrollArea.setWidgetResizable(True)
            self.MainScrollArea.setObjectName("MainScrollArea")
            self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
            self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 559, 429))
            self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
            self.MonthWidget = QtWidgets.QWidget(self.scrollAreaWidgetContents_2)
            self.MonthWidget.setGeometry(QtCore.QRect(0, 10, 561, 111))
            self.MonthWidget.setObjectName("MonthWidget")
            self.MonthName = QtWidgets.QLabel(self.MonthWidget)
            self.MonthName.setGeometry(QtCore.QRect(0, 0, 561, 21))
            self.MonthName.setObjectName("MonthName")
            self.MonthScrollArea = QtWidgets.QScrollArea(self.MonthWidget)
            self.MonthScrollArea.setGeometry(QtCore.QRect(0, 20, 561, 91))
            self.MonthScrollArea.setWidgetResizable(True)
            self.MonthScrollArea.setObjectName("MonthScrollArea")
            self.scrollAreaWidget = QtWidgets.QWidget()
            self.scrollAreaWidget.setGeometry(QtCore.QRect(0, 0, 559, 89))
            self.scrollAreaWidget.setObjectName("scrollAreaWidget")
            self.OperationLable = QtWidgets.QWidget(self.scrollAreaWidget)
            self.OperationLable.setGeometry(QtCore.QRect(0, 0, 561, 31))
            self.OperationLable.setObjectName("OperationLable")
            self.sumLable = QtWidgets.QLabel(self.OperationLable)
            self.sumLable.setGeometry(QtCore.QRect(0, 0, 91, 21))
            self.sumLable.setObjectName("sumLable")
            self.line_2 = QtWidgets.QFrame(self.OperationLable)
            self.line_2.setGeometry(QtCore.QRect(90, 0, 20, 31))
            self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
            self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
            self.line_2.setObjectName("line_2")
            self.nameButton = QtWidgets.QPushButton(self.OperationLable)
            self.nameButton.setGeometry(QtCore.QRect(100, 0, 371, 32))
            self.nameButton.setObjectName("nameButton")
            self.dateLable = QtWidgets.QLabel(self.OperationLable)
            self.dateLable.setGeometry(QtCore.QRect(480, 0, 71, 21))
            self.dateLable.setObjectName("dateLable")
            self.line_3 = QtWidgets.QFrame(self.OperationLable)
            self.line_3.setGeometry(QtCore.QRect(470, 0, 16, 31))
            self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
            self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
            self.line_3.setObjectName("line_3")
            self.line = QtWidgets.QFrame(self.OperationLable)
            self.line.setGeometry(QtCore.QRect(-10, 20, 561, 16))
            self.line.setFrameShape(QtWidgets.QFrame.HLine)
            self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
            self.line.setObjectName("line")
            self.MonthScrollArea.setWidget(self.scrollAreaWidget)
            self.MainScrollArea.setWidget(self.scrollAreaWidgetContents_2)

        self.retranslateUi(self, data)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Form, data):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form",
                                      "<html><head/><body><p><span style=\" font-size:18pt;\">Список финансовых операций</span></p></body></html>"))
        if not data:
            print('jjjjj')
            self.EmptyLabel.setText(_translate("Form", "<html><head/><body><p><br/></p></body></html>"))
        else:
            print('hhhhh')
            self.MonthName.setText(_translate("Form", "Май"))
            self.sumLable.setText(_translate("Form", "<html><head/><body><p align=\"center\">500 р</p></body></html>"))
            self.nameButton.setText(_translate("Form", "PushButton"))
            self.dateLable.setText(
                _translate("Form", "<html><head/><body><p align=\"center\">01/12/18</p></body></html>"))
