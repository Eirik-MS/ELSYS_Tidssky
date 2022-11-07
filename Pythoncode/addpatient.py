import sys
sys.path
sys.path.append('C:\\Users\\mgnso\\AppData\\Local\\Programs\\Python\\Python310\\lib\\site-packages')
from PyQt5 import QtCore, QtGui, QtWidgets

class Addpatient(QtWidgets.QFrame):
    def __init__(self, *args, **kwargs):

        QtWidgets.QFrame.__init__(self,*args,**kwargs)

        self.setGeometry(QtCore.QRect(10, 60, 604, 37))
        self.setMaximumSize(QtCore.QSize(16777215, 55))
        self.setStyleSheet("")
        self.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.setFrameShadow(QtWidgets.QFrame.Raised)
        self.setObjectName("addpatient")
        self.verticalLayout_72 = QtWidgets.QVBoxLayout(self)
        self.verticalLayout_72.setContentsMargins(0, 0, 0, 3)
        self.verticalLayout_72.setSpacing(0)
        self.verticalLayout_72.setObjectName("verticalLayout_72")
        self.mainframe = QtWidgets.QFrame(self)
        self.mainframe.setMinimumSize(QtCore.QSize(0, 30))
        self.mainframe.setMaximumSize(QtCore.QSize(16777215, 30))
        self.mainframe.setStyleSheet("background-color: rgba(255, 255, 255, 180); \n"
                                     "border-radius:10px;\n"
                                     "font: 12px \"Roboto Cn\";")
        self.mainframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mainframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainframe.setObjectName("mainframe")
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout(self.mainframe)
        self.horizontalLayout_24.setContentsMargins(10, 0, 10, 0)
        self.horizontalLayout_24.setSpacing(10)
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        self.check = QtWidgets.QCheckBox(self.mainframe)
        self.check.setMinimumSize(QtCore.QSize(30, 30))
        self.check.setMaximumSize(QtCore.QSize(13, 16777215))
        self.check.setStyleSheet("QCheckBox{background:none;}")
        self.check.setText("")
        self.check.setObjectName("check")
        self.horizontalLayout_24.addWidget(self.check)
        self.navn = QtWidgets.QLabel(self.mainframe)
        self.navn.setMinimumSize(QtCore.QSize(290, 0))
        font = QtGui.QFont()
        font.setFamily("Roboto Cn")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.navn.setFont(font)
        self.navn.setStyleSheet("background:none;")
        self.navn.setObjectName("navn")
        self.horizontalLayout_24.addWidget(self.navn)
        self.romlabel = QtWidgets.QLabel(self.mainframe)
        self.romlabel.setMaximumSize(QtCore.QSize(30, 16777215))
        font = QtGui.QFont()
        font.setFamily("Roboto Cn")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.romlabel.setFont(font)
        self.romlabel.setStyleSheet("font: 75 12px \"Roboto Cn\"; background:none;")
        self.romlabel.setObjectName("romlabel")
        self.horizontalLayout_24.addWidget(self.romlabel)
        self.rom = QtWidgets.QLabel(self.mainframe)
        self.rom.setMinimumSize(QtCore.QSize(90, 0))
        self.rom.setMaximumSize(QtCore.QSize(90, 16777215))
        self.rom.setStyleSheet("background:none;")
        self.rom.setObjectName("rom")
        self.horizontalLayout_24.addWidget(self.rom)
        self.tidlabel = QtWidgets.QLabel(self.mainframe)
        self.tidlabel.setMinimumSize(QtCore.QSize(20, 0))
        self.tidlabel.setMaximumSize(QtCore.QSize(30, 16777215))
        self.tidlabel.setStyleSheet("background:none;")
        self.tidlabel.setObjectName("tidlabel")
        self.horizontalLayout_24.addWidget(self.tidlabel)
        self.tid = QtWidgets.QLabel(self.mainframe)
        self.tid.setMinimumSize(QtCore.QSize(80, 0))
        self.tid.setStyleSheet("background:none;")
        self.tid.setObjectName("tid")
        self.horizontalLayout_24.addWidget(self.tid)
        self.verticalLayout_72.addWidget(self.mainframe)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.navn.setText(_translate("Form", "Pasientnavn"))
        self.romlabel.setText(_translate("Form", "Rom:"))
        self.rom.setText(_translate("Form", "PET-Scan"))
        self.tidlabel.setText(_translate("Form", "Kl.:"))
        self.tid.setText(_translate("Form", "12:45"))

