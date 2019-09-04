from PyQt5 import QtWidgets, QtGui, uic, QtCore
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import pyqtSignal as qtsig
import os
#from withdrawalUI import Ui_MainWindow


# Path from main
UI_NAME = "withdrawal.ui"
UI_PATH = "./GUI_Design/" + UI_NAME

path = os.getcwd()
qtCreatorFile = path + os.sep + UI_PATH
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

''' Object_Name
LCD_Total

LE_Withdrawal

BT_Confirm
BT_Cancel

'''

class WithdrawalUi(QtWidgets.QMainWindow, Ui_MainWindow):

    CloseSig = qtsig()
    WithSig  = qtsig(str,int)

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
        self.LE_Withdrawal.setText("")
        self.LE_Withdrawal.setFocus()

        #print("Withdrawal Mode\nSetup",Account,Money)

    def closeEvent(self,event):
        self.CloseSig.emit()
        event.accept()

    def iniGuiEvent(self):
        # Signal and Slot
        # LE
        self.LE_Withdrawal.returnPressed.connect(self.Withdrawal_Enter)

        # Button
        self.BT_Confirm.clicked.connect(self.WithDrawal)
        self.BT_Cancel.clicked.connect(self.close)

    def WithDrawal(self):
        #QtWidgets.QMessageBox.information(self,'測試','這是確定按下去之後會跳出來的東西')
        self.money -= self.with_money
        print("WithDrawal",self.with_money,"Remain",self.money)
        self.WithSig.emit(self.acc,self.money)
        self.close()    

    def Withdrawal_Enter(self):
        try:
            self.with_money = int(self.sender().text())
            if(self.with_money > self.money):
                QtWidgets.QMessageBox.warning(self,'警告','餘額不足!')
                self.LE_Withdrawal.clear()
                self.LE_Withdrawal.setFocus()
        except:
            self.with_money = 0
            QtWidgets.QMessageBox.warning(self,'警告','金額錯誤!')
            self.LE_Withdrawal.clear()
            self.LE_Withdrawal.setFocus()
        #print("Enter",self.with_money)
