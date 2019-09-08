from PyQt5 import QtWidgets, QtGui, uic, QtCore
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import pyqtSignal as qtsig
import os
import csv
import json
#from page1 import Ui_MainWindow

# Path from main
UI_NAME = "page1.ui"
UI_PATH = "./GUI_Design/" + UI_NAME

Ui_MainWindow, QtBaseClass = uic.loadUiType(UI_PATH)

class CampUi(QtWidgets.QMainWindow, Ui_MainWindow):

    AccSig = qtsig(str,int)
    WithOpenSig = qtsig()
    DepoOpenSig = qtsig()
    FinalOpenSig = qtsig()
    IncreRateSig = qtsig(str)

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.iniGuiEvent()
    
    def iniGuiEvent(self):
        # Initial
        #self.LCD_Length.display("5")
        #self.LCD_Interest_Rate.display("2")
        self.MessageHide()

        # Timer setup
        self.Time_Refresh()
        time = QtCore.QTimer(self)
        time.setInterval(1000)
        time.timeout.connect(self.Time_Refresh)
        time.start()

        # Button Connect
        self.BT_WithDrawal.clicked.connect(self.Group_Enter)
        self.BT_Deposit.clicked.connect(self.Group_Enter)
        self.BT_AccountSearch.clicked.connect(self.Group_Enter)
        self.LE_Group.returnPressed.connect(self.Group_Pressed)

    def Time_Refresh(self):
        Date = QtCore.QDateTime.currentDateTime()
        self.Time_Out = Date.toString("hh:mm:ss")
        Count_Min = int(Date.toString("mm"))
        Count_Sec = int(Date.toString("ss"))
        if(Count_Min % 5 == 0 and Count_Sec % 60 == 0):
            print("Time to add")
            self.IncreRateSig.emit(self.Account)
        self.LCD_Time.display(self.Time_Out)

    def Group_Pressed(self):
        # Open Account Data
        with open("./Data/Account.json","r",encoding='utf8') as jsonfile:
            self.Account_dic = json.load(jsonfile)
        
        # Get Input Account
        self.Account = self.LE_Group.text()
        
        # Checking for Account Existence
        if(self.Account not in self.Account_dic.keys()):
            QtWidgets.QMessageBox.warning(self,'警告','查無學號!')
            self.MessageHide()
        else:
            print("Correct Account!\n")
            self.AccSig.emit(self.Account,self.Account_dic[self.Account])
            self.MessageShow()        

    def Group_Enter(self):
        if(self.sender().objectName()=="BT_WithDrawal"):
            self.WithOpenSig.emit()
            print("Withdrawal!")
        elif(self.sender().objectName()=="BT_Deposit"):
            self.DepoOpenSig.emit()
            print("Deposit!")
        elif(self.sender().objectName()=="BT_AccountSearch"):
            self.FinalOpenSig.emit()
            print("Inquiry!\n")

    def keyPressEvent(self, event):
        if(event.key()==QtCore.Qt.Key_Escape):
            self.MessageHide()

    def MessageShow(self):
        self.BT_WithDrawal.show()
        self.BT_Deposit.show()
        self.BT_AccountSearch.show()
        self.L_Serve.show()
        self.L_ServeEN.show()
    def MessageHide(self):
        self.Account = ""
        self.LE_Group.clear()
        self.LE_Group.setFocus()
        self.BT_WithDrawal.hide()
        self.BT_Deposit.hide()
        self.BT_AccountSearch.hide()
        self.L_Serve.hide()
        self.L_ServeEN.hide()

            