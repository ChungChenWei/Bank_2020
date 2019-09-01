#coding=utf-8
from PyQt5 import QtWidgets, QtGui

from mainForm import MainUi

import sys

if __name__ == "__main__":

    def run_app():
        app = QtWidgets.QApplication(sys.argv)
        window = MainUi()
        window.showMaximized()
        app.exec_() 
    run_app()