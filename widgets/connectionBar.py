from PyQt5 import QtWidgets
from .connectionBar_ui import Ui_connectionBar

class connectionBar(QtWidgets.QWidget,Ui_connectionBar):
    def __init__(self,parent=None):
       QtWidgets.QWidget.__init__(self,parent)
       self.setupUi(self)       
#tu się zaczyna obsługa waszego widgetu -> wszystkie guziki, wykresy i co tam ma być obsługuje się tylko tu
       self.b_connect.pressed.connect(self.b_connectAction)         
       #self.setStyleSheet(open('./style/connectionBar.css').read())
    def b_connectAction(self):
            if self.b_connect.text()=="Connect":
                self.b_connect.setText("Disconnect")
                self.ip_text.setEnabled(False)
                
            else:
                self.b_connect.setText("Connect")
                self.ip_text.setEnabled(True)
#Potrzebna jest jakaś metoda do updatowania widetu...
    def showWidget(self):
        self.show()

    def hideWidget(self):
        self.hide()

#każdy widget może działać jako osobne okno -> super do testowania. odkomentuj kod poniżej i uruchom...
#import sys
#app=QtWidgets.QApplication(sys.argv)
#window = connectionBar()
#window.show()
#app.exec_()
