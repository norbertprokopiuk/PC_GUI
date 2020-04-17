
from PyQt5 import QtCore

import time

class connectionHandler(QtCore.QObject):   
    dataReceived = QtCore.pyqtSignal(object)
    def __init__(self):
      super(connectionHandler,self).__init__()
      self.txAvailable =True
      self.dataBuffer = []
      self.active = True


    @QtCore.pyqtSlot()
    def receiveData(self):  #here we should use class for odroid connection. 
        a= 50
        while self.active:
            a+=1
            if a>60:
                a=50
            time.sleep(0.3)
            data=(a,1)
            self.dataReceived.emit(data)
    
    @QtCore.pyqtSlot(object)
    def sendData(self, data=[]):
        self.dataBuffer=data

    def stop(self):
        self.active=False

    def start(self):
        self.active = True