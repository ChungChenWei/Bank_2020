from PyQt5 import QtWidgets, QtGui, uic, QtCore
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import pyqtSignal as qtsig
import os
#from withdrawal import Ui_MainWindow

# Path from main
UI_NAME = "withdrawal.ui"
UI_PATH = "./GUI_Design/" + UI_NAME
Ui_MainWindow, QtBaseClass = uic.loadUiType(UI_PATH)

class WithdrawalUi(QtWidgets.QMainWindow, Ui_MainWindow):

    # Self-Define Signal
    # WithSig  : After Withdrwawal, it will send Account, AccountMoney, DepositMoney and WithDrawalMoney information
    # FinalSig : Update the final page
    WithSig  = qtsig(str,int,int,int)
    FinalSig = qtsig()
    CloseSig = qtsig()

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Button Connect
        self.BT_Confirm.clicked.connect(self.WithDrawal)
        self.BT_Cancel.clicked.connect(self.close)
    
    def Open_Init(self,Account,Money):
        # Account Update
        self.Account = Account
        self.AccountMoney = Money
        self.WithDrawalMoney = 0
        # Display Update
        self.LCD_Total.display(str(self.AccountMoney))
        self.LE_Withdrawal.setText("")
        self.LE_Withdrawal.setFocus()    

    def WithDrawal(self):
        # Try to transfer the LineEdit Content to Integer
        try:
            # If possible, continue checking
            self.WithDrawalMoney = int(self.LE_Withdrawal.text())
            # If there is not enough money to withdrawal, show error message
            if(self.WithDrawalMoney > self.AccountMoney):
                QtWidgets.QMessageBox.warning(self,'警告','帳戶餘額不足!')
            # If the input number is a negative number
            elif(self.WithDrawalMoney < 0):
                QtWidgets.QMessageBox.warning(self,'警告','金額不能為負!')
            elif(self.WithDrawalMoney < 100):
                QtWidgets.QMessageBox.warning(self,'警告','金額最小必須是100萬元!')
            else:
                # Calculate the result and send message to back side
                self.AccountMoney -= self.WithDrawalMoney
                print("WithDrawal",self.WithDrawalMoney,"Remain",self.AccountMoney)
                # Send information
                self.WithSig.emit(self.Account,self.AccountMoney,0,self.WithDrawalMoney)
                # After send message, call final page
                self.FinalSig.emit()
                # And close this page
                self.close()
        except:
            # If impossible, show error message
            QtWidgets.QMessageBox.warning(self,'警告','金額無法辨識!')
        
        # If not close, then clean up the LineEdit and reset the focus
        self.LE_Withdrawal.clear()
        self.LE_Withdrawal.setFocus()

    def closeEvent(self,event):
        self.CloseSig.emit()
        event.accept()