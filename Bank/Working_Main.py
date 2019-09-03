#coding=utf-8
from PyQt5 import QtWidgets, QtGui

from campForm import CampUi

import sys

if __name__ == "__main__":

    def run_app():
        app = QtWidgets.QApplication(sys.argv)
        window = CampUi()
        window.showMaximized()
        app.exec_() 
    run_app()