from PythonProject.Chapter5.ex73.libs.mymodule import calculation
from PythonProject.Chapter5.ex73.ui.MainWindow import Ui_MainWindow


class MainWindowEx(Ui_MainWindow):

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.resultLineEdit.setMinimumSize(350, 40)
        self.MainWindow.setFixedSize(500, 350)
        self.setupSignalAndSlot()
    def show_window(self):
        self.MainWindow.show()

    def setupSignalAndSlot(self):
        self.pushButton.clicked.connect(self.calc)
    def calc(self):
        a=int(self.aLineEdit.text())
        b=int(self.bLineEdit.text())
        c=int(self.cLineEdit.text())
        result = calculation(a, b, c)
        self.resultLineEdit.setText(str(result))
