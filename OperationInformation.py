# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'OperationInformation.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class InfoWindow(object):
    def setupUi(self, operation):
        self.SumLabel = QtWidgets.QLabel(self)
        self.SumLabel.setGeometry(QtCore.QRect(50, 30, 161, 91))
        self.SumLabel.setObjectName("SumLabel")
        self.DateLabel = QtWidgets.QLabel(self)
        self.DateLabel.setGeometry(QtCore.QRect(290, 60, 101, 41))
        self.DateLabel.setObjectName("DateLabel")
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(10, 0, 241, 41))
        self.label_3.setObjectName("label_3")
        self.NameLabel = QtWidgets.QLabel(self)
        self.NameLabel.setGeometry(QtCore.QRect(10, 120, 321, 31))
        self.NameLabel.setObjectName("NameLabel")
        self.line = QtWidgets.QFrame(self)
        self.line.setGeometry(QtCore.QRect(0, 110, 471, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self)
        self.line_2.setGeometry(QtCore.QRect(-10, 30, 471, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self)
        self.line_3.setGeometry(QtCore.QRect(240, 40, 16, 81))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self)
        self.line_4.setGeometry(QtCore.QRect(0, 150, 431, 16))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(self)
        self.line_5.setGeometry(QtCore.QRect(0, 270, 441, 20))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.CommentLabel = QtWidgets.QLabel(self)
        self.CommentLabel.setGeometry(QtCore.QRect(10, 160, 411, 111))
        self.CommentLabel.setStyleSheet("font: 14pt \"Times\";\n"
                                        "font: 13pt \".SF NS Text\";")
        self.CommentLabel.setObjectName("CommentLabel")
        self.label_6 = QtWidgets.QLabel(self)
        self.label_6.setGeometry(QtCore.QRect(10, 290, 191, 16))
        self.label_6.setObjectName("label_6")
        self.scrollArea = QtWidgets.QScrollArea(self)
        self.scrollArea.setGeometry(QtCore.QRect(10, 310, 311, 161))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 309, 159))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.layout = QtWidgets.QVBoxLayout()
        for category in operation['categories']:
            label = QtWidgets.QLabel()
            label.setText(category)
            self.layout.addWidget(label)

        self.widgetForLayout = QtWidgets.QWidget()
        self.widgetForLayout.setLayout(self.layout)
        self.scrollArea.setWidget(self.widgetForLayout)

        self.SumLabel.setText(operation['operation'] + str(operation['money']))

        self.DateLabel.setText('.'.join([str(i) for i in operation['date']]))

        self.NameLabel.setText(operation['name'])

        comment = operation['comment'].split()
        new_comment = ''
        pos = 0
        for i in comment:
            if len(i) > 31:
                new_comment += '\n' + i + '\n'
            elif pos + len(i) > 31:
                new_comment += '\n' + i
            else:
                new_comment += i
        self.CommentLabel.setText(new_comment)



        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.SumLabel.setText(_translate("Form",
                                         "<html><head/><body><p><span style=\" font-size:36pt;\"> + 754 р</span></p></body></html>"))
        self.DateLabel.setText(_translate("Form",
                                          "<html><head/><body><p><span style=\" font-size:18pt;\">07/04/2018</span></p></body></html>"))
        self.label_3.setText(_translate("Form",
                                        "<html><head/><body><p><span style=\" font-size:18pt;\">Информация об операции</span></p></body></html>"))
        self.NameLabel.setText(_translate("Form",
                                          "<html><head/><body><p><span style=\" font-size:18pt;\">Продукты</span></p></body></html>"))
        self.CommentLabel.setText(_translate("Form", "<html><head/><body><p><br/></p></body></html>"))
        self.label_6.setText(_translate("Form",
                                        "<html><head/><body><p><span style=\" font-size:14pt;\">Категории</span></p></body></html>"))
