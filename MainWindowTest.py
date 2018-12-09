from MainWindowNew import Ui_MainWindow
from AddOperationWidget import Operation_Add_Widget
from OpenFile import open_file
import sys
import datetime
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QInputDialog
from PyQt5.QtCore import QDate


class Adding_Widget(Operation_Add_Widget, QWidget):
    def __init__(self):
        super().__init__()

        now = str(datetime.datetime.now()).split()[0].split('-')
        today_date = QDate()
        today_date.setDate(int(now[0]), int(now[1]), int(now[2]))
        #self.dateEdit.setDate(today_date)


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.wi = Adding_Widget()
        self.wi.move(100, 100)

        self.FileName, okButtonPressed = QInputDialog.getText(self, 'Open file', 'Укажите путь к файлу')
        if okButtonPressed:
            self.data = open_file(self.FileName)
        else:
            self.data = open_file(self.FileName)

        self.SumLabel.setText(str(self.data['Sum']))

        self.AddButton.clicked.connect(self.open_adding)

    def open_adding(self):
        self.Window = Adding_Widget()
        self.Window.move(560, 110)
        self.Window.setupUi()
        self.Window.show()
        self.Window.SaveButton.clicked.connect(self.operation_saving)

    def operation_saving(self):
        money = int(self.Window.SumEdit.text())
        operation = '-' if self.Window.MinusButton.isChecked() else '+'
        date = self.Window.dateEdit.date().getDate()
        name = self.Window.NameEdit.text()
        comment = self.Window.CommentEdit.text()
        categories = [i.strip().lower() for i in self.Window.CategoriesEdit.text().split(',')]
        self.data['Operations'].append(
            {'money': money, 'operation': operation, 'date': date, 'name': name, 'comment': comment,
             'categories': categories})
        sum = self.data['Sum']
        if operation == '-':
            sum -= money
        else:
            sum += money
        self.data['Sum'] = sum
        self.SumLabel.setText(str(self.data['Sum']))
        print(self.data)
        self.Window.close()


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
