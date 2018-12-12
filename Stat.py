# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'stat.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Stat(object):
    def setupUi(self, sums, dates, income, expenditure):
        self.graphicsView = PlotWidget(self)
        self.graphicsView.setGeometry(QtCore.QRect(10, 70, 531, 201))
        self.graphicsView.setObjectName("graphicsView")
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(20, 10, 131, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 201, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(10, 280, 231, 31))
        self.label_3.setObjectName("label_3")
        self.SumPerDay = QtWidgets.QLabel(self)
        self.SumPerDay.setGeometry(QtCore.QRect(290, 270, 111, 41))
        self.SumPerDay.setObjectName("SumPerDay")
        self.label_5 = QtWidgets.QLabel(self)
        self.label_5.setGeometry(QtCore.QRect(10, 310, 251, 31))
        self.label_5.setObjectName("label_5")
        self.SumPerMonth = QtWidgets.QLabel(self)
        self.SumPerMonth.setGeometry(QtCore.QRect(290, 310, 141, 31))
        self.SumPerMonth.setObjectName("SumPerMonth")

        dates = [(i[0] % 1000) * 365 + i[1] * 31 + i[2] for i in dates]

        self.graphicsView.clear()
        self.graphicsView.plot(list(dates), list(sums), pen='r')

        self.SumPerDay.setText(expenditure)
        self.SumPerMonth.setText(income)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form",
                                      "<html><head/><body><p><span style=\" font-size:18pt;\">Статистика</span></p></body></html>"))
        self.label_2.setText(_translate("Form",
                                        "<html><head/><body><p><span style=\" font-size:14pt;\">График состояния кошелька</span></p></body></html>"))
        self.label_3.setText(_translate("Form",
                                        "<html><head/><body><p><span style=\" font-size:18pt;\">Средняя затрата за день:</span></p></body></html>"))
        self.label_5.setText(_translate("Form",
                                        "<html><head/><body><p><span style=\" font-size:18pt;\">Средний заработок в месяц:</span></p></body></html>"))


from pyqtgraph import PlotWidget
