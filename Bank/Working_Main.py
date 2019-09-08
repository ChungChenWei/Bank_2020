#coding=utf-8
from PyQt5 import QtWidgets, QtGui

from campForm import CampUi
from withdrawalForm import WithdrawalUi
from depositForm import DepositUi
from finalForm import FinalUi

import os
import sys
import json
import csv
import shutil

####'''
# Under Develope
# 1.小隊積分
# 0106 0306 0406
# 2.focus調整
# 3.table 順序
# 4.進入mode(切換)要顯示
# 5.返回鍵可以設定(event)
####

if __name__ == "__main__":

    def AccSetup(Account,Money):
        # Update With and Depo Page
        Withdrawal.Open_Init(Account,Money)
        Deposit.Open_Init(Account,Money)
        Final.Open_Init(Account,Money,0)
        # Add in No Interest List
        if(Account not in Account_No_Interest):
            Account_No_Interest.append(Account)

    def AccUpdate(Account,Money,depo,withd):
        # Account Data Input
        Account_Data = AccountJsonInput()
        # Log Update
        log_Update(Account,MainInterface.Time_Out,depo,withd,Money)
        # Account Data Update
        Account_Data[Account] = Money
        print("Update",Account,Money,'\n')
        # Account Data Output
        AccountJsonOutput(Account_Data)
        # Update Final Page
        Final.Open_Init(Account,Money,depo+withd)
        # Add in In Use List
        if(Account not in Account_In_Use and Money != 0):
            Account_In_Use.append(Account)
        elif(Money==0):
            try:
                Account_In_Use.remove(Account)
            except:
                pass
        with open("./Data/Account_In_Use.csv","w") as csvfile:
            csv.writer(csvfile).writerow(Account_In_Use)

    def Bank_Update(Account_Present):
        print("Present Working Account",Account_Present)
        # Account Data Input
        Account_Data = AccountJsonInput()
        #### Back Side Monitor
        print("In Use ",Account_In_Use)
        print("No Add ",Account_No_Interest)
        # If account is in use and not in no interest
        for Account in Account_In_Use:
            if( Account not in Account_No_Interest and not(Account in Account_Present)):
                # Bank Interest Update
                Interest = int(Account_Data[Account] * InterestRate)
                Account_Data[Account] += Interest
                # Log Update
                log_Update(Account,MainInterface.Time_Out,Interest,0,Account_Data[Account])
                #### Back Side Monitor
                print("Update",Account,Account_Data[Account])
        # Clean up No Interest List
        Account_No_Interest.clear()
        # Account Data Output
        AccountJsonOutput(Account_Data)
        #### Back Side Monitor
        print("Bank Update!\n")

        ####
        # Consider Output No Interest List to file
        ####

    def ChildClose():
        MainInterface.LE_Group.clear()
        MainInterface.LE_Group.setFocus()
        MainInterface.Account = ""
        MainInterface.BT_WithDrawal.hide()
        MainInterface.BT_Deposit.hide()
        MainInterface.BT_AccountSearch.hide()
        MainInterface.L_Serve.hide()

    def log_Update(Account,Time,depo,withd,Money):
        try:
            log = open("./Data/Log/"+Account+".csv","a", newline='')
        except:
            log = open("./Data/Log/"+Account+".csv","w", newline='')
        csv.writer(log).writerow([Time,depo,withd,Money])
        log.close()
    def AccountJsonInput():
        with open("./Data/Account.json","r") as jsonfile:
            return json.load(jsonfile)
    def AccountJsonOutput(OutputData):
        with open("./Data/Account.json","w") as jsonfile:
            json.dump(OutputData,jsonfile)

    # Global Var
    Account_In_Use      = []
    Account_No_Interest = []
    Account_Data        = {}
    Account_Init_List   = "./Data/TestAccount.csv"
    InterestRate        = 0.01

    # if Account.json is not exit, then reset the account setting
    if(not os.path.isfile("./Data/Account.json")):
        print("Reset Account Start")
        # Remove Log files and Recreat
        shutil.rmtree("./Data/Log/")
        os.mkdir("./Data/Log/")
        # Remove In-Use file and Recreat
        os.remove("./Data/Account_In_Use.csv")
        csvfile = open("./Data/Account_In_Use.csv","w")
        csvfile.close()
        # Load Accout List
        with open(Account_Init_List,"r") as csvfile:
            for acc in next(csv.reader(csvfile)):
                Account_Data[acc] = 0
        # Reset Account Data
        with open("./Data/Account.json","w") as jsonfile:
            json.dump(Account_Data,jsonfile)
        print("Reset Account Done")
    else:
        with open("./Data/Account_In_Use.csv","r") as csvfile:
            try:
                Account_In_Use = next(csv.reader(csvfile))
            except:
                pass

    # Window define
    app = QtWidgets.QApplication(sys.argv)
    MainInterface = CampUi()
    Withdrawal    = WithdrawalUi()
    Deposit       = DepositUi()
    Final         = FinalUi()
    MainInterface.showMaximized()

    # Button Connect
    MainInterface.WithOpenSig.connect(Withdrawal.showMaximized)
    MainInterface.DepoOpenSig.connect(Deposit.showMaximized)
    MainInterface.FinalOpenSig.connect(Final.showMaximized)
    MainInterface.IncreRateSig.connect(Bank_Update)
    MainInterface.AccSig.connect(AccSetup)

    # Signal and Slot
    Withdrawal.WithSig.connect(AccUpdate)
    Withdrawal.FinalSig.connect(Final.showMaximized)
    Withdrawal.CloseSig.connect(ChildClose)
    Deposit.DepoSig.connect(AccUpdate)
    Deposit.FinalSig.connect(Final.showMaximized)
    Deposit.CloseSig.connect(ChildClose)
    Final.CloseSig.connect(ChildClose)

    app.exec_() 