# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'nothing.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from OperationInformation import InfoWindow
# from PyQt5.QtWidgets import QWidget, QApplication, QPushButton


class Info(QtWidgets.QWidget, InfoWindow):
    def __init__(self, operation):
        super().__init__()
        self.setupUi(operation)


class OperationList(object):
    def setupUi(self, data):
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(20, 10, 161, 41))
        self.label.setObjectName("label")
        self.scrollArea = QtWidgets.QScrollArea(self)
        self.scrollArea.setGeometry(QtCore.QRect(20, 50, 531, 381))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 529, 379))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        months = ['Январь ', 'Февраль ', 'Март ', 'Апрель ', 'Май ', 'Июнь ', 'Июль ', 'Август ', 'Сентябрь ',
                  'Октябрь ', 'Ноябрь ', 'Декабрь ']

        self.mainLayout = QtWidgets.QGridLayout()
        k = 0
        if data:
            last_date = data[0]['date'][:2]
            last_date[1] -= 1  # Для вывода первой строки о месяце
            for i in data:
                if last_date != i['date'][:2]:
                    # Добавление строки названия месяца
                    month = QtWidgets.QLabel()
                    last_date = i['date'][:2]
                    month.setText(months[last_date[1] - 1] + str(last_date[0]))
                    layout = QtWidgets.QHBoxLayout()
                    layout.addWidget(month)
                    layout.addWidget(QtWidgets.QLabel())
                    layout.addWidget(QtWidgets.QLabel())
                    self.mainLayout.addLayout(layout, k, 0)
                    k += 1
                newLayout = self.transform_data_into_layout(i)
                self.mainLayout.addLayout(newLayout, k, 0)
                k += 1

        self.WidgetForLayout = QtWidgets.QWidget()
        self.WidgetForLayout.setLayout(self.mainLayout)
        self.scrollArea.setWidget(self.WidgetForLayout)

        child = self.mainLayout.itemAt(0)
        k = 0
        while child:
            if child.itemAt(1) is not None and type(child.itemAt(1).widget()) == MyButton:
                item = child.itemAt(1).widget()
                item.clicked.connect(self.open_info)
            k += 1
            child = self.mainLayout.itemAt(k)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def transform_data_into_layout(self, data):
        # Создает из информации об операции layout со строкой для таблицы
        layout = QtWidgets.QHBoxLayout()

        sum = QtWidgets.QLabel()
        sum.setText(data['operation'] + str(data['money']))
        layout.addWidget(sum)

        name = MyButton(data)
        name.setText(data['name'])
        layout.addWidget(name)

        date = QtWidgets.QLabel()
        date.setText('.'.join([str(i) for i in data['date']]))
        layout.addWidget(date)

        return layout

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form",
                                      "<html><head/><body><p><span style=\" font-size:18pt;\">Список операций</span></p></body></html>"))

    def open_info(self):
        data = self.sender().info
        self.Window1 = Info(data)
        print(data)
        self.Window1.move(520, 100)
        self.Window1.show()


class MyButton(QtWidgets.QPushButton):
    def __init__(self, data):
        super().__init__()
        self.info = data
