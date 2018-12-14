# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CategoriesList.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class CategoriesList(object):
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

        categories = {}
        for operation in data:
            for category in operation['categories']:
                if category != '':
                    if category in categories.keys():
                        categories[category].append(operation)
                    else:
                        categories[category] = [operation]

        self.mainLayout = QtWidgets.QGridLayout()
        k = 0
        print(categories)
        for category in categories.keys():
            print(category)
            name = QtWidgets.QLabel()
            name.setText(category)
            local_layout = QtWidgets.QHBoxLayout()
            local_layout.addWidget(name)
            local_layout.addWidget(QtWidgets.QLabel())
            local_layout.addWidget(QtWidgets.QLabel())
            self.mainLayout.addLayout(local_layout, k, 0)
            k += 1
            for operation in categories[category]:

                self.mainLayout.addLayout(self.transform_data_into_layout(operation), k, 0)
                k += 1

        self.widgetForLayout = QtWidgets.QWidget()
        self.widgetForLayout.setLayout(self.mainLayout)
        self.scrollArea.setWidget(self.widgetForLayout)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def transform_data_into_layout(self, data):
        # Создает из информации об операции layout со строкой для таблицы
        layout = QtWidgets.QHBoxLayout()

        sum = QtWidgets.QLabel()
        sum.setText(data['operation'] + str(data['money']))
        layout.addWidget(sum)

        name = QtWidgets.QPushButton()
        name.setText(data['name'])
        layout.addWidget(name)

        date = QtWidgets.QLabel()
        date.setText('.'.join([str(i) for i in data['date']]))
        layout.addWidget(date)

        return layout

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:18pt;\">Список категорий</span></p></body></html>"))

