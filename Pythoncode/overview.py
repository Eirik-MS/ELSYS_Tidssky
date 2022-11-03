from addpatient import Addpatient
from PyQt5 import QtCore, QtGui, QtWidgets
from Classes import Patients
from room import Room


class Overview(QtWidgets.QFrame):

    # Initializing variables and functions
    def __init__(self, *args, **kwargs):

        # Create global translate protocol:
        self._translate = QtCore.QCoreApplication.translate

        # Create the patient dictionary:
        self.patients = Patients()

        # Create the mainframe
        QtWidgets.QFrame.__init__(self, *args, **kwargs)

        # Configure the Overview object:
        self.createOverview(self, *args, **kwargs)

        # Assign functions to buttons:
        self.leggtil.clicked.connect(           lambda: self.addPatient(
                                                            self.navninput.text(),
                                                            self.tidinput.text(),
                                                            self.rominput.currentText()))
        self.navninput.returnPressed.connect(   lambda: self.addPatient(
                                                            self.navninput.text(),
                                                            self.tidinput.text(),
                                                            self.rominput.currentText()))
        self.tidinput.returnPressed.connect(    lambda: self.navninput.setFocus())
        self.tidinput.returnPressed.connect(    lambda: self.addPatient(
                                                            self.navninput.text(),
                                                            self.tidinput.text(),
                                                            self.rominput.currentText()))

        self.fjern.clicked.connect(             lambda: self.deletePatient(self.navninput.text()))
        self.settinn.clicked.connect(           lambda: self.addTime(self.navninput.text(), self.tidinput.text()))

    # Configure the contents of the Overview object
    def createOverview(self, *args, **kwargs):

        # Configure the main frame
        self.setObjectName("MainWindow")
        self.setGeometry(QtCore.QRect(20, 230, 900, 300))
        self.setMinimumSize(QtCore.QSize(900, 300))
        self.setMaximumSize(QtCore.QSize(16777215, 8765))
        self.setStyleSheet("QFrame#MainWindow    {background-color: rgba(0, 0, 0, 100);        border-radius:15px;}")
        self.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.setFrameShadow(QtWidgets.QFrame.Raised)
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")

        # Create the frame fra the schedule
        self.timeplan = QtWidgets.QFrame(self)
        self.timeplan.setMaximumSize(QtCore.QSize(16777215, 40))
        self.timeplan.setStyleSheet("background-color:rgb(0,0,0,80); border-radius:15px;")
        self.timeplan.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.timeplan.setFrameShadow(QtWidgets.QFrame.Raised)
        self.timeplan.setObjectName("timeplan")

        # Configure the label for the schedule frame
        self.timeplanLay = QtWidgets.QVBoxLayout(self.timeplan)
        self.timeplanLay.setContentsMargins(0, 0, 0, 0)
        self.timeplanLay.setSpacing(0)
        self.timeplanLay.setObjectName("timeplanLay")

        # Create the label that says "Timeplan"
        self.timeplanlabel = QtWidgets.QLabel(self.timeplan)
        self.timeplanlabel.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.timeplanlabel.setFont(font)
        self.timeplanlabel.setStyleSheet("font-size:25px; background:none;  color: rgba(255, 255, 255, 200);")
        self.timeplanlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.timeplanlabel.setObjectName("timeplanlabel")
        self.timeplanLay.addWidget(self.timeplanlabel)
        self.verticalLayout.addWidget(self.timeplan)

        # Create the frame that will display the patients in the schedule
        self.contents = QtWidgets.QFrame(self)
        self.contents.setMinimumSize(QtCore.QSize(644, 0))
        self.contents.setStyleSheet("""
                                    QFrame#frame_3                             {background-color:rgb(0,0,0,80);}
                                    QScrollBar::handle:vertical:hover          {background-color: rgb(189, 223, 246, 180);}
                                    QScrollBar::handle:vertical:pressed        {background-color: rgba(189, 223, 246, 100);}
                                    QScrollBar::sub-line:vertical:hover        {background-color: rgb(255, 0, 127, 0);}
                                    QScrollBar::sub-line:vertical:pressed      {background-color: rgb(185, 0, 92, 0);}
                                    QScrollBar::add-line:vertical:hover        {background-color: rgb(255, 0, 127, 0);}
                                    QScrollBar::add-line:vertical:pressed      {background-color: rgb(185, 0, 92, 0);}
                                    QScrollBar::sub-page:vertical              {background-color: rgb(255, 85,0,0);}
                                    QScrollBar::add-page:vertical              {background-color:rgb(0,0,123,0);}
                                    QScrollBar::sub-line:vertical              {background-color: rgb(59, 59, 90, 0);    height: 0px;         border: none;}        
                                    QScrollBar::add-line:vertical              {background-color: rgb(59, 59, 90, 0);    height: 0px;         border: none;}
                                    QScrollBar::handle:vertical                {background-color: rgba(0, 0, 0, 120);    min-height: 30px;    border-radius: 4px;}
                                    QScrollBar:vertical                        {background: rgb(45, 45, 68, 0);          width: 8px;          border: none;                
                                                                                margin: 15px 0 15px 0;                                        border-radius: 0px;}
                                    
                                    QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical  {background: none;}
                                    QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical    {background: none;}
                                    """)

        self.contents.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.contents.setFrameShadow(QtWidgets.QFrame.Raised)
        self.contents.setObjectName("contents")

        # Configure the layout for the content frame
        self.contentsLay = QtWidgets.QVBoxLayout(self.contents)
        self.contentsLay.setContentsMargins(0, 0, 0, 0)
        self.contentsLay.setObjectName("contentsLay")

        # Create the scrolling area
        self.scrollarea = QtWidgets.QScrollArea(self.contents)
        self.scrollarea.setStyleSheet("""QScrollArea    {background-color:rgb(0,0,0,0);     border-radius:15px;     border: 1px solid;}
                                         QScrollBar::add-page:vertical, QScrollBar::sub-page:verticall              {background-color:rgb(0,0,0,0);}""")
        self.scrollarea.setWidgetResizable(True)
        self.scrollarea.setObjectName("scrollarea")

        # Create the scrolling widget
        self.scrollwidget = QtWidgets.QWidget()
        self.scrollwidget.setGeometry(QtCore.QRect(0, 0, 880, 149))
        self.scrollwidget.setStyleSheet("background-color:rgb(0,0,0,0);")
        self.scrollwidget.setObjectName("scrollwidget")

        # Create layout for scrolling wisget
        self.scrollwidgetLay = QtWidgets.QVBoxLayout(self.scrollwidget)
        self.scrollwidgetLay.setContentsMargins(0, 0, 0, 0)
        self.scrollwidgetLay.setSpacing(0)
        self.scrollwidgetLay.setObjectName("scrollwidgetLay")

        # Create the scrolling frame
        self.scrollframe = QtWidgets.QFrame(self.scrollwidget)
        self.scrollframe.setMinimumSize(QtCore.QSize(0, 0))
        self.scrollframe.setStyleSheet("QFrame#scrollframe{background:none;}")
        self.scrollframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.scrollframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.scrollframe.setObjectName("scrollframe")

        # Create the scrolling frame layout
        self.scrollframeLay = QtWidgets.QVBoxLayout(self.scrollframe)
        self.scrollframeLay.setContentsMargins(15, 8, 15, 8)
        self.scrollframeLay.setSpacing(3)
        self.scrollframeLay.addItem(QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding))
        self.scrollframeLay.setObjectName("scrollframeLay")
        self.scrollframeLay.setAlignment(QtCore.Qt.AlignTop)
        self.scrollwidgetLay.addWidget(self.scrollframe)
        self.scrollarea.setWidget(self.scrollwidget)
        self.contentsLay.addWidget(self.scrollarea)

        # Create the frame with the input widgets
        self.inputs = QtWidgets.QFrame(self.contents)
        self.inputs.setMinimumSize(QtCore.QSize(0, 50))
        self.inputs.setStyleSheet("background:none;    border-radius:10px; font: 8pt \"Roboto Cn\";")
        self.inputs.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.inputs.setFrameShadow(QtWidgets.QFrame.Raised)
        self.inputs.setObjectName("inputs")

        # Configure the layout for the input frame
        self.inputsLay = QtWidgets.QHBoxLayout(self.inputs)
        self.inputsLay.setContentsMargins(0, 0, 0, 0)
        self.inputsLay.setSpacing(30)
        self.inputsLay.setObjectName("inputsLay")

        # Configure the name input
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

######## Create the name input widget
        self.navninput = QtWidgets.QLineEdit(self.navnframe)
        self.navninput.setMinimumSize(QtCore.QSize(0, 40))
        self.navninput.setStyleSheet("")
        self.navninput.setText("")
        self.navninput.setAlignment(QtCore.Qt.AlignCenter)
        self.navninput.setPlaceholderText("")
        self.navninput.setObjectName("navninput")
        self.navnframeLay.addWidget(self.navninput)
        self.inputsLay.addWidget(self.navnframe)

        # Configure the time input
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

######## Create the time input
        self.tidinput = QtWidgets.QLineEdit(self.tidframe)
        self.tidinput.setMinimumSize(QtCore.QSize(0, 40))
        self.tidinput.setStyleSheet("")
        self.tidinput.setText("")
        self.tidinput.setInputMask("99:99")
        self.tidinput.setAlignment(QtCore.Qt.AlignCenter)
        self.tidinput.setPlaceholderText("")
        self.tidinput.setObjectName("tidinput")
        self.tidframeLay.addWidget(self.tidinput)
        self.inputsLay.addWidget(self.tidframe)

        # Configure the room input
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

######## Create the room input widget
        self.rominput = QtWidgets.QComboBox(self.romframe)
        self.rominput.setMinimumSize(QtCore.QSize(0, 40))
        self.rominput.setStyleSheet("")
        self.rominput.setObjectName("rominput")

        # Add items to the dropdown box
        self.rominput.addItem("")
        self.rominput.addItem("")
        self.rominput.addItem("")
        self.rominput.addItem("")
        self.rominput.addItem("")
        self.romframeLay.addWidget(self.rominput)
        self.inputsLay.addWidget(self.romframe)
        self.contentsLay.addWidget(self.inputs)

        # Configure the buttons
        self.knapper = QtWidgets.QFrame(self.contents)
        self.knapper.setMinimumSize(QtCore.QSize(0, 30))
        self.knapper.setMaximumSize(QtCore.QSize(16777215, 30))
        self.knapper.setStyleSheet("""
                                        QPushButton                 {border:1px solid;        border-color: rgb(39, 39, 39);        border-radius:0px;
                                                                     border-radius:10px;      background-color: rbg(0,0,0,80);      color: rgb(217, 217, 217);}
                                        QPushButton:hover           {background-color: rgba(0, 0, 0, 120);}
                                        QPushButton:pressed         {background-color: rgba(0, 0, 0, 200);}
                                   """)

        self.knapper.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.knapper.setFrameShadow(QtWidgets.QFrame.Raised)
        self.knapper.setObjectName("knapper")
        self.knapperLay = QtWidgets.QHBoxLayout(self.knapper)
        self.knapperLay.setContentsMargins(0, 0, 0, 0)
        self.knapperLay.setSpacing(4)
        self.knapperLay.setObjectName("knapperLay")

######## Create the remove button
        self.fjern = QtWidgets.QPushButton(self.knapper)
        self.fjern.setMinimumSize(QtCore.QSize(70, 25))
        self.fjern.setStyleSheet("")
        self.fjern.setObjectName("fjern")
        self.knapperLay.addWidget(self.fjern)

######## Create the insert button
        self.settinn = QtWidgets.QPushButton(self.knapper)
        self.settinn.setMinimumSize(QtCore.QSize(70, 25))
        self.settinn.setStyleSheet("")
        self.settinn.setObjectName("settinn")
        self.knapperLay.addWidget(self.settinn)

######## Create the switch button
        self.bytt = QtWidgets.QPushButton(self.knapper)
        self.bytt.setMinimumSize(QtCore.QSize(70, 25))
        self.bytt.setStyleSheet("")
        self.bytt.setObjectName("bytt")
        self.knapperLay.addWidget(self.bytt)

######## Create the add button
        self.leggtil = QtWidgets.QPushButton(self.knapper)
        self.leggtil.setMinimumSize(QtCore.QSize(70, 25))
        self.leggtil.setStyleSheet("")
        self.leggtil.setObjectName("leggtil")
        self.knapperLay.addWidget(self.leggtil)

        # Add the buttons to the main layout
        self.contentsLay.addWidget(self.knapper)
        self.verticalLayout.addWidget(self.contents)

        # Apply text

        self.timeplanlabel.setText(self._translate("MainWindow", "Timeplan"))
        self.navnlabel.setText(self._translate("MainWindow", "   Navn:"))
        self.tidlabel.setText(self._translate("MainWindow", "   Tid:"))
        self.romlabel.setText(self._translate("MainWindow", "   Rom:"))
        self.rominput.setItemText(0, self._translate("MainWindow", "1"))
        self.rominput.setItemText(1, self._translate("MainWindow", "2"))
        self.rominput.setItemText(2, self._translate("MainWindow", "3"))
        self.rominput.setItemText(3, self._translate("MainWindow", "4"))
        self.rominput.setItemText(4, self._translate("MainWindow", "PET-Scan"))
        self.fjern.setToolTip(self._translate("MainWindow", "Fjern markert(e) pasienter fra timeplanen."))
        self.fjern.setText(self._translate("MainWindow", "Fjern pasient:"))
        self.settinn.setToolTip(self._translate("MainWindow",
                                                "Sett pasient inn midt i planen. Fører pasienten frem i køen og forskyver behandlingstidspunktene til pasientene bak i køen."))
        self.settinn.setText(self._translate("MainWindow", "Sett inn pasient:"))
        self.bytt.setToolTip(self._translate("MainWindow",
                                             "Bytt timeplanene til to pasienter. Merk: kun to pasienter kan byttes om gangen."))
        self.bytt.setText(self._translate("MainWindow", "Bytt pasienter:"))
        self.leggtil.setToolTip(self._translate("MainWindow", "Legger til en pasient bakerst i timeplanen."))
        self.leggtil.setText(self._translate("MainWindow", "Legg til pasient:"))

        QtCore.QMetaObject.connectSlotsByName(self)

    # Function for adding another patient to the schedule
    def addPatient(self, name, time, room):

        if self.navninput.text() != '' and len(self.tidinput.text()) == 5:

            self.patients.addPatient(name, time, room, Addpatient(self.scrollframe))
            self.patients.dict[name][2].navn.setText(self._translate("Form", f"{name}"))
            self.patients.dict[name][2].tid.setText(self._translate("Form", f"{self.patients.dict[name][0]}"))
            self.patients.dict[name][2].rom.setText(self._translate("Form", f"{self.patients.dict[name][1]}"))
            #
            self.scrollframeLay.insertWidget(self.scrollframeLay.count() - 1, self.patients.dict[name][2])
            #
            self.navninput.setText('')
            self.tidinput.setText('')

    # Function for deleting a patient from the schedule
    def deletePatient(self, name):

        if name in self.patients.dict:
            self.patients.dict[name][2].setParent(None)
            del self.patients.dict[name]
            self.navninput.setText('')
            self.tidinput.setText('')



