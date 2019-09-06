from PyQt5 import QtWidgets, QtGui, uic, QtCore
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import pyqtSignal as qtsig
import os
#from depositUI import Ui_MainWindow

# Path from main
UI_NAME = "deposit.ui"
UI_PATH = "./GUI_Design/" + UI_NAME
Ui_MainWindow, QtBaseClass = uic.loadUiType(UI_PATH)

class DepositUi(QtWidgets.QMainWindow, Ui_MainWindow):

    # Self-Define Signal
    # DepoSig  : After Deposit, it will send Account, AccountMoney, DepositMoney and WithDrawalMoney information
    # FinalSig : Update the final page
    DepoSig  = qtsig(str,int,int,int)
    FinalSig = qtsig()
    CloseSig = qtsig()

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Button Conncet
        self.BT_Confirm.clicked.connect(self.Deposit)
        self.BT_Cancel.clicked.connect(self.close)  

    def Open_Init(self,Account,Money):
        # Account Update
        self.Account = Account
        self.AccountMoney = Money
        self.DepositMoney = 0
        # Display Update
        self.LCD_Total.display(str(Money))
        self.LE_Deposit.setText("")
        self.LE_Deposit.setFocus()

    def Deposit(self):
        # Try to transfer the LineEdit Content to Integer
        try:
            # If possible, continue checking
            self.DepositMoney = int(self.LE_Deposit.text())
            # If the input number is a negative number
            if(self.DepositMoney<0):
                QtWidgets.QMessageBox.warning(self,'警告','金額不能為負!')
            else:
                # Calculate the result and send message to back side
                self.AccountMoney += self.DepositMoney
                print("Deposit",self.DepositMoney,"Remain",self.AccountMoney)
                # Send information
                self.DepoSig.emit(self.Account,self.AccountMoney,self.DepositMoney,0)
                # After send message, call final page
                self.FinalSig.emit()
                # And close this page
                self.close()
        except:
            # If impossible, show error message
            QtWidgets.QMessageBox.warning(self,'警告','金額無法辨識!')
        
        # If not close, then clean up the LineEdit and reset the focus
        self.LE_Deposit.clear()
        self.LE_Deposit.setFocus()

    def closeEvent(self,event):
        self.CloseSig.emit()
        event.accept()

        