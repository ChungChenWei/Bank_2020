#coding=utf-8
from PyQt5 import QtWidgets, QtGui

from campForm import CampUi
from withdrawalForm import WithdrawalUi
from depositForm import DepositUi

import sys
import json
import csv

if __name__ == "__main__":

    def AccSetup(Account,Money):
        Withdrawal.Open_Init(Account,Money)
        Deposit.Open_Init(Account,Money)
        print("Setup",Account,Money)

    def AccUpdate(Account,Money):
        with open("./Data/Account.json","r",encoding='utf8') as jsonfile:
            Account_dic = json.load(jsonfile)
        Account_list=[]
        with open("./Data/Account.csv","r", newline='') as fp:
            Rows = csv.reader(fp)
            for Row in Rows:
                Account_list = list(Row)
        
        Account_dic[Account] = Money
        Account_list.append(Account)
        print("Update",Account,Money,"\n")
        print(Account_list)

        with open("./Data/Account.json","w",encoding='utf8') as jsonfile:
            json.dump(Account_dic,jsonfile)
        with open("./Data/Account.csv","w", newline='') as fp:
            csv.writer(fp).writerow(Account_list)

    def Bank_Update():
        with open("./Data/Account.json","r",encoding='utf8') as jsonfile:
            Account_dic = json.load(jsonfile)
        Account_list=[]
        with open("./Data/Account.csv","r", newline='') as fp:
            Rows = csv.reader(fp)
            for Row in Rows:
                Account_list = list(Row)

        for Account in Account_dic.keys():
            if(Account not in Account_list):
                Account_dic[Account] *= 1.01
                print("Update",Account,Account_dic[Account])

        with open("./Data/Account.json","w",encoding='utf8') as jsonfile:
            json.dump(Account_dic,jsonfile)
            print("Bank Update!\n")
        with open("./Data/Account.csv","w", newline='') as fp:
            csv.writer(fp).writerow([])

    def ChildClose():
        MainInterface.LE_Group.clear()
        MainInterface.LE_Group.setFocus()

    #def run_app():
    app = QtWidgets.QApplication(sys.argv)
    MainInterface = CampUi()
    Withdrawal    = WithdrawalUi()
    Deposit       = DepositUi()
    MainInterface.showMaximized()

    # Button Connect
    MainInterface.WithOpenSig.connect(Withdrawal.showMaximized)
    MainInterface.DepoOpenSig.connect(Deposit.showMaximized)
    MainInterface.IncreRateSig.connect(Bank_Update)

    # Signal and Slot
    MainInterface.AccSig.connect(AccSetup)
    Withdrawal.CloseSig.connect(ChildClose)
    Withdrawal.WithSig.connect(AccUpdate)
    Deposit.CloseSig.connect(ChildClose)
    Deposit.DepoSig.connect(AccUpdate)

    app.exec_() 
    #run_app()