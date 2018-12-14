from MainWindowNew import Ui_MainWindow
from AddOperationWidget import Operation_Add_Widget
from OpenFile import open_file
import sys
import datetime
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QInputDialog
from PyQt5.QtCore import QDate
from Stat import Stat
from FuncForDatesSorting import datesSorting
from Saving import save_file
from OperationList import OperationList
from FuncForDatesSorting import datesSorting
from CategoriesList import CategoriesList

class CategoriesWindow(QWidget, CategoriesList):
    def __init__(self, data):
        super().__init__()
        self.setupUi(data)

class Adding_Widget(Operation_Add_Widget, QWidget):
    def __init__(self):
        super().__init__()

        now = str(datetime.datetime.now()).split()[0].split('-')
        today_date = QDate()
        today_date.setDate(int(now[0]), int(now[1]), int(now[2]))

        self.setupUi(today_date)


class Statyic_Window(QWidget, Stat):
    def __init__(self, sums, dates, income, expenditure):
        super().__init__()
        self.setupUi(sums, dates, income, expenditure)

class MainList(OperationList, QWidget):
    def __init__(self, data):
        super().__init__()
        self.setupUi(data)


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
            self.close()

        self.SumLabel.setText(str(self.data['Sum']))

        self.AddButton.clicked.connect(self.open_adding)
        self.StatButton.clicked.connect(self.open_stat)
        self.MainListButton.clicked.connect(self.open_main_list)
        self.CategoriesButton.clicked.connect(self.open_categories)

    def closeEvent(self, event):
        print(event)
        i, okBtnPressed = QInputDialog.getItem(
            self,
            "Выход",
            "Вы хотите выйти? Выберите параметр",
            ("Сохранить и выйти", "Не сохранять и выйти", "Не выходить"),
            1,
            False
        )
        if i == 'Сохранить и выйти':
            save_file(self.FileName, self.data)
            can_exit = True
        elif i == 'Не сохранять и выйти':
            can_exit = True
        else:
            can_exit = False
        if can_exit:
            event.accept()
        else:
            event.ignore()

    def open_adding(self):
        self.Window = Adding_Widget()
        self.Window.move(520, 100)
        self.Window.show()
        self.Window.SaveButton.clicked.connect(self.operation_saving)

    def open_stat(self):
        # При открытии, если операции были совершены, производится их сортировка,
        # Если же нет, на инициализацию подаются пустые списки
        if self.data['Operations']:
            sums = [0]
            dates = []
            operations = [(i['money'], i['operation'], i['date']) for i in self.data['Operations']]

            # Сортируется по возрастанию даты:
            operations = sorted(operations, key=datesSorting)
            dates.append(operations[0][2])

            # Создаются списки для инициализации(видов состояние счета и даты)
            # Вместе с этим считаются средние данные
            income = 0
            incomeDates = []
            expenditure = 0
            expenditureDates = []
            for i in operations:
                if i[1] == '+':
                    sums.append(sums[-1] + i[0])
                    income += i[0]

                    if (i[2][1], i[2][0]) not in incomeDates:
                        incomeDates.append((i[2][1], i[2][0]))
                else:
                    sums.append(sums[-1] - i[0])
                    expenditure += i[0]

                    if (i[2][2], i[2][1], i[2][0]) not in expenditureDates:
                        expenditureDates.append((i[2][2], i[2][1], i[2][0]))

                dates.append(i[2])

            if incomeDates:
                incomeAverage = f"{income / len(incomeDates):.{2}f}"
            else:
                incomeAverage = '0.00'
            if expenditureDates:
                expenditureAverage = f"{expenditure / len(expenditureDates):.{2}f}"
            else:
                expenditureAverage = '0.00'


        else:
            sums = []
            dates = []
            incomeAverage = '0.00'
            expenditureAverage = '0.00'

        self.Window = Statyic_Window(sums, dates, incomeAverage, expenditureAverage)
        self.Window.move(520, 100)
        self.Window.show()

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

        self.Window.close()

    def open_main_list(self):
        data = sorted(self.data['Operations'], key=lambda x: datesSorting(x, 'date'))
        print(data)
        self.Window = MainList(data)
        self.Window.move(520, 100)
        self.Window.show()

    def open_categories(self):
        data = sorted(self.data['Operations'], key=lambda x: datesSorting(x, 'date'))
        self.Window = CategoriesWindow(data)
        self.Window.move(520, 100)
        self.Window.show()


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
