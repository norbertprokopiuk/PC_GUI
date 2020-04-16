import sys
from PyQt5 import QtWidgets, uic, QtGui

from mainwindow import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.setupUi(self)
        self.setStyleSheet(open('style/mainWindow.css').read())

    def getControl(self):
        return self.connectionBar


def run():
    app=QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    control = window.getControl()
    
    app.exec_()

run()