from MainWindowNew import Ui_MainWindow
from AddOperationWidget import Operation_Add_Widget
from OpenFile import open_file
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QInputDialog


class Adding_Widget(Operation_Add_Widget, QWidget):
    def __init__(self):
        super().__init__()



class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.wi = Adding_Widget()
        self.wi.move(100, 100)

        self.FileName, okButtonPressed = QInputDialog.getText(self, 'Open file', 'Укажите путь к файлу')
        if okButtonPressed:
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
        money = self.Window.SumEdit.text()
        operation = '-' if self.Window.MinusButton.isChecked() else '+'
        date = self.Window.dateEdit.date()
        name = self.Window.NameEdit.text()
        comment = self.Window.CommentEdit.text()
        categories = [i.strip().lower() for i in self.Window.CategoriesEdit.text().split(',')]
        self.data['Operations'].append(
            {'money': money, 'operation': operation, 'date': date, 'name': name, 'comment': comment,
             'categories': categories})
        print(self.data)


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
