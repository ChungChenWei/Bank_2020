from PyQt5 import QtWidgets, QtGui, uic, QtCore
from PyQt5.QtWidgets import QFileDialog
import os
import csv
#from mainUI import Ui_MainWindow


# Path from main
UI_NAME = "mainUI.ui"
UI_PATH = "./GUI_Design/" + UI_NAME

path = os.getcwd()
qtCreatorFile = path + os.sep + UI_PATH
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

# Input Data Config
VenueNeed_Col = 5
Table_Col     = 7
Data_Input_Table_Col = 5
#Data_Input_Table_Row = 3

class MainUi(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        
        self.Year      = "108"
        self.Test_Kind = "哈哈"
        self.Subject   = "測試"

        self.G1_Row = -1
        self.G2_Row = -1

        self.VenueNeed = 0

        self.iniGuiEvent()
    
    def iniGuiEvent(self):
        self.L_Year.setText(self.Year)
        self.L_TestKind.setText(self.Test_Kind)
        self.L_Subject.setText(self.Subject)

        # LCD Warning Palette
        self.LCD_NPalette = self.LCD_Produce.palette()
        self.LCD_WPalette = self.LCD_Produce.palette()
        self.LCD_WPalette.setColor(self.LCD_WPalette.WindowText, QtGui.QColor(255, 0, 0))


        # LCD Data input
        self.LCD_VenueNeed.display(str(self.VenueNeed))
        self.LCD_Produce_Change()      

        # Timer setup
        self.Time_Refresh()
        time = QtCore.QTimer(self)
        time.setInterval(1000)
        time.timeout.connect(self.Time_Refresh)
        time.start()         

        # signal and slot
        self.LE_Group.returnPressed.connect(self.L_Group_Change)

        self.LE_Print.returnPressed.connect(self.LCD_Produce_Change)
        self.LE_Waste.returnPressed.connect(self.LCD_Produce_Change)
        self.LE_Table.returnPressed.connect(self.LCD_Produce_Change)

        self.LE_Group.setFocus()

    # When Line Edit of Group Pressed Enter
    def L_Group_Change(self):
        # Group ID and Display Name
        Group_Dic = {'1':"第一組",'2':"第二組"}
        # The input from line edit of Group
        Group_NO = self.LE_Group.text()
        
        # Display the label of Group and change focus to VenueNumber
        if(Group_Dic.__contains__(Group_NO)):
            self.L_Group.setText(Group_Dic[Group_NO])
            self.Group = int(Group_NO)
            self.LE_NO.setFocus()
        
        # Group wrong! Go back to line edit of Group and clear
        else:
            QtWidgets.QMessageBox.warning(self,'錯誤','組別輸入錯誤')
            self.Group = 0
            self.LE_Group.setFocus()
            self.LE_Group.clear()
    
    # When the number about produce has changed
    def LCD_Produce_Change(self):
        # Check if line edit is empty
        if(self.LE_Print.text()==''):
            self.LE_Print.setText('0')
        if(self.LE_Waste.text()==''):
            self.LE_Waste.setText('0')
        if(self.LE_Table.text()==''):
            self.LE_Table.setText('0')
        
        self.LCD_Produce.display(str(int(self.LE_Print.text())-int(self.LE_Waste.text())))

        # Check if need to print more
        if(self.LCD_VenueNeed.intValue()>self.LCD_Produce.intValue()):
            self.LCD_ExPrint.setPalette(self.LCD_WPalette)
            self.LCD_ExPrint.display(str(self.LCD_VenueNeed.intValue()-self.LCD_Produce.intValue()))
        else:
            self.LCD_ExPrint.setPalette(self.LCD_NPalette)
            self.LCD_ExPrint.display('0')

        # Check if need to produce more
        if(self.LCD_VenueNeed.intValue() > self.LCD_Packed.intValue()+int(self.LE_Table.text())):
            self.LCD_ExProduce.setPalette(self.LCD_WPalette)
            self.LCD_ExProduce.display(str(self.LCD_VenueNeed.intValue() - self.LCD_Packed.intValue() - int(self.LE_Table.text())))
        else:
            self.LCD_ExProduce.setPalette(self.LCD_NPalette)
            self.LCD_ExProduce.display('0')

        self.LE_Group.setFocus()
        self.LE_Group.clear()

    def Time_Refresh(self):
        Date = QtCore.QDateTime.currentDateTime()
        Time_Out = Date.toString("hh:mm:ss")
        Date_Out = Date.toString("yyyy年MM月dd日")
        self.Mark = Date.toString("yyyy/MM/dd hh:mm")
        self.LCD_Time.display(Time_Out)
        self.L_Date.setText(Date_Out)
