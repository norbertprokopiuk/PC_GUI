import sys, time
from PyQt5 import QtWidgets, uic, QtGui, QtCore
from mainwindow import Ui_MainWindow
from connectionHandler import *




class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.setupUi(self)
        self.setStyleSheet(open('style/mainWindow.css').read())
        self.setupThread()
        self.connectButtons()

    def connectButtons(self):
        self.connectionBar.b_connect.pressed.connect(self.manageConnection)
      
    def setupThread(self):
        self.telemetryThread=QtCore.QThread() 
        self.handler = connectionHandler()
        self.handler.moveToThread(self.telemetryThread)
        self.telemetryThread.started.connect(self.handler.receiveData)
        self.handler.dataReceived.connect(self.updateWidgets)
        

    def manageConnection(self):
        if self.telemetryThread.isRunning():
            self.handler.dataReceived.disconnect()
            self.handler.stop()
            self.telemetryThread.exit()
        else:
            self.telemetryThread.start()
            self.handler.start()
            self.handler.dataReceived.connect(self.updateWidgets)
            self.connectionBar.sendData.connect(self.handler.sendData)


    def updateWidgets(self, data):
        hum = data[0] 
        self.connectionBar.update(hum)


def main():
    app=QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()

main()