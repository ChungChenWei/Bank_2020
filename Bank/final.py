# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'final.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1590, 755)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Chekiang Sung")
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.Central_Grid = QtWidgets.QGridLayout()
        self.Central_Grid.setObjectName("Central_Grid")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.Central_Grid.addItem(spacerItem, 4, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 13, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.Central_Grid.addItem(spacerItem1, 6, 0, 1, 1)
        self.Grid_Slogan = QtWidgets.QGridLayout()
        self.Grid_Slogan.setObjectName("Grid_Slogan")
        self.L_Slogan = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.L_Slogan.sizePolicy().hasHeightForWidth())
        self.L_Slogan.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("標楷體")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.L_Slogan.setFont(font)
        self.L_Slogan.setObjectName("L_Slogan")
        self.Grid_Slogan.addWidget(self.L_Slogan, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.Central_Grid.addLayout(self.Grid_Slogan, 9, 0, 1, 1)
        self.Grid_Time = QtWidgets.QGridLayout()
        self.Grid_Time.setObjectName("Grid_Time")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.Grid_Time.addItem(spacerItem2, 0, 0, 1, 1)
        self.Grid_Time.setColumnStretch(0, 1)
        self.Central_Grid.addLayout(self.Grid_Time, 2, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.Central_Grid.addItem(spacerItem3, 8, 0, 1, 1)
        self.Grid_Title = QtWidgets.QGridLayout()
        self.Grid_Title.setContentsMargins(0, -1, -1, -1)
        self.Grid_Title.setObjectName("Grid_Title")
        self.Title = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("SetoFont")
        font.setPointSize(60)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.Title.setFont(font)
        self.Title.setScaledContents(False)
        self.Title.setObjectName("Title")
        self.Grid_Title.addWidget(self.Title, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.Central_Grid.addLayout(self.Grid_Title, 0, 0, 1, 1)
        self.Grid_Detail = QtWidgets.QGridLayout()
        self.Grid_Detail.setObjectName("Grid_Detail")
        self.Grid_Rate = QtWidgets.QGridLayout()
        self.Grid_Rate.setObjectName("Grid_Rate")
        self.LE_Account = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.LE_Account.setFont(font)
        self.LE_Account.setFocusPolicy(QtCore.Qt.NoFocus)
        self.LE_Account.setObjectName("LE_Account")
        self.Grid_Rate.addWidget(self.LE_Account, 0, 0, 1, 1)
        self.Grid_Detail.addLayout(self.Grid_Rate, 0, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.Grid_Detail.addItem(spacerItem4, 0, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("標楷體")
        font.setPointSize(40)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.Grid_Detail.addWidget(self.label_3, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.Grid_Detail.setColumnStretch(0, 1)
        self.Grid_Detail.setColumnStretch(1, 1)
        self.Grid_Detail.setColumnStretch(2, 2)
        self.Central_Grid.addLayout(self.Grid_Detail, 1, 0, 1, 1)
        self.Grid_Group = QtWidgets.QGridLayout()
        self.Grid_Group.setObjectName("Grid_Group")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("標楷體")
        font.setPointSize(40)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.Grid_Group.addWidget(self.label, 0, 2, 1, 1)
        self.L_Group = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("標楷體")
        font.setPointSize(40)
        self.L_Group.setFont(font)
        self.L_Group.setObjectName("L_Group")
        self.Grid_Group.addWidget(self.L_Group, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.Grid_Group.addItem(spacerItem5, 0, 3, 1, 1)
        self.LCD_Trade = QtWidgets.QLCDNumber(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(40)
        self.LCD_Trade.setFont(font)
        self.LCD_Trade.setDigitCount(10)
        self.LCD_Trade.setObjectName("LCD_Trade")
        self.Grid_Group.addWidget(self.LCD_Trade, 0, 1, 1, 1)
        self.Grid_Group.setColumnStretch(0, 1)
        self.Grid_Group.setColumnStretch(1, 1)
        self.Grid_Group.setColumnStretch(3, 2)
        self.Central_Grid.addLayout(self.Grid_Group, 3, 0, 1, 1)
        self.Grid_Button = QtWidgets.QGridLayout()
        self.Grid_Button.setObjectName("Grid_Button")
        self.BT_Back = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BT_Back.sizePolicy().hasHeightForWidth())
        self.BT_Back.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(30)
        self.BT_Back.setFont(font)
        self.BT_Back.setObjectName("BT_Back")
        self.Grid_Button.addWidget(self.BT_Back, 0, 1, 1, 1)
        self.Table = QtWidgets.QTableWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("標楷體")
        font.setPointSize(20)
        self.Table.setFont(font)
        self.Table.setObjectName("Table")
        self.Table.setColumnCount(4)
        self.Table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.Table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.Table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.Table.setHorizontalHeaderItem(3, item)
        self.Table.horizontalHeader().setStretchLastSection(False)
        self.Table.verticalHeader().setVisible(False)
        self.Grid_Button.addWidget(self.Table, 0, 0, 1, 1)
        self.Central_Grid.addLayout(self.Grid_Button, 7, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("標楷體")
        font.setPointSize(40)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("標楷體")
        font.setPointSize(40)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 0, 3, 1, 1)
        self.LCD_Money = QtWidgets.QLCDNumber(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(40)
        self.LCD_Money.setFont(font)
        self.LCD_Money.setDigitCount(10)
        self.LCD_Money.setObjectName("LCD_Money")
        self.gridLayout.addWidget(self.LCD_Money, 0, 1, 1, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 1)
        self.gridLayout.setColumnStretch(3, 2)
        self.Central_Grid.addLayout(self.gridLayout, 5, 0, 1, 1)
        self.Central_Grid.setRowStretch(0, 2)
        self.Central_Grid.setRowStretch(1, 2)
        self.Central_Grid.setRowStretch(2, 1)
        self.Central_Grid.setRowStretch(3, 2)
        self.Central_Grid.setRowStretch(4, 1)
        self.Central_Grid.setRowStretch(5, 2)
        self.Central_Grid.setRowStretch(6, 1)
        self.Central_Grid.setRowStretch(7, 6)
        self.Central_Grid.setRowStretch(8, 1)
        self.Central_Grid.setRowStretch(9, 2)
        self.gridLayout_7.addLayout(self.Central_Grid, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1590, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.L_Slogan.setText(_translate("MainWindow", "一 時 存 錢 一 時 爽 ， 一 直 存 錢 一 直 爽 ， 錢 多 就 比 誰 更 浪 ， 身 價 翻 倍 紅 不 讓"))
        self.Title.setText(_translate("MainWindow", "樂來樂生氣銀行"))
        self.label_3.setText(_translate("MainWindow", "交易帳戶"))
        self.label.setText(_translate("MainWindow", "萬元"))
        self.L_Group.setText(_translate("MainWindow", "交易金額"))
        self.BT_Back.setText(_translate("MainWindow", "返回 RETURN"))
        item = self.Table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "交易時間"))
        item = self.Table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "存入"))
        item = self.Table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "領出"))
        item = self.Table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "餘額"))
        self.label_4.setText(_translate("MainWindow", "萬元"))
        self.label_2.setText(_translate("MainWindow", "帳戶餘額"))

