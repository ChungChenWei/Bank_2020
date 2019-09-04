from PyQt5 import QtWidgets, QtGui, uic, QtCore
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import pyqtSignal as qtsig
import os
#from depositUI import Ui_MainWindow

# Path from main
UI_NAME = "deposit.ui"
UI_PATH = "./GUI_Design/" + UI_NAME

path = os.getcwd()
qtCreatorFile = path + os.sep + UI_PATH
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

''' Object_Name
LCD_Total

LE_Deposit

BT_Confirm
BT_Cancel

'''

class DepositUi(QtWidgets.QMainWindow, Ui_MainWindow):
 
    CloseSig = qtsig()
    DepoSig  = qtsig(str,int)

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.iniGuiEvent()
    
    def Open_Init(self,Account,Money):
        # Account Update
        self.acc = Account
        self.money = Money

        self.LCD_Total.display(str(Money))
        self.LE_Deposit.setText("")
        self.LE_Deposit.setFocus()

        #print("Deposit Mode\nSetup",Account,Money)

    def closeEvent(self,event):
        self.CloseSig.emit()
        event.accept()

    def iniGuiEvent(self):
        # Signal and Slot
        # LE
        self.LE_Deposit.returnPressed.connect(self.Deposit_Enter)

        # Button
        self.BT_Confirm.clicked.connect(self.Deposit)
        self.BT_Cancel.clicked.connect(self.close)

    def Deposit(self):
        #QtWidgets.QMessageBox.information(self,'測試','這是確定按下去之後會跳出來的東西')
        self.money += self.depo_money
        print("Deposit",self.depo_money,"Remain",self.money)
        self.DepoSig.emit(self.acc,self.money)
        self.close()
        

    def Deposit_Enter(self):
        try:
            self.depo_money = int(self.sender().text())
        except:
            self.depo_money = 0
            QtWidgets.QMessageBox.warning(self,'警告','金額錯誤!')
            self.LE_Deposit.clear()
            self.LE_Deposit.setFocus()
        #print("Enter",self.with_money)
