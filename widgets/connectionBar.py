from PyQt5 import QtWidgets
from .connectionBar_ui import Ui_connectionBar

#Creating child class of Ui_connectionBar and qwidget
class connectionBar(QtWidgets.QWidget,Ui_connectionBar):
    def __init__(self,parent=None):
       QtWidgets.QWidget.__init__(self,parent)
       self.setupUi(self)       
#now you can add labels stylesheets... whatever you need
       self.b_connect.pressed.connect(self.b_connectAction)         
       #self.setStyleSheet(open('./style/connectionBar.css').read())
    def b_connectAction(self):
            if self.b_connect.text()=="Connect":
                self.b_connect.setText("Disconnect")
                self.ip_text.setEnabled(False)
                
            else:
                self.b_connect.setText("Connect")
                self.ip_text.setEnabled(True)

    def update(self):
        self.show()

   

#każdy widget może działać jako osobne okno -> super do testowania. odkomentuj kod poniżej i uruchom...
#import sys
#app=QtWidgets.QApplication(sys.argv)
#window = connectionBar()
#window.show()
#app.exec_()
