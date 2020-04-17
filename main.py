import sys, time
from PyQt5 import QtWidgets, uic, QtGui, QtCore


from mainwindow import Ui_MainWindow


class telemetryThread(QtCore.QThread):   
    
    dataReceived = QtCore.pyqtSignal(object)
    def __init__(self, parent = None):
       super(telemetryThread, self).__init__(parent)

    def run(self):  #here we should use class for odroid connection. 
        a= 50
        while 1:
            a+=1
            if a>60:
                a=50
            time.sleep(0.3)
            data=(a,1)
            self.dataReceived.emit(data)

    def sendData(self, data=()):
        pass

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.setupUi(self)
        self.setStyleSheet(open('style/mainWindow.css').read())
        self.telemetryThread=telemetryThread()
        self.connectionBar.b_connect.pressed.connect(self.manageConnection)
        

    def manageConnection(self):
        if self.telemetryThread.isRunning():
            self.telemetryThread.dataReceived.disconnect()
            self.telemetryThread.terminate()
        else:
            
            self.telemetryThread.start()
            self.telemetryThread.dataReceived.connect(self.updateWidgets)
            self.connectionBar.sendData.connect(self.telemetryThread.sendData)

    def updateWidgets(self, data):
        hum = data[0]
        
        self.connectionBar.update(hum)


def main():
    app=QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()

main()