import sys

from PyQt6.QtWidgets import QApplication, QMainWindow

from PythonProject.Chapter5.ex73.ui.MainWindowEx import MainWindowEx

app=QApplication(sys.argv)
myui=MainWindowEx()
myui.setupUi(QMainWindow())
myui.show_window()
app.exec()