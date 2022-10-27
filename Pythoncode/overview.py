import sys
from addpatient import Addpatient
sys.path
sys.path.append('C:\\Users\\mgnso\\AppData\\Local\\Programs\\Python\\Python310\\lib\\site-packages')
from PyQt5 import QtCore, QtGui, QtWidgets


class Overview(QtWidgets.QFrame):
    def __init__(self, *args, **kwargs):
        QtWidgets.QFrame.__init__(self, *args, **kwargs)
        self.setObjectName("MainWindow")

        self.setGeometry(QtCore.QRect(20, 230, 900, 300))
        self.setMinimumSize(QtCore.QSize(900, 300))
        self.setMaximumSize(QtCore.QSize(16777215, 8765))
        self.setStyleSheet("QFrame#MainWindow    {background-color: rgba(0, 0, 0, 100);        border-radius:15px;}")
        self.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.setFrameShadow(QtWidgets.QFrame.Raised)
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")
        self.timeplan = QtWidgets.QFrame(self)
        self.timeplan.setMaximumSize(QtCore.QSize(16777215, 40))
        self.timeplan.setStyleSheet("background-color:rgb(0,0,0,80); border-radius:15px;")
        self.timeplan.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.timeplan.setFrameShadow(QtWidgets.QFrame.Raised)
        self.timeplan.setObjectName("timeplan")
        self.timeplanLay = QtWidgets.QVBoxLayout(self.timeplan)
        self.timeplanLay.setContentsMargins(0, 0, 0, 0)
        self.timeplanLay.setSpacing(0)
        self.timeplanLay.setObjectName("timeplanLay")
        self.timeplanlabel = QtWidgets.QLabel(self.timeplan)
        self.timeplanlabel.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.timeplanlabel.setFont(font)
        self.timeplanlabel.setStyleSheet("font-size:25px; background:none;\n"
"color: rgba(255, 255, 255, 200);")
        self.timeplanlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.timeplanlabel.setObjectName("timeplanlabel")
        self.timeplanLay.addWidget(self.timeplanlabel)
        self.verticalLayout.addWidget(self.timeplan)
        self.contents = QtWidgets.QFrame(self)
        self.contents.setMinimumSize(QtCore.QSize(644, 0))
        self.contents.setStyleSheet("QFrame#frame_3                                  {background-color:rgb(0,0,0,80);}\n"
"QScrollBar::handle:vertical:hover         {background-color: rgb(189, 223, 246, 180);}\n"
"QScrollBar::handle:vertical:pressed     {background-color: rgba(189, 223, 246, 100);}\n"
"QScrollBar::sub-line:vertical:hover     {background-color: rgb(255, 0, 127, 0);}\n"
"QScrollBar::sub-line:vertical:pressed     {background-color: rgb(185, 0, 92, 0);}\n"
"QScrollBar::add-line:vertical:hover     {background-color: rgb(255, 0, 127, 0);}\n"
"QScrollBar::add-line:vertical:pressed {background-color: rgb(185, 0, 92, 0);}\n"
"QScrollBar::sub-page:vertical             {background-color: rgb(255, 85,0,0);}\n"
"QScrollBar::add-page:vertical             {background-color:rgb(0,0,123,0);}\n"
"QScrollBar::sub-line:vertical                 {background-color: rgb(59, 59, 90, 0);    height: 0px;                border: none;}        \n"
"QScrollBar::add-line:vertical                {background-color: rgb(59, 59, 90, 0);    height: 0px;                border: none;}\n"
"QScrollBar::handle:vertical                         {background-color: rgba(0, 0, 0, 120);    min-height: 30px;    border-radius: 4px;}\n"
"QScrollBar:vertical                                   {background: rgb(45, 45, 68, 0);            width: 8px;                border: none;                \n"
"                                                             margin: 15px 0 15px 0;                                                            border-radius: 0px;}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical     {background: none;}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical         {background: none;}\n"
"\n"
"")
        self.contents.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.contents.setFrameShadow(QtWidgets.QFrame.Raised)
        self.contents.setObjectName("contents")
        self.contentsLay = QtWidgets.QVBoxLayout(self.contents)
        self.contentsLay.setContentsMargins(0, 0, 0, 0)
        self.contentsLay.setObjectName("contentsLay")
        self.scrollarea = QtWidgets.QScrollArea(self.contents)
        self.scrollarea.setStyleSheet("QScrollArea{background-color:rgb(0,0,0,0); border-radius:15px; border: 1px solid;}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:verticall{background-color:rgb(0,0,0,0);}")
        self.scrollarea.setWidgetResizable(True)
        self.scrollarea.setObjectName("scrollarea")
        self.scrollwidget = QtWidgets.QWidget()
        self.scrollwidget.setGeometry(QtCore.QRect(0, 0, 880, 149))
        self.scrollwidget.setStyleSheet("background-color:rgb(0,0,0,0);")
        self.scrollwidget.setObjectName("scrollwidget")
        self.scrollwidgetLay = QtWidgets.QVBoxLayout(self.scrollwidget)
        self.scrollwidgetLay.setContentsMargins(0, 0, 0, 0)
        self.scrollwidgetLay.setSpacing(0)
        self.scrollwidgetLay.setObjectName("scrollwidgetLay")
        self.scrollframe = QtWidgets.QFrame(self.scrollwidget)
        self.scrollframe.setMinimumSize(QtCore.QSize(0, 0))
        self.scrollframe.setStyleSheet("QFrame#scrollframe{background:none;}")
        self.scrollframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.scrollframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.scrollframe.setObjectName("scrollframe")
        self.scrollframeLay = QtWidgets.QVBoxLayout(self.scrollframe)
        self.scrollframeLay.setContentsMargins(15, 3, 15, 3)
        self.scrollframeLay.setSpacing(3)
        self.scrollframeLay.setObjectName("scrollframeLay")
        self.scrollwidgetLay.addWidget(self.scrollframe)
        self.scrollarea.setWidget(self.scrollwidget)
        self.contentsLay.addWidget(self.scrollarea)
        self.inputs = QtWidgets.QFrame(self.contents)
        self.inputs.setMinimumSize(QtCore.QSize(0, 50))
        self.inputs.setStyleSheet("background:none;    border-radius:10px; \n"
"font: 8pt \"Roboto Cn\";")
        self.inputs.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.inputs.setFrameShadow(QtWidgets.QFrame.Raised)
        self.inputs.setObjectName("inputs")
        self.inputsLay = QtWidgets.QHBoxLayout(self.inputs)
        self.inputsLay.setContentsMargins(0, 0, 0, 0)
        self.inputsLay.setSpacing(30)
        self.inputsLay.setObjectName("inputsLay")
        self.navnframe = QtWidgets.QFrame(self.inputs)
        self.navnframe.setMinimumSize(QtCore.QSize(100, 0))
        self.navnframe.setStyleSheet("")
        self.navnframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.navnframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.navnframe.setObjectName("navnframe")
        self.navnframeLay = QtWidgets.QVBoxLayout(self.navnframe)
        self.navnframeLay.setContentsMargins(0, 0, 0, 0)
        self.navnframeLay.setSpacing(0)
        self.navnframeLay.setObjectName("navnframeLay")
        self.navnlabel = QtWidgets.QLabel(self.navnframe)
        self.navnlabel.setStyleSheet("")
        self.navnlabel.setObjectName("navnlabel")
        self.navnframeLay.addWidget(self.navnlabel)
        self.navninput = QtWidgets.QLineEdit(self.navnframe)
        self.navninput.setMinimumSize(QtCore.QSize(0, 40))
        self.navninput.setStyleSheet("")
        self.navninput.setText("")
        self.navninput.setAlignment(QtCore.Qt.AlignCenter)
        self.navninput.setPlaceholderText("")
        self.navninput.setObjectName("navninput")
        self.navnframeLay.addWidget(self.navninput)
        self.inputsLay.addWidget(self.navnframe)
        self.tidframe = QtWidgets.QFrame(self.inputs)
        self.tidframe.setMinimumSize(QtCore.QSize(100, 0))
        self.tidframe.setStyleSheet("")
        self.tidframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tidframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tidframe.setObjectName("tidframe")
        self.tidframeLay = QtWidgets.QVBoxLayout(self.tidframe)
        self.tidframeLay.setContentsMargins(0, 0, 0, 0)
        self.tidframeLay.setSpacing(0)
        self.tidframeLay.setObjectName("tidframeLay")
        self.tidlabel = QtWidgets.QLabel(self.tidframe)
        self.tidlabel.setStyleSheet("")
        self.tidlabel.setObjectName("tidlabel")
        self.tidframeLay.addWidget(self.tidlabel)
        self.tidinput = QtWidgets.QLineEdit(self.tidframe)
        self.tidinput.setMinimumSize(QtCore.QSize(0, 40))
        self.tidinput.setStyleSheet("")
        self.tidinput.setText("")
        self.tidinput.setAlignment(QtCore.Qt.AlignCenter)
        self.tidinput.setPlaceholderText("")
        self.tidinput.setObjectName("tidinput")
        self.tidframeLay.addWidget(self.tidinput)
        self.inputsLay.addWidget(self.tidframe)
        self.romframe = QtWidgets.QFrame(self.inputs)
        self.romframe.setMinimumSize(QtCore.QSize(100, 0))
        self.romframe.setStyleSheet("")
        self.romframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.romframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.romframe.setObjectName("romframe")
        self.romframeLay = QtWidgets.QVBoxLayout(self.romframe)
        self.romframeLay.setContentsMargins(0, 0, 0, 0)
        self.romframeLay.setSpacing(0)
        self.romframeLay.setObjectName("romframeLay")
        self.romlabel = QtWidgets.QLabel(self.romframe)
        self.romlabel.setStyleSheet("")
        self.romlabel.setObjectName("romlabel")
        self.romframeLay.addWidget(self.romlabel)
        self.rominput = QtWidgets.QComboBox(self.romframe)
        self.rominput.setMinimumSize(QtCore.QSize(0, 40))
        self.rominput.setStyleSheet("")
        self.rominput.setObjectName("rominput")
        self.rominput.addItem("")
        self.rominput.addItem("")
        self.rominput.addItem("")
        self.rominput.addItem("")
        self.rominput.addItem("")
        self.romframeLay.addWidget(self.rominput)
        self.inputsLay.addWidget(self.romframe)
        self.contentsLay.addWidget(self.inputs)
        self.knapper = QtWidgets.QFrame(self.contents)
        self.knapper.setMinimumSize(QtCore.QSize(0, 30))
        self.knapper.setMaximumSize(QtCore.QSize(16777215, 30))
        self.knapper.setStyleSheet("QPushButton                {border:1px solid;        border-color: rgb(39, 39, 39);        border-radius:0px;\n"
"                                     border-radius:10px;    background-color: rbg(0,0,0,80);    color: rgb(217, 217, 217);}\n"
"QPushButton:hover        {background-color: rgba(0, 0, 0, 120);}\n"
"QPushButton:pressed {background-color: rgba(0, 0, 0, 200);}")
        self.knapper.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.knapper.setFrameShadow(QtWidgets.QFrame.Raised)
        self.knapper.setObjectName("knapper")
        self.knapperLay = QtWidgets.QHBoxLayout(self.knapper)
        self.knapperLay.setContentsMargins(0, 0, 0, 0)
        self.knapperLay.setSpacing(4)
        self.knapperLay.setObjectName("knapperLay")
        self.fjern = QtWidgets.QPushButton(self.knapper)
        self.fjern.setMinimumSize(QtCore.QSize(70, 25))
        self.fjern.setStyleSheet("")
        self.fjern.setObjectName("fjern")
        self.knapperLay.addWidget(self.fjern)
        self.settinn = QtWidgets.QPushButton(self.knapper)
        self.settinn.setMinimumSize(QtCore.QSize(70, 25))
        self.settinn.setStyleSheet("")
        self.settinn.setObjectName("settinn")
        self.knapperLay.addWidget(self.settinn)
        self.bytt = QtWidgets.QPushButton(self.knapper)
        self.bytt.setMinimumSize(QtCore.QSize(70, 25))
        self.bytt.setStyleSheet("")
        self.bytt.setObjectName("bytt")
        self.knapperLay.addWidget(self.bytt)
        self.leggtil = QtWidgets.QPushButton(self.knapper)
        self.leggtil.setMinimumSize(QtCore.QSize(70, 25))
        self.leggtil.setStyleSheet("")
        self.leggtil.setObjectName("leggtil")
        self.knapperLay.addWidget(self.leggtil)
        self.contentsLay.addWidget(self.knapper)
        self.verticalLayout.addWidget(self.contents)

        self.leggtil.clicked.connect(lambda:self.addPatient(self.navninput.text(), self.tidinput.text(), self.rominput.currentText()))


        self.retranslateUi(self)

        QtCore.QMetaObject.connectSlotsByName(self)

    def addPatient(self, name, time, room):

        patient = Addpatient(self.scrollframe)
        _translate = QtCore.QCoreApplication.translate
        patient.navn.setText(_translate("Form", f"{name}"))
        patient.tid.setText(_translate("Form", f"{time}"))
        patient.rom.setText(_translate("Form", f"{room}"))
        self.scrollframeLay.addWidget(patient)
        self.navninput.setText('')
        self.tidinput.setText('')


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.timeplanlabel.setText(_translate("MainWindow", "Timeplan"))
        self.navnlabel.setText(_translate("MainWindow", "   Navn:"))
        self.tidlabel.setText(_translate("MainWindow", "   Tid:"))
        self.romlabel.setText(_translate("MainWindow", "   Rom:"))
        self.rominput.setItemText(0, _translate("MainWindow", "1"))
        self.rominput.setItemText(1, _translate("MainWindow", "2"))
        self.rominput.setItemText(2, _translate("MainWindow", "3"))
        self.rominput.setItemText(3, _translate("MainWindow", "4"))
        self.rominput.setItemText(4, _translate("MainWindow", "PET-Scan"))
        self.fjern.setToolTip(_translate("MainWindow", "Fjern markert(e) pasienter fra timeplanen."))
        self.fjern.setText(_translate("MainWindow", "Fjern pasient:"))
        self.settinn.setToolTip(_translate("MainWindow", "Sett pasient inn midt i planen. Fører pasienten frem i køen og forskyver behandlingstidspunktene til pasientene bak i køen."))
        self.settinn.setText(_translate("MainWindow", "Sett inn pasient:"))
        self.bytt.setToolTip(_translate("MainWindow", "Bytt timeplanene til to pasienter. Merk: kun to pasienter kan byttes om gangen."))
        self.bytt.setText(_translate("MainWindow", "Bytt pasienter:"))
        self.leggtil.setToolTip(_translate("MainWindow", "Legger til en pasient bakerst i timeplanen."))
        self.leggtil.setText(_translate("MainWindow", "Legg til pasient:"))
import Bakgrunnsbilde


