import sympy
from PyQt5 import QtCore, QtGui, QtWidgets
import Bakgrunnsbilde
import datetime
import numpy as np
from sympy import *


class Room(QtWidgets.QFrame):

    # Initialization sequence
    def __init__(self, Master, gui, ow):

        # Instance variable that defines the room number:
        self.roomnr = 1

        # Initialize the main frame:
        QtWidgets.QFrame.__init__(self, Master)

        # Initialize global timer variables:
        self.timer_counter_num = 0
        self.timer_running = False

        # Initialize global translation variable:
        self._translate = QtCore.QCoreApplication.translate

        # Run boot-up functions:
        self.createMainframe(gui, ow)

        # Confiugre buttons:
        self.textenter.returnPressed.connect(lambda: self.timerFunctions('start', ow))
        self.start.clicked.connect( lambda: self.timerFunctions('start', ow))
        self.start.clicked.connect( lambda: gui.timerColors())
        self.textenter.returnPressed.connect(lambda: gui.timerColors())
        self.stop.clicked.connect(  lambda: self.timerFunctions('stop', ow))
        self.reset.clicked.connect( lambda: self.timerFunctions('reset', ow))
        self.plus.clicked.connect(  lambda: self.addTime(ow))
        self.minus.clicked.connect( lambda: self.negTime(ow))

       # Connect the global glock to the patient2room() function

        gui.clock.timeout.connect(lambda: self.patient2room(gui, ow))

########################################################################################################################
#   Configuring boot-up functions. Each part of the object has it's own function. One function runs the next and so on
#   These could all be in one function, but i found it much more tidy to divide them into distinct functions.
########################################################################################################################
    def createMainframe(self, gui, ow):

        self.setObjectName("MainWindow")

        # Set the size of the window and size constraints

        self.setGeometry(QtCore.QRect(0, 0, 259, 316))
        self.setMinimumSize(QtCore.QSize(250, 0))
        self.setMaximumSize(QtCore.QSize(16777215, 16777215))

        # Set Grid layout

        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(1)
        self.verticalLayout_4.setObjectName("verticalLayout_4")

        ################################################################################################################
        # Create the title label
        ################################################################################################################

        self.roomlabel = QtWidgets.QFrame(self)

        # Size constraints

        self.roomlabel.setMinimumSize(QtCore.QSize(0, 25))
        self.roomlabel.setMaximumSize(QtCore.QSize(16777215, 25))

        # Set style

        self.roomlabel.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.539773, y1:1, x2:0.523, y2:0, stop:0.676136 rgba(0, 0, 0, 120), "
                                     "stop:0.881356 rgba(112, 112, 112, 60), stop:1 rgba(255, 255, 255, 0));" "border-radius:2px;" "border-bottom-left-radius:15px;"
                                     "border-bottom-right-radius:15px;")

        # Set grid layout

        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.roomlabel)
        self.verticalLayout_6.setContentsMargins(0, 4, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")

        # Create the label itself and define font and style

        self.label_2 = QtWidgets.QLabel(self.roomlabel)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPixelSize(13)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background:none;""color: rgb(255, 255, 255);")

        # Add label widget to the layout
        self.verticalLayout_6.addWidget(self.label_2, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_4.addWidget(self.roomlabel)


        self.pasientstatus = QtWidgets.QFrame(self)

        # Set size constraints and style

        self.pasientstatus.setMinimumSize(QtCore.QSize(0, 85))
        self.pasientstatus.setMaximumSize(QtCore.QSize(16777215, 85))
        self.pasientstatus.setStyleSheet("border-radius:15px;""border-bottom-right-radius:0px;""border-bottom-left-radius:0px;""background-color: rgba(0, 0, 0, 120);")

        # Set grid Layout
        self.gridLayout = QtWidgets.QGridLayout(self.pasientstatus)
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.gridLayout.setHorizontalSpacing(1)
        self.gridLayout.setVerticalSpacing(3)

        ################################################################################################################
        # Create the frame with "Pasient:" and "<patient name>"
        ################################################################################################################

        self.pasientframe = QtWidgets.QFrame(self.pasientstatus)
        self.pasientframe.setStyleSheet("border-radius:0px;""border-top-left-radius:10px;""border-bottom-left-radius:10px;")
        self.pasientframe.setMaximumSize(75,85)

        # Set grid layout

        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.pasientframe)
        self.verticalLayout_7.setContentsMargins(8, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)


        # Create the label that displays "Pasient:"

        self.pasientlabel = QtWidgets.QLabel(self.pasientframe)
        font = QtGui.QFont()
        font.setFamily("Roboto Cn")
        font.setPixelSize(13)
        self.pasientlabel.setFont(font)
        self.pasientlabel.setStyleSheet("background:none;""color: rgb(217, 217, 217);")
        self.verticalLayout_7.addWidget(self.pasientlabel, 0, QtCore.Qt.AlignLeft)
        self.gridLayout.addWidget(self.pasientframe, 0, 0, 1, 1)

        # Create the frame with the patients's name/pseudonym

        self.pasientsvarframe = QtWidgets.QFrame(self.pasientstatus)
        self.pasientsvarframe.setStyleSheet("border-radius:0px;""border-top-right-radius:10px;""border-bottom-right-radius:10px;")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.pasientsvarframe)
        self.verticalLayout_8.setContentsMargins(8, 3, 0, 0)

        # Create the label with the patient's name/pseudonym

        self.pasientsvarlabel = QtWidgets.QLabel(self.pasientsvarframe)
        font = QtGui.QFont()
        font.setFamily("Roboto Cn")
        font.setPixelSize(13)
        self.pasientsvarlabel.setFont(font)
        self.pasientsvarlabel.setStyleSheet("background:none;""color: rgb(255, 255, 255);")
        self.pasientsvarlabel.setAlignment(QtCore.Qt.AlignLeft)
        self.verticalLayout_8.addWidget(self.pasientsvarlabel)
        self.gridLayout.addWidget(self.pasientsvarframe, 0, 1, 1, 1)

        ################################################################################################################
        # Create the frame with "Status:" and "<patient status>"
        ################################################################################################################

        self.statusframe = QtWidgets.QFrame(self.pasientstatus)
        self.statusframe.setStyleSheet("border-radius:15px;""border-top-left-radius:10px;"
                                       "border-bottom-left-radius:10px;")

        # Set grid layout

        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.statusframe)
        self.verticalLayout_9.setContentsMargins(8, 0, 0, 0)
        self.verticalLayout_9.setSpacing(0)

        # Create label to display "Status:"

        self.statuslabel = QtWidgets.QLabel(self.statusframe)
        font = QtGui.QFont()
        font.setFamily("Roboto Cn")
        font.setPixelSize(13)
        self.statuslabel.setFont(font)
        self.statuslabel.setStyleSheet("background:none;""color: rgb(217, 217, 217);")
        self.verticalLayout_9.addWidget(self.statuslabel, 0, QtCore.Qt.AlignLeft)
        self.gridLayout.addWidget(self.statusframe, 1, 0, 1, 1)

        # Create the frame to display "<patient status>"

        self.statussvarframe = QtWidgets.QFrame(self.pasientstatus)
        self.statussvarframe.setStyleSheet("border-radius:0px;""border-top-right-radius:10px;""border-bottom-right-radius:10px;")

        # Set grid layout

        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.statussvarframe)
        self.verticalLayout_10.setContentsMargins(8, 3, 0, 0)
        self.verticalLayout_10.setSpacing(0)

        # Create the label to display "<patient status>"

        self.statussvarlabel = QtWidgets.QLabel(self.statussvarframe)
        font = QtGui.QFont()
        font.setFamily("Roboto Cn")
        font.setPixelSize(13)
        self.statussvarlabel.setFont(font)
        self.statussvarlabel.setStyleSheet("background:none;""color: rgb(255, 255, 255);")
        self.statussvarlabel.setAlignment(QtCore.Qt.AlignLeft)

        # Set grid layout

        self.verticalLayout_10.addWidget(self.statussvarlabel, 0, QtCore.Qt.AlignLeft)
        self.gridLayout.addWidget(self.statussvarframe, 1, 1, 1, 1)

        ################################################################################################################
        # Create the frame with "Neste behandling:" and "<next treatment>"
        ################################################################################################################

        self.nestebeh = QtWidgets.QFrame(self.pasientstatus)
        self.nestebeh.setStyleSheet("border-radius:0px;""border-top-left-radius:10px;""border-bottom-left-radius:10px;")

        # Set grid layout

        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.nestebeh)
        self.verticalLayout_11.setContentsMargins(8, 0, 0, 0)
        self.verticalLayout_11.setSpacing(0)

        # Create the label to display "Neste behandling:"

        self.nestebehlabel = QtWidgets.QLabel(self.nestebeh)
        font = QtGui.QFont()
        font.setFamily("Roboto Cn")
        font.setPixelSize(13)
        self.nestebehlabel.setFont(font)
        self.nestebehlabel.setStyleSheet("background:none;""color: rgb(217, 217, 217);")

        # Set grid layout

        self.verticalLayout_11.addWidget(self.nestebehlabel, 0, QtCore.Qt.AlignLeft)
        self.gridLayout.addWidget(self.nestebeh, 2, 0, 1, 1)

        # Create frame to display "<next treatment>"

        self.nestebehsvarframe = QtWidgets.QFrame(self.pasientstatus)
        self.nestebehsvarframe.setStyleSheet("border-radius:0px;""border-top-right-radius:10px;""border-bottom-right-radius:10px;")

        # Set grid layout

        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.nestebehsvarframe)
        self.verticalLayout_12.setContentsMargins(8, 0, 0, 0)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")

        # Create label to display "<next treatment>"

        self.nestebehsvarlabel = QtWidgets.QLabel(self.nestebehsvarframe)
        font = QtGui.QFont()
        font.setFamily("Roboto Cn")
        font.setPixelSize(13)
        self.nestebehsvarlabel.setFont(font)
        self.nestebehsvarlabel.setStyleSheet("background:none;""color: rgb(255, 255, 255);")

        # Set grid layout

        self.verticalLayout_12.addWidget(self.nestebehsvarlabel, 0, QtCore.Qt.AlignLeft)
        self.gridLayout.addWidget(self.nestebehsvarframe, 2, 1, 1, 1)
        self.verticalLayout_4.addWidget(self.pasientstatus)



        self.timer = QtWidgets.QFrame(self)
        self.timer.setStyleSheet("border-radius:0px;""background-color: rgba(0, 0, 0, 120);"
                                 "border-bottom-left-radius:15px;""border-bottom-right-radius:15px;")

        # Set grid layout

        self.verticalLayout_44 = QtWidgets.QVBoxLayout(self.timer)
        self.verticalLayout_44.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_44.setSpacing(4)

        # Create frame to containt the timer label

        self.timerframe = QtWidgets.QFrame(self.timer)
        self.timerframe.setMinimumSize(QtCore.QSize(250, 80))
        self.timerframe.setMaximumSize(QtCore.QSize(250, 80))

        self.timerframe.setStyleSheet(f"""border-radius:40px; background:none; border:2px solid;
                                          border-color: rgba(255, 255, 255, 255)""")

        # Set grid layout

        self.verticalLayout_49 = QtWidgets.QVBoxLayout(self.timerframe)
        self.verticalLayout_49.setObjectName("verticalLayout_49")

################################################################################################################
# Create the timer label
#################################################################################################################


        self.lcdtime = QtWidgets.QLabel(self.timerframe)

        # Set style and font

        self.lcdtime.setStyleSheet("color: rgba(255, 255, 255, 200);border:none;")
        font = QtGui.QFont()
        font.setFamily("Roboto Cn")
        font.setPixelSize(45)
        self.lcdtime.setFont(font)

        # Set grid layout

        self.verticalLayout_49.addWidget(self.lcdtime)
        self.lcdtime.setAlignment(QtCore.Qt.AlignHCenter)
        self.lcdtime.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout_44.addWidget(self.timerframe, 0, QtCore.Qt.AlignHCenter)

################################################################################################################
# Create buttons
#################################################################################################################

        # Frame for start and stop

        self.startstopframe = QtWidgets.QFrame(self.timer)

        self.startstopframe.setMinimumSize(QtCore.QSize(0, 30))
        self.startstopframe.setMaximumSize(QtCore.QSize(16777215, 30))
        self.startstopframe.setStyleSheet("background:none;")

        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.startstopframe)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setSpacing(0)

        ################################################################################################################
        # Create the start button
        #################################################################################################################

        self.start = QtWidgets.QPushButton(self.startstopframe)

        self.start.setMinimumSize(QtCore.QSize(50, 30))
        self.start.setMaximumSize(QtCore.QSize(50, 30))

        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPixelSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.start.setFont(font)
        self.start.setStyleSheet("QPushButton{\n""border:1px solid;\n""border-color: rgb(39, 39, 39);\n"
                                 "border-radius:0px;\n""border-radius:15px;\n""background-color: rbg(0,0,0,80);\n"
                                 "    color: rgb(217, 217, 217);\n""}\n""QPushButton:hover{\n"
                                 "background-color: rgba(0, 0, 0, 120);\n""}")

        self.horizontalLayout_11.addWidget(self.start)

        ################################################################################################################
        # Create the stop button
        #################################################################################################################

        self.stop = QtWidgets.QPushButton(self.startstopframe)

        self.stop.setMinimumSize(QtCore.QSize(50, 30))
        self.stop.setMaximumSize(QtCore.QSize(50, 30))

        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPixelSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.stop.setFont(font)

        self.stop.setStyleSheet("QPushButton{\n""border:1px solid;\n""border-color: rgb(39, 39, 39);\n"
                                "border-radius:0px;\n""border-radius:15px;\n""background-color: rbg(0,0,0,80);\n"
                                "    color: rgb(217, 217, 217);\n""}\n""QPushButton:hover{\n"
                                "background-color: rgba(0, 0, 0, 120);\n""}")

        self.horizontalLayout_11.addWidget(self.stop)

        # Initialize the button as disabled:
        self.stop.setEnabled(False)

        ################################################################################################################
        # Create the reset button
        #################################################################################################################

        self.reset = QtWidgets.QPushButton(self.startstopframe)

        self.reset.setMinimumSize(QtCore.QSize(50, 30))
        self.reset.setMaximumSize(QtCore.QSize(50, 30))

        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPixelSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.reset.setFont(font)
        self.reset.setStyleSheet("QPushButton{\n""border:1px solid;\n""border-color: rgb(39, 39, 39);\n"
                                 "border-radius:0px;\n""border-radius:15px;\n""background-color: rbg(0,0,0,80);\n"
                                 "    color: rgb(217, 217, 217);\n""}\n""QPushButton:hover{\n"
                                 "background-color: rgba(0, 0, 0, 120);\n""}")

        self.horizontalLayout_11.addWidget(self.reset)
        self.verticalLayout_44.addWidget(self.startstopframe)

        # Frame for the "add tim" button

        self.addtimeframe = QtWidgets.QFrame(self.timer)

        self.addtimeframe.setMinimumSize(QtCore.QSize(0, 30))
        self.addtimeframe.setMaximumSize(QtCore.QSize(16777215, 30))

        self.addtimeframe.setStyleSheet("background:none")

        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.addtimeframe)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")

        # Initialize the button as disabled:
        self.reset.setEnabled(False)

        ################################################################################################################
        # Create the minus time button
        #################################################################################################################

        self.minus = QtWidgets.QPushButton(self.addtimeframe)

        self.minus.setMinimumSize(QtCore.QSize(30, 30))
        self.minus.setMaximumSize(QtCore.QSize(30, 30))

        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPixelSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.minus.setFont(font)
        self.minus.setStyleSheet(""" 
                                    QPushButton:disabled   {    background-color:   rgba(255, 255, 255, 80)         }
                                    QPushButton:hover      {    background-color:   rgba(0, 0, 0, 120);             }
                                    QPushButton:pressed    {    background-color:   rgba(0, 0, 0, 200);             } 
                                    QPushButton            {    background-color:   rgb(0,0,0,80); 
                                                                border-color:       rgb(39, 39, 39);
                                                                border:             1px solid;   
                                                                border-radius:      0px;  
                                                                border-radius:      15px;
                                                                color:              rgba(0, 0, 0, 255)                }      
                                """)

        self.horizontalLayout_6.addWidget(self.minus)

        # Initialize button as disabled:
        self.minus.setEnabled(False)

        ################################################################################################################
        # Create the text enter widget
        #################################################################################################################

        self.textenter = QtWidgets.QLineEdit(self.addtimeframe)

        self.textenter.setMinimumSize(QtCore.QSize(0, 30))
        self.textenter.setMaximumSize(QtCore.QSize(120, 16777215))

        font = QtGui.QFont()
        font.setFamily("Roboto Cn")
        font.setPixelSize(13)
        self.textenter.setFont(font)
        self.textenter.setStyleSheet("border-radius:5px;\n" 
                                     "background-color: rgba(0, 0, 0, 120); \n"
                                     "color: rgb(255, 255, 255);")

        self.textenter.setAlignment(QtCore.Qt.AlignCenter)
        self.horizontalLayout_6.addWidget(self.textenter)

        # Create a layout inside the textenter:
        self.textenterlay = QtWidgets.QHBoxLayout(self.textenter)
        self.textenterlay.setContentsMargins(15, 0,0, 0)
        self.textenterlabel = QtWidgets.QLabel(self.textenter)
        self.textenterlay.addWidget(self.textenterlabel)
        self.textenterlabel.setStyleSheet("background:none")
        self.textenter.setFont(font)


        # Create an input mask:
        self.textenter.setText("00:00:00")
        self.textenter.setInputMask("99:99:99")

        # Define the initial input validator
        self.reg_ex = QtCore.QRegExp("[0-2]{1}[0-3]{1}"+":"+"[0-5]{1}[0-9]{1}"+":"+"[0-5]{1}[0-9]{1}")
        self.input_validator1 = QtGui.QRegExpValidator(self.reg_ex, self.textenter)
        self.textenter.setValidator(self.input_validator1)

        # Define the input validator for when the timer is running:
        self.reg_ex2 = QtCore.QRegExp("[0-9]{2}")
        self.input_validator2 = QtGui.QRegExpValidator(self.reg_ex2, self.textenter)

        # Initialize enterbox as disabled
        self.textenter.setEnabled(False)


        ################################################################################################################
        # Create the plus time button
        #################################################################################################################

        self.plus = QtWidgets.QPushButton(self.addtimeframe)

        self.plus.setMinimumSize(QtCore.QSize(30, 30))
        self.plus.setMaximumSize(QtCore.QSize(30, 30))

        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPixelSize(13)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(False)
        self.plus.setFont(font)
        self.plus.setStyleSheet(""" 
                                    QPushButton:disabled   {    background-color:   rgba(255, 255, 255, 80)         }
                                    QPushButton:hover      {    background-color:   rgba(0, 0, 0, 120);             }
                                    QPushButton:pressed    {    background-color:   rgba(0, 0, 0, 200);             } 
                                    QPushButton            {    background-color:   rgb(0,0,0,80); 
                                                                border-color:       rgb(39, 39, 39);
                                                                border:             1px solid;   
                                                                border-radius:      0px;  
                                                                border-radius:      15px;
                                                                color:              rgba(0, 0, 0, 255)                }      
                                """)

        self.plus.setAutoRepeatDelay(0)

        self.horizontalLayout_6.addWidget(self.plus)
        self.verticalLayout_44.addWidget(self.addtimeframe)
        self.verticalLayout_4.addWidget(self.timer)

        # Initialize as diabled
        self.plus.setEnabled(False)


################################################################################################################
# This one thing I have no idea of what does
#################################################################################################################

        QtCore.QMetaObject.connectSlotsByName(self)

################################################################################################################
# Translate protocol
#################################################################################################################

        self.label_2.setText(self._translate("MainWindow", "Injeksjonsrom 1"))
        self.pasientlabel.setText(self._translate("MainWindow", "Pasient:"))
        self.pasientsvarlabel.setText(self._translate("MainWindow", ""))
        self.statuslabel.setText(self._translate("MainWindow", "Status:"))
        self.statussvarlabel.setText(self._translate("MainWindow", ""))
        self.nestebehlabel.setText(self._translate("MainWindow", "PET-Scan:"))
        self.nestebehsvarlabel.setText(self._translate("MainWindow", ""))
        self.start.setText(self._translate("MainWindow", "START"))
        self.stop.setText(self._translate("MainWindow", "STOP"))
        self.reset.setText(self._translate("MainWindow", "RESET"))
        self.minus.setText(self._translate("MainWindow", "-"))
        self.plus.setText(self._translate("MainWindow", "+"))

        ########### Initialize the timer display

        self.lcdtime.setText(self._translate("MainWindow", "00:00:00"))

        #### Initialize variable to know treatment has not started
        self.treatmentstarted = False

# ########################################################################################################################
#   Configuring other functions:
# ########################################################################################################################

    # Tells the timer how to operate
    def timerFunctions(self, work, ow):

        # When the start-button is pressed:
        if work == 'start' and self.textenter.text() != "00:00:00" and len(self.textenter.text()) != 2:

            # Define the treatment as started:

            ow.patients.dict[self.pasientsvarlabel.text()][3] = True

            # Set the state of the timer to Running
            self.timer_running = True

            # Disable and enable buttons
            self.start.setEnabled(False)
            self.stop.setEnabled(True)
            self.reset.setEnabled((False))

             # If the timer starts for the first time, create timer-thread and fetch the time from the entrybox
            if self.timer_counter_num == 0:

                #Fetch time from entrybox
                timer_time_str = self.textenter.text()
                hours, minutes, seconds = timer_time_str.split(':')
                minutes = int(minutes) + (int(hours) * 60)
                seconds = int(seconds) + (minutes * 60)
                self.timer_counter_num = self.timer_counter_num + seconds

                # Convert the entrybox to plus/minus time:
                self.textenter.setInputMask("99")
                self.textenterlabel.setText(self._translate("MainWindow", "Min ±"))
                self.textenter.setText(self._translate("MainWindow", '00'))
                self.textenter.setValidator(self.input_validator2)
                # Start the count() function:
                self.count()
            else:
                self.count()

            # Disable plus and minus buttons if no patient in the room and enable if patient in room
            # Also disable enterbox
            if self.pasientsvarlabel.text() == "":
                self.plus.setEnabled(False)
                self.minus.setEnabled(False)
                self.textenter.setText(self._translate("MainWindow", ""))
                self.textenterlabel.setText(self._translate("MainWindow", ""))
            else:
                self.plus.setEnabled(True)
                self.minus.setEnabled(True)
                self.textenter.setEnabled(False)

        # When the stop-button is pressed:
        elif work == 'stop':

            # Set timer state to Off
            self.timer_running = False

            # Disable/Enable buttons
            self.start.setEnabled(True)
            self.stop.setEnabled(False)
            self.reset.setEnabled(True)

            # Stop the count() function:
            self.timer.stop()

        # When the reset-button is pressed:
        elif work == 'reset':

            # If the timer ran out, stop the timer:
            if self.timer_counter_num == 0:
                self.timer.stop()
                self.timer_running = False

            # If the timer was manually reset:
            else:
                # Reset the time
                self.timer_counter_num = 0
                self.timer.stop()
                self.timer_running = False

            # Display "00:00:00"
            self.lcdtime.setText(self._translate("MainWindow", '00:00:00'))

            #Enable/Disable buttons
            self.start.setEnabled(True)
            self.reset.setEnabled(False)
            self.plus.setEnabled(False)
            self.minus.setEnabled(False)

            # Reset the entrybox:
            self.textenter.setEnabled(True)
            self.textenter.setText(self._translate("MainWindow", '00:00:00'))
            self.textenter.setInputMask("99:99:99")

            # Convert the textenter back to regular time format
            self.textenter.setInputMask("99:99:99")
            self.textenter.setText(self._translate("MainWindow", "00:00:00"))
            self.textenterlabel.setText(self._translate("MainWindow", ""))
            self.textenter.setValidator(self.input_validator1)

    # Counts down once a second
    def count(self):

        # Check if timer is running:
        if self.timer_running == True:

            # Run the reset function when time runs out:
            if self.timer_counter_num == 0:

                self.timerFunctions('reset')
                return

            # If time hasn't run out, set display variable to the current time:
            else:

                display = datetime.timedelta(seconds=self.timer_counter_num)
                self.timer_counter_num -= 1

        # Display the current time
        self.lcdtime.setText(self._translate("MainWindow", f'0{display}'))

        # Create a thread that can run the count() function once a second:
        # Create a thread that can run the count() function once a second:
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.count)
        self.timer.setInterval(1000)  # 1000ms = 1s

        # Run the count() function once a second
        self.timer.start()

    # Add time to the display and schedule
    def addTime(self, ow):

        if int(self.textenter.text()) != "00":

            timeint = int(self.textenter.text())
            sec     = timeint * 60

            if self.timer_counter_num + sec >= 86400:

                return

            else:

                # Add the time to the dictionary
                ow.patients.addTime(self.pasientsvarlabel.text(), self.textenter.text(), self.timer_counter_num)
                nexttreatment = ow.patients.string2Min(ow.patients.dict[f'{self.pasientsvarlabel.text()}'][0])
                nexttreatment = nexttreatment + 45
                nexttreatment = ow.patients.min2String(nexttreatment)
                self.nestebehsvarlabel.setText(self._translate("MainWindow", f"{nexttreatment}"))
                self.timer_counter_num += sec
                display = datetime.timedelta(seconds=self.timer_counter_num)
                self.lcdtime.setText(self._translate("MainWindow", f'0{display}'))

    # Subtract time from the display and schedule
    def negTime(self, ow):

        timeint = int(self.textenter.text())
        sec = timeint * 60

        if self.timer_counter_num - sec <= 0:

            ow.patients.subTime(self.pasientsvarlabel.text(), self.timer_counter_num, self.timer_counter_num)
            nexttreatment = ow.patients.string2Min(ow.patients.dict[f'{self.pasientsvarlabel.text()}'][0])
            nexttreatment = nexttreatment + 45
            nexttreatment = ow.patients.min2String(nexttreatment)
            self.nestebehsvarlabel.setText(self._translate("MainWindow", f"{nexttreatment}"))
            self.timerFunctions("reset", ow)

        else:

            ow.patients.subTime(self.pasientsvarlabel.text(), self.textenter.text(), self.timer_counter_num)
            nexttreatment = ow.patients.string2Min(ow.patients.dict[f'{self.pasientsvarlabel.text()}'][0])
            nexttreatment = nexttreatment + 45
            nexttreatment = ow.patients.min2String(nexttreatment)
            self.nestebehsvarlabel.setText(self._translate("MainWindow", f"{nexttreatment}"))
            self.timer_counter_num -= sec
            display = datetime.timedelta(seconds=self.timer_counter_num)
            self.lcdtime.setText(self._translate("MainWindow", f'0{display}'))

    def patient2room(self, gui, ow):

        # Only run this function if the dictionary is not empty. If not the program would crash on opening since
        # no patients would be added yet
        if ow.patients.dict == {}:
            return

        # Iterate through the patient schedule
        for i in ow.patients.dict:

            # Convert the scheduled time to minutes past midnight
            Hours, Minutes = ow.patients.dict[i][0].split(':')
            patienttime = (int(Hours) * 60) + int(Minutes)

            # Run code below only if the clock is in the period where the patient is scheduled to be treated (or if the treatment isn't finished yet)
            if ow.patients.dict[i][1] == self.roomnr and (  (gui.clockNum >= patienttime) and ( ((patienttime+45)>=gui.clockNum) or self.timer_running==True)) :

                pass

            else:

                continue

            # Find the time for PET-Scan:

            petTime = str(datetime.timedelta(minutes=(patienttime + 45)))
            if len(petTime) == 7:
                time = f"0{petTid}"
            petTime = petTime[:5]

            # Don't swap patient if the countdown isn't finished
            if self.timer_counter_num != 0:
                continue

            self.pasientsvarlabel.setText(self._translate("MainWindow", f"{i}"))
            self.textenter.setEnabled(True)

            # If the treatment isn't startet yet, the status is "Waiting for treatment"
            if ow.patients.dict[i][3] == False:

                self.statussvarlabel.setText(self._translate("MainWindow", "Venter på injeksjon"))

            # When the treatment is over status is "Waiting for PET-Scan
            elif self.timer_counter_num == 0:

                self.statussvarlabel.setText(self._translate("MainWindow", "Avventer PET-Scan"))

            # When the treatment is started and there is more than 15 min left: the status is "Under treatment"
            elif self.timer_counter_num >= (15 * 60):

                self.statussvarlabel.setText(self._translate("MainWindow", "Under behandling"))

            # When there is less than 15 minutes left, status is "WC and water"
            elif self.timer_counter_num < (15 * 60) and self.timer_counter_num > 0:

                self.statussvarlabel.setText(self._translate("MainWindow", "Vann og WC"))

            # Next treatment is patients.dict index 0 + 45 min and any possible delays
            self.nestebehsvarlabel.setText(self._translate("MainWindow", f"{petTime}"))