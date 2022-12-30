from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QFileDialog, QMessageBox
import json
import sys
import numpy as np
import qdarkstyle
from qdarkstyle.dark.palette import DarkPalette
from qdarkstyle.light.palette import LightPalette


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1493, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        # labl TimeBox
        self.lblTimeBox = QtWidgets.QLabel(self.centralwidget)
        self.lblTimeBox.setGeometry(QtCore.QRect(10, 0, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lblTimeBox.setFont(font)
        self.lblTimeBox.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTimeBox.setObjectName("lblTimeBox")
        self.lblDay = QtWidgets.QLabel(self.centralwidget)
        self.lblDay.setGeometry(QtCore.QRect(10, 40, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lblDay.setFont(font)
        self.lblDay.setAlignment(QtCore.Qt.AlignCenter)
        self.lblDay.setObjectName("lblDay")
        # Schedule
        self.gbSchedule = QtWidgets.QGroupBox(self.centralwidget)
        self.gbSchedule.setGeometry(QtCore.QRect(500, 18, 481, 741))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.gbSchedule.setFont(font)
        self.gbSchedule.setAlignment(QtCore.Qt.AlignCenter)
        self.gbSchedule.setObjectName("gbSchedule")
        ##txtSch
        self.dictTxt = {}
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        y = 33
        for i in range(18):
            ObjectName = "txtSch"+str(i+6)
            self.txtSch = QtWidgets.QTextEdit(self.gbSchedule)
            self.txtSch.setGeometry(QtCore.QRect(70, y, 401, 31))
            self.txtSch.setFont(font)
            self.txtSch.setObjectName(ObjectName)
            self.dictTxt[ObjectName] = self.txtSch
            y += 39
        x = 40
        for i in range(18):
            self.lblHour = QtWidgets.QLabel(self.gbSchedule)
            self.lblHour.setGeometry(QtCore.QRect(16, x, 37, 22))
            self.lblHour.setFont(font)
            self.lblHour.setAlignment(QtCore.Qt.AlignCenter)
            self.lblHour.setObjectName("lblHour"+str(i))
            self.lblHour.setText(str(i+6)+":00")
            x += 39
        # Date
        self.gbDate = QtWidgets.QGroupBox(self.centralwidget)
        self.gbDate.setGeometry(QtCore.QRect(10, 193, 207, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.gbDate.setFont(font)
        self.gbDate.setTitle("")
        self.gbDate.setObjectName("gbDate")
        self.lblDate = QtWidgets.QLabel(self.gbDate)
        self.lblDate.setGeometry(QtCore.QRect(8, 10, 47, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblDate.setFont(font)
        self.lblDate.setObjectName("lblDate")
        self.dateEdit = QtWidgets.QDateEdit(self.gbDate)
        self.dateEdit.setGeometry(QtCore.QRect(70, 10, 121, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.dateEdit.setFont(font)
        self.dateEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.dateEdit.setDate(QtCore.QDate(2022, 11, 20))
        self.dateEdit.setObjectName("dateEdit")
        # BrainDump
        self.gbBrainDump = QtWidgets.QGroupBox(self.centralwidget)
        self.gbBrainDump.setGeometry(QtCore.QRect(10, 535, 481, 224))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.gbBrainDump.setFont(font)
        self.gbBrainDump.setAlignment(QtCore.Qt.AlignCenter)
        self.gbBrainDump.setObjectName("gbBrainDump")
        self.txtBrainDump = QtWidgets.QTextEdit(self.gbBrainDump)
        self.txtBrainDump.setGeometry(QtCore.QRect(10, 20, 461, 191))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.txtBrainDump.setFont(font)
        self.txtBrainDump.setObjectName("txtBrainDump")
        self.dictTxt["txtBrainDump"] = self.txtBrainDump
        # TopPriority
        self.gbTopPriority = QtWidgets.QGroupBox(self.centralwidget)
        self.gbTopPriority.setGeometry(QtCore.QRect(10, 281, 211, 241))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.gbTopPriority.setFont(font)
        self.gbTopPriority.setAlignment(QtCore.Qt.AlignCenter)
        self.gbTopPriority.setObjectName("gbTopPriority")

        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        y = 28
        for i in range(3):
            ObjectName = "txtTop"+str(i+1)
            self.txtTop = QtWidgets.QTextEdit(self.gbTopPriority)
            self.txtTop.setGeometry(QtCore.QRect(10, y, 191, 61))
            self.txtTop.setFont(font)
            self.txtTop.setObjectName(ObjectName)
            self.dictTxt[ObjectName] = self.txtTop
            y += 70
        # GoalsDay 
        self.gbGoalsDay = QtWidgets.QGroupBox(self.centralwidget)
        self.gbGoalsDay.setGeometry(QtCore.QRect(240, 20, 241, 501))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.gbGoalsDay.setFont(font)
        self.gbGoalsDay.setAlignment(QtCore.Qt.AlignCenter)
        self.gbGoalsDay.setObjectName("gbGoalsDay")
        self.txtGoalsDay = QtWidgets.QTextEdit(self.gbGoalsDay)
        self.txtGoalsDay.setGeometry(QtCore.QRect(10, 28, 221, 461))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.txtGoalsDay.setFont(font)
        self.txtGoalsDay.setObjectName("txtGoalsDay")
        self.dictTxt["txtGoalsDay"] = self.txtGoalsDay

        self.gbBtn = QtWidgets.QGroupBox(self.centralwidget)
        self.gbBtn.setGeometry(QtCore.QRect(10, 99, 211, 71))
        self.gbBtn.setTitle("")
        self.gbBtn.setObjectName("gbBtn")
        self.btnLoad = QtWidgets.QPushButton(self.gbBtn)
        self.btnLoad.setGeometry(QtCore.QRect(10, 16, 91, 41))
        self.btnLoad.setObjectName("btnLoad")
        self.btnSave = QtWidgets.QPushButton(self.gbBtn)
        self.btnSave.setGeometry(QtCore.QRect(110, 16, 91, 41))
        self.btnSave.setObjectName("btnSave")
        # description
        self.gbdescription = QtWidgets.QGroupBox(self.centralwidget)
        self.gbdescription.setGeometry(QtCore.QRect(990, 18, 491, 741))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.gbdescription.setFont(font)
        self.gbdescription.setAlignment(QtCore.Qt.AlignCenter)
        self.gbdescription.setObjectName("gbdescription")
        self.txtDescription = QtWidgets.QTextEdit(self.gbdescription)
        self.txtDescription.setGeometry(QtCore.QRect(10, 18, 471, 691))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.txtDescription.setFont(font)
        self.txtDescription.setObjectName("txtDescription")
        self.dictTxt["txtDescription"] = self.txtDescription
        ##
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1493, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TimeBox"))
        self.lblTimeBox.setText(_translate("MainWindow", "TIMEBOX"))
        self.gbSchedule.setTitle(_translate("MainWindow", "Schedule"))
        self.lblDay.setText(_translate("MainWindow", "DAYLY"))
        self.lblDate.setText(_translate("MainWindow", "Date: "))
        self.dateEdit.setDisplayFormat(_translate("MainWindow", "yyyy/M/d"))
        self.gbBrainDump.setTitle(_translate("MainWindow", "Brain Dump"))
        self.gbTopPriority.setTitle(_translate("MainWindow", "Top 3 Priorities"))
        self.gbGoalsDay.setTitle(_translate("MainWindow", "Goals of the Day"))
        self.btnLoad.setText(_translate("MainWindow", "Load"))
        self.btnSave.setText(_translate("MainWindow", "Save"))
        self.gbdescription.setTitle(_translate("MainWindow", "Description"))
        self.btnSave.clicked.connect(self.Save)
        self.btnLoad.clicked.connect(self.Load)

    def Load(self):
        temp_var = self.dateEdit.date() 
        filename = str(temp_var.toPyDate())+'.json'

        with open(filename, 'r') as f:
             self.Init = json.load(f)
        
        for x, y in self.Init.items():
            self.dictTxt[str(x)].setPlainText(y)
        
    def Save(self):
        temp_var = self.dateEdit.date() 
        filename = str(temp_var.toPyDate())+'.json'
        self.Init = {}
        for x, y in self.dictTxt.items():
            self.Init[str(x)] = y.toPlainText()

        with open(filename, 'w') as f:
             json.dump(self.Init, f)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet(palette=DarkPalette))
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
