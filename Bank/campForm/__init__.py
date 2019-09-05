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
        # LE
        self.LE_Group.returnPressed.connect(self.Group_Enter)

        # Button
        self.BT_WithDrawal.clicked.connect(self.WithDrawal)
        self.BT_Deposit.clicked.connect(self.Deposit)


    def Time_Refresh(self):
        Date = QtCore.QDateTime.currentDateTime()
        Time_Out = Date.toString("hh:mm:ss")
        Count_Out = int(Date.toString("ss"))
        if(Count_Out%10==0):
            print("Time to add")
            self.IncreRateSig.emit()
        self.LCD_Time.display(Time_Out)

    def WithDrawal(self):
        if(self.LE_Group.text()!=""):
            self.WithOpenSig.emit()
        else:
            print("Empty Account!\n")
        #QtWidgets.QMessageBox.information(self,'測試','這是WithDrawal按下去之後會跳出來的東西')

    def Deposit(self):
        if(self.LE_Group.text()!=""):
            self.DepoOpenSig.emit()
        else:
            print("Empty Account!\n")
        #QtWidgets.QMessageBox.information(self,'測試','這是Deposit按下去之後會跳出來的東西')

    def Group_Enter(self):
        with open("./Data/Account.json","r",encoding='utf8') as jsonfile:
            self.Account_dic = json.load(jsonfile)
        self.Account = self.sender().text()
        if(self.Account not in self.Account_dic.keys()):
            QtWidgets.QMessageBox.warning(self,'警告','查無學號!')
            self.LE_Group.clear()
            self.LE_Group.setFocus()
        else:
            print("Correct Account!")
            self.AccSig.emit(self.Account,self.Account_dic[self.Account])
            # Some Success Message Appare on the Ui
        
