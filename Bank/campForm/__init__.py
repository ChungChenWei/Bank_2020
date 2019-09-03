from PyQt5 import QtWidgets, QtGui, uic, QtCore
from PyQt5.QtWidgets import QFileDialog
import os
import csv
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
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.iniGuiEvent()
    
    def iniGuiEvent(self):
        # Initial
        #self.LCD_Length.display("5")
        #self.LCD_Interest_Rate.display("2")

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
        #Date_Out = Date.toString("yyyy年MM月dd日")
        #self.Mark = Date.toString("yyyy/MM/dd hh:mm")
        self.LCD_Time.display(Time_Out)
        #self.L_Date.setText(Date_Out)

    def WithDrawal(self):
        QtWidgets.QMessageBox.information(self,'測試','這是WithDrawal按下去之後會跳出來的東西')

    def Deposit(self):
        QtWidgets.QMessageBox.information(self,'測試','這是Deposit按下去之後會跳出來的東西')

    def Group_Enter(self):
        QtWidgets.QMessageBox.information(self,'測試','這是組別輸入完會跳出來的東西')
        
