# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\svidl\OneDrive\שולחן העבודה\MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

import App
from PyQt5 import QtCore, QtGui, QtWidgets





class Ui_Form(object):

    def OpenWin(self):

        self.window = App.QtWidgets.QWidget()
        self.ui = App.Ui_Form()
        self.ui.setupUi(self.window)
        self.window.show()
        Form.setVisible(False)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1120, 863)
        font = QtGui.QFont()
        font.setFamily("century gothic")
        font.setPointSize(-1)
        Form.setFont(font)
        Form.setLayoutDirection(QtCore.Qt.RightToLeft)
        Form.setStyleSheet("*{\n"
"    font-family:century gothic;\n"
"    font-size:24px;\n"
"    \n"
"}\n"
"QFrame\n"
"{\n"
"    background:rgb(222, 222, 222);\n"
"}\n"
"#VidioButton\n"
"{\n"
"font-color:rgb(0, 255, 0);\n"
"background:rgb(255, 255, 255);    \n"
"border-radius:60px;\n"
"}\n"
"#InfoButton\n"
"{\n"
"\n"
"background:rgb(255, 255, 255);    \n"
"border-radius:60px;\n"
"}\n"
"\n"
"#StartButton\n"
"{\n"
"\n"
"background:rgb(107, 107, 107);    \n"
"border-radius:60px;\n"
"}\n"
"")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(260, 10, 671, 781))
        font = QtGui.QFont()
        font.setFamily("century gothic")
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.frame.setFont(font)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(150, 20, 381, 81))
        font = QtGui.QFont()
        font.setFamily("century gothic")
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("*{\n"
"    font-family:century gothic;\n"
"    font-size:35px;\n"
"    \n"
"}")
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setLineWidth(3)
        self.label.setObjectName("label")
        self.VidioButton = QtWidgets.QPushButton(self.frame)
        self.VidioButton.setGeometry(QtCore.QRect(150, 150, 361, 121))
        self.VidioButton.setObjectName("VidioButton")
        self.InfoButton = QtWidgets.QPushButton(self.frame)
        self.InfoButton.setGeometry(QtCore.QRect(150, 310, 361, 121))
        self.InfoButton.setObjectName("InfoButton")
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(210, 280, 241, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.frame)
        self.calendarWidget.setGeometry(QtCore.QRect(30, 460, 601, 236))
        self.calendarWidget.setAutoFillBackground(True)
        self.calendarWidget.setObjectName("calendarWidget")
        self.line_2 = QtWidgets.QFrame(self.frame)
        self.line_2.setGeometry(QtCore.QRect(210, 440, 261, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.StartButton = QtWidgets.QPushButton(Form)
        self.StartButton.setGeometry(QtCore.QRect(520, 720, 131, 141))
        self.StartButton.setAcceptDrops(False)
        self.StartButton.setAutoFillBackground(False)
        self.StartButton.setAutoRepeat(False)
        self.StartButton.setFlat(False)
        self.StartButton.setObjectName("StartButton")

        self.StartButton.clicked.connect(self.OpenWin)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Fractography Anlyzer"))
        self.VidioButton.setText(_translate("Form", "video guide"))
        self.InfoButton.setText(_translate("Form", "Info"))
        self.StartButton.setText(_translate("Form", "START"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
