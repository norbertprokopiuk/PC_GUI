import asyncore
import socket
from PyQt5 import QtCore



class clientHandler(asyncore.dispatcher_with_send,QtCore.QObject):
    
    dataReceived = QtCore.pyqtSignal(object)

    def __init__(self,conn):
        QtCore.QObject.__init__(self)
        asyncore.dispatcher_with_send.__init__(self,conn)

    def handle_read(self):
        data = self.recv(8192)
        self.dataReceived.emit(data)
        
     
            





class connectionHandler(QtCore.QObject,asyncore.dispatcher):   
    clientConnected = QtCore.pyqtSignal()

    clients = []

    def __init__(self,ip,port):
      asyncore.dispatcher.__init__(self)
      QtCore.QObject.__init__(self)
      self.ip =ip
      self.port = port
     


    @QtCore.pyqtSlot()
    def run(self):  #here we should use class for odroid connection. 
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind((self.ip,self.port))
        self.listen(5)
        
        asyncore.loop()


    def stop(self):
        self.active=False

    def start(self):
        self.active = True

        #asyncore specific
    def handle_accept(self):
        client_info = self.accept()
        if client_info is not None:
            conn, addr = client_info
            print("connected with: ", addr)
            self.clients.append (clientHandler(conn))
            self.clientConnected.emit()