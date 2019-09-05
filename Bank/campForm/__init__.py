from PyQt5 import QtWidgets, QtGui, uic, QtCore
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import pyqtSignal as qtsig
import os
import csv
import json
#from campUI import Ui_MainWindow

# Path from main
UI_NAME = "page1.ui"
UI_PATH = "./GUI_Design/" + UI_NAME

path = os.getcwd()
qtCreatorFile = path + os.sep + UI_PATH
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

''' Object_Name
LCD_Length
LCD_Interest_Rate
LCD_Time

BT_WithDrawal
BT_Deposit

'''

class CampUi(QtWidgets.QMainWindow, Ui_MainWindow):

    AccSig = qtsig(str,int)
    WithOpenSig = qtsig()
    DepoOpenSig = qtsig()
    IncreRateSig = qtsig()

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.iniGuiEvent()
        #print(self.Account_dic.keys())
    
    def iniGuiEvent(self):
        # Initial
        #self.LCD_Length.display("5")
        #self.LCD_Interest_Rate.display("2")
        self.LE_Group.setFocus()

        # Timer setup
        self.Time_Refresh()
        time = QtCore.QTimer(self)
        time.setInterval(1000)
        time.timeout.connect(self.Time_Refresh)
        time.start()

        # Signal and Slot
        # Button
        self.BT_WithDrawal.clicked.connect(self.Group_Enter)
        self.BT_Deposit.clicked.connect(self.Group_Enter)

    def Time_Refresh(self):
        Date = QtCore.QDateTime.currentDateTime()
        Time_Out = Date.toString("hh:mm:ss")
        Count_Out = int(Date.toString("ss"))
        if(Count_Out%10==0):
            print("Time to add")
            self.IncreRateSig.emit()
        self.LCD_Time.display(Time_Out)

    def Group_Enter(self):
        # Open Account Data
        with open("./Data/Account.json","r",encoding='utf8') as jsonfile:
            self.Account_dic = json.load(jsonfile)
        
        # Get Input Account
        self.Account = self.LE_Group.text()
        
        # Checking for Account Existence
        if(self.Account not in self.Account_dic.keys()):
            QtWidgets.QMessageBox.warning(self,'警告','查無學號!')
            self.Account = ""
            self.LE_Group.clear()
            self.LE_Group.setFocus()
        else:
            print("Correct Account!")
            self.AccSig.emit(self.Account,self.Account_dic[self.Account])
            if(self.sender().objectName()=="BT_WithDrawal"):
                self.WithOpenSig.emit()
            elif(self.sender().objectName()=="BT_Deposit"):
                self.DepoOpenSig.emit()

            # Some Success Message Appare on the Ui
        
