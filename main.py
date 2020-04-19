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
        self.serverThread=QtCore.QThread() 
        self.server = connectionHandler('localhost',8080)
        self.server.moveToThread(self.serverThread)
        self.clientsconnected = 0
        self.serverThread.started.connect(self.server.run)
        self.server.clientConnected.connect(self.setupConnection)



    def setupConnection(self):
        self.server.clients[self.clientsconnected].dataReceived.connect(self.updateWidgets)
        self.clientsconnected += 1
        

    def manageConnection(self):
        if self.serverThread.isRunning():
            print(self.clientsconnected)
            for i in range (self.clientsconnected):
                self.server.clients[i].dataReceived.disconnect()
                self.server.clients[i].close()
            self.clientsconnected = 0
            self.server.stop()
            self.serverThread.exit()
        else:
            self.serverThread.start()
            self.server.start()
            


    def updateWidgets(self, data):
        #print(data)
        #hum = data[0] 
        self.connectionBar.update(data)


def main():
    app=QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()

main()