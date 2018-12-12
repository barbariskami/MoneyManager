# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindowNew.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(250, -20, 20, 601))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.SumLabel = QtWidgets.QLabel(self.centralwidget)
        self.SumLabel.setGeometry(QtCore.QRect(20, -10, 161, 81))
        self.SumLabel.setObjectName("SumLabel")
        self.AddButton = QtWidgets.QPushButton(self.centralwidget)
        self.AddButton.setGeometry(QtCore.QRect(0, 70, 261, 51))
        self.AddButton.setObjectName("AddButton")
        self.MainListButton = QtWidgets.QPushButton(self.centralwidget)
        self.MainListButton.setGeometry(QtCore.QRect(0, 110, 261, 51))
        self.MainListButton.setObjectName("MainListButton")
        self.RegulalButton = QtWidgets.QPushButton(self.centralwidget)
        self.RegulalButton.setGeometry(QtCore.QRect(0, 150, 261, 51))
        self.RegulalButton.setObjectName("RegulalButton")
        self.CategoriesButton = QtWidgets.QPushButton(self.centralwidget)
        self.CategoriesButton.setGeometry(QtCore.QRect(0, 190, 261, 51))
        self.CategoriesButton.setObjectName("CategoriesButton")
        self.StatButton = QtWidgets.QPushButton(self.centralwidget)
        self.StatButton.setGeometry(QtCore.QRect(0, 230, 261, 51))
        self.StatButton.setObjectName("StatButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.SumLabel.setText(_translate("MainWindow",
                                         "<html><head/><body><p><span style=\" font-size:36pt;\">12 987 р</span></p></body></html>"))
        self.AddButton.setText(_translate("MainWindow", "Добавить операцию"))
        self.MainListButton.setText(_translate("MainWindow", "Финансовые операции"))
        self.RegulalButton.setText(_translate("MainWindow", "Регклярные платежи"))
        self.CategoriesButton.setText(_translate("MainWindow", "Категории"))
        self.StatButton.setText(_translate("MainWindow", "Статистика"))
