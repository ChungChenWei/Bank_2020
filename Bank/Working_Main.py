#coding=utf-8
from PyQt5 import QtWidgets, QtGui

from campForm import CampUi
from withdrawalForm import WithdrawalUi
from depositForm import DepositUi

import sys
import json

if __name__ == "__main__":

    def AccSetup(Account,Money):
        Withdrawal.Open_Init(Account,Money)
        Deposit.Open_Init(Account,Money)
        print("Setup",Account,Money)

    def AccUpdate(Account,Money):
        with open("./Data/Account.json","r",encoding='utf8') as jsonfile:
            Account_dic = json.load(jsonfile)
        
        Account_dic[Account] = Money
        print("Update",Account,Money,"\n")

        with open("./Data/Account.json","w",encoding='utf8') as jsonfile:
            json.dump(Account_dic,jsonfile)

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

    # Signal and Slot
    MainInterface.AccSig.connect(AccSetup)
    Withdrawal.CloseSig.connect(ChildClose)
    Withdrawal.WithSig.connect(AccUpdate)
    Deposit.CloseSig.connect(ChildClose)
    Deposit.DepoSig.connect(AccUpdate)

    app.exec_() 
    #run_app()