# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\svidl\OneDrive\שולחן העבודה\AppWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

import main
import main2
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QFileDialog
from tkinter.filedialog import askopenfilename
from tkinter import *
from tkinter import messagebox
from PIL import Image
from pylab import *
import numpy as np
import cv2

filename= ''


def ShowPic():
        Ui_Form.OpenDialog()




class Ui_Form(object):






    def UploadImage(self):
            self.OpenDialog()

    def OpenDialog(self):
            global filename
            filename = QFileDialog.getOpenFileName()
            path= filename[0]
            print(filename)
            main.LoadImg(path)
            pixmap = QPixmap(path)
            self.label_2.setPixmap(QPixmap(pixmap))

    def ShowPic(self):
            ref = main.select()
            reff= 'C:/Users/svidl/PycharmProjects/FinalProject/' + ref
            pixmap2 = QPixmap(reff)
            self.label_2.setPixmap(QPixmap(pixmap2))


    def MaskLoad(self):
            main.load_mask()

    def MaskApp(self):

            ref = main.apply_mask()

            print(ref)
            reff = 'C:/Users/svidl/PycharmProjects/FinalProject/' + ref
            pixmap2 = QPixmap(reff)

            self.label_2.setPixmap(QPixmap(pixmap2))

    def Direction(self):
            main.line_detect()
            reff = 'C:/Users/svidl/PycharmProjects/FinalProject/' + 'images/lines'
            pixmap2 = QPixmap(reff)

            self.label_2.setPixmap(QPixmap(pixmap2))

    def ClearImg(self):
            self.label_2.clear()


    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1122, 867)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(-10, -10, 1201, 891))
        self.frame.setStyleSheet("\n"
"*{\n"
"background-color:rgb(226, 226, 226);\n"
"}\n"
"#frame_2\n"
"{\n"
"background-color:rgb(255, 255, 255);\n"
"border-radius:60px;\n"
"}\n"
"#ImageUp\n"
"{\n"
"background-color:rgb(222, 222, 222);\n"
"border-radius:20px;\n"
"}\n"
"#label\n"
"{\n"
"background-color:rgb(255, 255, 255);\n"
"}\n"
"#line2\n"
"{\n"
"background-color:rgb(255, 255, 255);\n"
"}\n"
"#MaskUp\n"
"{\n"
"background-color:rgb(222, 222, 222);\n"
"border-radius:20px;\n"
"}\n"
"#ApllyMask\n"
"{\n"
"background-color:rgb(222, 222, 222);\n"
"border-radius:20px;\n"
"}\n"
"#SelectCrack\n"
"{\n"
"background-color:rgb(222, 222, 222);\n"
"border-radius:20px;\n"
"}\n"
"#CrackDirection\n"
"{\n"
"background-color:rgb(222, 222, 222);\n"
"border-radius:20px;\n"
"}\n"
"#Distance\n"
"{\n"
"background-color:rgb(222, 222, 222);\n"
"border-radius:20px;\n"
"}\n"
"#Filter\n"
"{\n"
"background-color:rgb(222, 222, 222);\n"
"border-radius:20px;\n"
"}\n"
"#Save\n"
"{\n"
"background-color:rgb(222, 222, 222);\n"
"border-radius:20px;\n"
"}\n"
"#Print\n"
"{\n"
"background-color:rgb(222, 222, 222);\n"
"border-radius:20px;\n"
"}\n"
"#Clear\n"
"{\n"
"background-color:rgb(222, 222, 222);\n"
"border-radius:20px;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(900, 40, 231, 831))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(9)
        self.frame_2.setFont(font)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.ImageUp = QtWidgets.QPushButton(self.frame_2)
        self.ImageUp.setGeometry(QtCore.QRect(40, 80, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(9)
        self.ImageUp.setFont(font)
        self.ImageUp.setObjectName("ImageUp")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(90, 20, 55, 16))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.line2 = QtWidgets.QFrame(self.frame_2)
        self.line2.setGeometry(QtCore.QRect(40, 50, 161, 16))
        self.line2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line2.setObjectName("line2")
        self.line_2 = QtWidgets.QFrame(self.frame_2)
        self.line_2.setGeometry(QtCore.QRect(60, 140, 118, 3))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.MaskUp = QtWidgets.QPushButton(self.frame_2)
        self.MaskUp.setGeometry(QtCore.QRect(40, 170, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(9)
        self.MaskUp.setFont(font)
        self.MaskUp.setObjectName("MaskUp")
        self.ApllyMask = QtWidgets.QPushButton(self.frame_2)
        self.ApllyMask.setGeometry(QtCore.QRect(42, 250, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(9)
        self.ApllyMask.setFont(font)
        self.ApllyMask.setObjectName("ApllyMask")
        self.SelectCrack = QtWidgets.QPushButton(self.frame_2)
        self.SelectCrack.setGeometry(QtCore.QRect(40, 340, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(9)
        self.SelectCrack.setFont(font)
        self.SelectCrack.setObjectName("SelectCrack")
        self.line_3 = QtWidgets.QFrame(self.frame_2)
        self.line_3.setGeometry(QtCore.QRect(60, 310, 118, 3))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.CrackDirection = QtWidgets.QPushButton(self.frame_2)
        self.CrackDirection.setGeometry(QtCore.QRect(40, 410, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(9)
        self.CrackDirection.setFont(font)
        self.CrackDirection.setObjectName("CrackDirection")
        self.Distance = QtWidgets.QPushButton(self.frame_2)
        self.Distance.setGeometry(QtCore.QRect(40, 480, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(9)
        self.Distance.setFont(font)
        self.Distance.setObjectName("Distance")
        self.Filter = QtWidgets.QPushButton(self.frame_2)
        self.Filter.setGeometry(QtCore.QRect(40, 550, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(9)
        self.Filter.setFont(font)
        self.Filter.setObjectName("Filter")
        self.line_4 = QtWidgets.QFrame(self.frame_2)
        self.line_4.setGeometry(QtCore.QRect(60, 610, 118, 3))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.Save = QtWidgets.QPushButton(self.frame_2)
        self.Save.setGeometry(QtCore.QRect(40, 640, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(9)
        self.Save.setFont(font)
        self.Save.setObjectName("Save")
        self.Print = QtWidgets.QPushButton(self.frame_2)
        self.Print.setGeometry(QtCore.QRect(42, 710, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(9)
        self.Print.setFont(font)
        self.Print.setObjectName("Print")
        self.Clear = QtWidgets.QPushButton(self.frame_2)
        self.Clear.setGeometry(QtCore.QRect(60, 780, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(9)
        self.Clear.setFont(font)
        self.Clear.setObjectName("Clear")
        self.line_5 = QtWidgets.QFrame(self.frame_2)
        self.line_5.setGeometry(QtCore.QRect(60, 770, 118, 3))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(880, 80, 20, 741))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(30, 30, 841, 831))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")

        self.ImageUp.clicked.connect(self.UploadImage)

        self.SelectCrack.clicked.connect(self.ShowPic)

        self.MaskUp.clicked.connect(self.MaskLoad)

        self.ApllyMask.clicked.connect(self.MaskApp)

        self.CrackDirection.clicked.connect(self.Direction)

        self.Clear.clicked.connect(self.ClearImg)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.ImageUp.setText(_translate("Form", "Upload Image"))
        self.label.setText(_translate("Form", "Tools"))
        self.MaskUp.setText(_translate("Form", "Upload Mask"))
        self.ApllyMask.setText(_translate("Form", "Aplly Mask"))
        self.SelectCrack.setText(_translate("Form", "Select Crack"))
        self.CrackDirection.setText(_translate("Form", "figure out Direction"))
        self.Distance.setText(_translate("Form", "Distances"))
        self.Filter.setText(_translate("Form", "Aplly Filter"))
        self.Save.setText(_translate("Form", "Save"))
        self.Print.setText(_translate("Form", "Print"))
        self.Clear.setText(_translate("Form", "Clear"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())


