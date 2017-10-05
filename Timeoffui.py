# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Timeoffui.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

import time
import subprocess
import Timeoff_rc
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(301, 138)
        font = QtGui.QFont()
        font.setPointSize(12)
        Form.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icon/Aha-Soft-Large-Calendar-Clock.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.timeEdit = QtWidgets.QTimeEdit(Form)
        self.timeEdit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.timeEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.timeEdit.setObjectName("timeEdit")
        self.gridLayout.addWidget(self.timeEdit, 1, 0, 1, 1)
        self.radioButton = QtWidgets.QRadioButton(Form)
        self.radioButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.gridLayout.addWidget(self.radioButton, 2, 0, 1, 1)
        self.timeEdit_2 = QtWidgets.QTimeEdit(Form)
        self.timeEdit_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.timeEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.timeEdit_2.setCurrentSection(QtWidgets.QDateTimeEdit.MinuteSection)
        self.timeEdit_2.setObjectName("timeEdit_2")
        self.gridLayout.addWidget(self.timeEdit_2, 1, 1, 1, 1)
        self.radioButton_2 = QtWidgets.QRadioButton(Form)
        self.radioButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.radioButton_2.setCheckable(True)
        self.radioButton_2.setObjectName("radioButton_2")
        self.gridLayout.addWidget(self.radioButton_2, 2, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 3, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setEnabled(False)
        self.gridLayout.addWidget(self.pushButton_2, 3, 1, 1, 1)

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(self.run)
        self.pushButton_2.clicked.connect(self.Stopesd)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.timeEdit, self.radioButton)
        Form.setTabOrder(self.radioButton, self.timeEdit_2)
        Form.setTabOrder(self.timeEdit_2, self.radioButton_2)
        Form.setTabOrder(self.radioButton_2, self.pushButton)
        Form.setTabOrder(self.pushButton, self.pushButton_2)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "TimeOff"))
        self.label.setText(_translate("Form", "АВТОВІДКЛЮЧЕННЯ"))
        self.timeEdit.setDisplayFormat(_translate("Form", "HH:mm"))
        self.radioButton.setText(_translate("Form", "в годинах"))
        self.timeEdit_2.setDisplayFormat(_translate("Form", "m"))
        self.radioButton_2.setText(_translate("Form", "в хвилинах"))
        self.pushButton.setText(_translate("Form", "ЗАПУСТИТИ"))
        self.pushButton_2.setText(_translate("Form", "ЗУПИНИТИ"))

    def run(self):
        if self.radioButton.isChecked():
            self.bool = True
            self.timer = QtCore.QTimer()
            self.timer.setInterval(60000)
            self.timer.setSingleShot(False)
            self.timer.timeout.connect(self.Ckloc)
            self.timer.start()
            self.pushButton.setEnabled(False)
            self.pushButton_2.setEnabled(True)
            self.radioButton.setEnabled(False)
            self.radioButton_2.setEnabled(False)
        else:
            self.bool = False
            self.tick = 0
            self.timer_1 = QtCore.QTimer()
            self.timer_1.setInterval(60000)
            self.timer_1.setSingleShot(False)
            self.timer_1.timeout.connect(self.Mins)
            self.timer_1.start()
            self.pushButton.setEnabled(False)
            self.pushButton_2.setEnabled(True)
            self.radioButton.setEnabled(False)
            self.radioButton_2.setEnabled(False)

    def Ckloc(self):
        if time.strftime("%H:%M") == self.timeEdit.text():
            subprocess.Popen("shutdown -s -t 0 -f", shell=True)

    def Mins(self):
        if int(self.timeEdit_2.text()) == self.tick:
            subprocess.Popen("shutdown -s -t 0 -f", shell=True)
        self.tick += 1

    def Stopesd(self):
        if self.bool:
            self.timer.stop()
            self.pushButton.setEnabled(True)
            self.pushButton_2.setEnabled(False)
            self.radioButton.setEnabled(True)
            self.radioButton_2.setEnabled(True)
        if not self.bool:
            self.timer_1.stop()
            self.pushButton.setEnabled(True)
            self.pushButton_2.setEnabled(False)
            self.radioButton.setEnabled(True)
            self.radioButton_2.setEnabled(True)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
