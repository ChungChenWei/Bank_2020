from PyQt5 import QtWidgets, QtGui, uic, QtCore
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import pyqtSignal as qtsig
import os
import csv
#from final import Ui_MainWindow

# Path from main
UI_NAME = "final.ui"
UI_PATH = "./GUI_Design/" + UI_NAME
Ui_MainWindow, QtBaseClass = uic.loadUiType(UI_PATH)

class FinalUi(QtWidgets.QMainWindow, Ui_MainWindow):

    # CloseSig : Before Close this window, tell the parten window to update
    CloseSig = qtsig()

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Button Connect
        self.BT_Back.clicked.connect(self.close)
        # Table Setup
        header = self.Table.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
    
    def Open_Init(self,Account,Money,Trade):
        # Display Setup
        self.LE_Account.setText(Account)
        self.LCD_Trade.display(str(Trade))
        self.LCD_Money.display(str(Money))
        try:
            # Open Log file
            log = open("./Data/Log/"+Account+".csv","r", newline='')
            Rows = csv.reader(log)
            # Table Update
            self.Table_Update(Rows)
            log.close()
        except:
            pass

    def Table_Update(self,Input):
        self.Table.clearContents()
        for i,row in enumerate(Input):
            self.Table.setRowCount(i+1)
            for j in range(4):
                self.Table.setItem(i,j,self.ItemCreatorWithVHC(row[j]))

    def ItemCreatorWithVHC(self,Content):
        newItem = QtWidgets.QTableWidgetItem(str(Content))
        newItem.setTextAlignment(QtCore.Qt.AlignVCenter)
        newItem.setTextAlignment(QtCore.Qt.AlignHCenter)
        return newItem

    def closeEvent(self,event):
        self.CloseSig.emit()
        event.accept()
