# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(443, 543)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.plusBatton = QtWidgets.QPushButton(self.centralwidget)
        self.plusBatton.setGeometry(QtCore.QRect(290, 20, 111, 111))
        self.plusBatton.setStyleSheet("\n"
                                      "font: 64pt \"Symbol\";")
        self.plusBatton.setObjectName("plusBatton")

        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 150, 441, 21))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.goToList = QtWidgets.QPushButton(self.centralwidget)
        self.goToList.setGeometry(QtCore.QRect(20, 170, 61, 61))
        self.goToList.setStyleSheet("font: 40pt \".SF NS Text\";")
        self.goToList.setObjectName("goToList")

        self.goToBillsList = QtWidgets.QPushButton(self.centralwidget)
        self.goToBillsList.setGeometry(QtCore.QRect(20, 250, 61, 61))
        self.goToBillsList.setStyleSheet("font: 40pt \".SF NS Text\";")
        self.goToBillsList.setObjectName("goToBillsList")

        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(0, 230, 441, 21))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")

        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(0, 370, 441, 21))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")

        self.listLable = QtWidgets.QLabel(self.centralwidget)
        self.listLable.setGeometry(QtCore.QRect(90, 170, 361, 31))
        self.listLable.setObjectName("listLable")

        self.billsLable = QtWidgets.QLabel(self.centralwidget)
        self.billsLable.setGeometry(QtCore.QRect(90, 250, 291, 41))
        self.billsLable.setObjectName("billsLable")

        self.debtLable = QtWidgets.QLabel(self.centralwidget)
        self.debtLable.setGeometry(QtCore.QRect(20, 310, 221, 51))
        self.debtLable.setObjectName("debtLable")

        self.billsSum = QtWidgets.QLabel(self.centralwidget)
        self.billsSum.setGeometry(QtCore.QRect(260, 320, 111, 31))
        self.billsSum.setObjectName("billsSum")

        self.mainSum = QtWidgets.QLabel(self.centralwidget)
        self.mainSum.setGeometry(QtCore.QRect(30, 20, 241, 101))
        self.mainSum.setObjectName("mainSum")

        self.sumLable = QtWidgets.QLabel(self.centralwidget)
        self.sumLable.setGeometry(QtCore.QRect(10, 10, 81, 21))
        self.sumLable.setObjectName("sumLable")

        self.goToStat = QtWidgets.QPushButton(self.centralwidget)
        self.goToStat.setGeometry(QtCore.QRect(20, 390, 61, 61))
        self.goToStat.setStyleSheet("font: 40pt \".SF NS Text\";")
        self.goToStat.setObjectName("goToStat")

        self.statLable = QtWidgets.QLabel(self.centralwidget)
        self.statLable.setGeometry(QtCore.QRect(90, 390, 291, 41))
        self.statLable.setObjectName("statLable")

        MainWindow.setCentralWidget(self.centralwidget)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 443, 22))
        self.menubar.setObjectName("menubar")
        self.menuMoneyManager = QtWidgets.QMenu(self.menubar)
        self.menuMoneyManager.setObjectName("menuMoneyManager")
        MainWindow.setMenuBar(self.menubar)
        self.menubar.addAction(self.menuMoneyManager.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.plusBatton.setText(_translate("MainWindow", "+"))
        self.goToList.setText(_translate("MainWindow", ">"))
        self.goToBillsList.setText(_translate("MainWindow", ">"))
        self.listLable.setText(_translate("MainWindow",
                                          "<html><head/><body><p><span style=\" font-size:24pt;\">Список финансовых операций</span></p></body></html>"))
        self.billsLable.setText(_translate("MainWindow",
                                           "<html><head/><body><p><span style=\" font-size:24pt;\">Регулярные Счета</span></p></body></html>"))
        self.debtLable.setText(_translate("MainWindow",
                                          "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                          "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                          "p, li { white-space: pre-wrap; }\n"
                                          "</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                                          "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">У вас имеется долг по </span></p>\n"
                                          "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">оплате счетов на сумму</span></p></body></html>"))
        self.billsSum.setText(_translate("MainWindow",
                                         "<html><head/><body><p><span style=\" font-size:24pt;\">3 560р</span></p></body></html>"))
        self.mainSum.setText(_translate("MainWindow",
                                        "<html><head/><body><p align=\"center\"><span style=\" font-size:48pt;\">12 000р</span></p></body></html>"))
        self.sumLable.setText(_translate("MainWindow",
                                         "<html><head/><body><p><span style=\" font-size:18pt;\">Сумма</span></p></body></html>"))
        self.goToStat.setText(_translate("MainWindow", ">"))
        self.statLable.setText(_translate("MainWindow",
                                          "<html><head/><body><p><span style=\" font-size:24pt;\">Статистика</span></p></body></html>"))
        self.menuMoneyManager.setTitle(_translate("MainWindow", "MoneyManager"))

