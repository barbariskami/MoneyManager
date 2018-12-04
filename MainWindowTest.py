from Ui_MainWindow import Ui_MainWindow
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel

class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.surprise = QLabel(self)
        self.surprise.move(300, 300)
        self.plusBatton.clicked.connect(self.run)

    def run(self):
        self.surprise.setText('Surprise!')

app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
