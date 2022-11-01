import sympy
from PyQt5 import QtCore, QtGui, QtWidgets
import Bakgrunnsbilde
import datetime
import numpy as np
from sympy import *

class Room(QtWidgets.QFrame):

    def __init__(self, *args, **kwargs):

        # Make global timer variables
        self.timer_counter_num = 0
        self.timer_running = False

        #Make the frame
        QtWidgets.QFrame.__init__(self, *args, **kwargs)

        # Create global translation protocol:
        self._translate = QtCore.QCoreApplication.translate

        # Configure the frame
        self.createRoom(self, *args, **kwargs)

        # Define buttons
        self.start.clicked.connect(lambda: self.timerColors())
        self.start.clicked.connect( lambda: self.timerFunctions('start'))
        self.stop.clicked.connect(  lambda: self.timerFunctions('stop'))
        self.reset.clicked.connect( lambda: self.timerFunctions('reset'))

    # Define the function that configures the Room-object (self):
    def createRoom(self, *args, **kwargs):

########################################################################################################################
# Configuring the main frame
########################################################################################################################


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

########################################################################################################################
# Create the frame with pasient information/status
########################################################################################################################

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

        # Set grid layout

        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.pasientframe)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)

        # Create the label that displays "Pasient:"

        self.pasientlabel = QtWidgets.QLabel(self.pasientframe)
        font = QtGui.QFont()
        font.setFamily("Roboto Cn")
        font.setPixelSize(13)
        self.pasientlabel.setFont(font)
        self.pasientlabel.setStyleSheet("background:none;""color: rgb(217, 217, 217);")
        self.verticalLayout_7.addWidget(self.pasientlabel, 0, QtCore.Qt.AlignHCenter)
        self.gridLayout.addWidget(self.pasientframe, 0, 0, 1, 1)

        # Create the frame with the patients's name/pseudonym

        self.pasientsvarframe = QtWidgets.QFrame(self.pasientstatus)
        self.pasientsvarframe.setStyleSheet("border-radius:0px;""border-top-right-radius:10px;""border-bottom-right-radius:10px;")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.pasientsvarframe)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)

        # Create the label with the patient's name/pseudonym

        self.pasientsvarlabel = QtWidgets.QLabel(self.pasientsvarframe)
        font = QtGui.QFont()
        font.setFamily("Roboto Cn")
        font.setPixelSize(13)
        self.pasientsvarlabel.setFont(font)
        self.pasientsvarlabel.setStyleSheet("background:none;""color: rgb(255, 255, 255);")
        self.pasientsvarlabel.setAlignment(QtCore.Qt.AlignCenter)
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
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(0)

        # Create label to display "Status:"

        self.statuslabel = QtWidgets.QLabel(self.statusframe)
        font = QtGui.QFont()
        font.setFamily("Roboto Cn")
        font.setPixelSize(13)
        self.statuslabel.setFont(font)
        self.statuslabel.setStyleSheet("background:none;""color: rgb(217, 217, 217);")
        self.verticalLayout_9.addWidget(self.statuslabel, 0, QtCore.Qt.AlignHCenter)
        self.gridLayout.addWidget(self.statusframe, 1, 0, 1, 1)

        # Create the frame to display "<patient status>"

        self.statussvarframe = QtWidgets.QFrame(self.pasientstatus)
        self.statussvarframe.setStyleSheet("border-radius:0px;""border-top-right-radius:10px;""border-bottom-right-radius:10px;")

        # Set grid layout

        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.statussvarframe)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setSpacing(0)

        # Create the label to display "<patient status>"

        self.statussvarlabel = QtWidgets.QLabel(self.statussvarframe)
        font = QtGui.QFont()
        font.setFamily("Roboto Cn")
        font.setPixelSize(13)
        self.statussvarlabel.setFont(font)
        self.statussvarlabel.setStyleSheet("background:none;""color: rgb(255, 255, 255);")
        self.statussvarlabel.setAlignment(QtCore.Qt.AlignCenter)

        # Set grid layout

        self.verticalLayout_10.addWidget(self.statussvarlabel)
        self.gridLayout.addWidget(self.statussvarframe, 1, 1, 1, 1)

        ################################################################################################################
        # Create the frame with "Neste behandling:" and "<next treatment>"
        ################################################################################################################

        self.nestebeh = QtWidgets.QFrame(self.pasientstatus)
        self.nestebeh.setStyleSheet("border-radius:0px;""border-top-left-radius:10px;""border-bottom-left-radius:10px;")

        # Set grid layout

        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.nestebeh)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setSpacing(0)

        # Create the label to display "Neste behandling:"

        self.nestebehlabel = QtWidgets.QLabel(self.nestebeh)
        font = QtGui.QFont()
        font.setFamily("Roboto Cn")
        font.setPixelSize(13)
        self.nestebehlabel.setFont(font)
        self.nestebehlabel.setStyleSheet("background:none;""color: rgb(217, 217, 217);")

        # Set grid layout

        self.verticalLayout_11.addWidget(self.nestebehlabel, 0, QtCore.Qt.AlignHCenter)
        self.gridLayout.addWidget(self.nestebeh, 2, 0, 1, 1)

        # Create frame to display "<next treatment>"

        self.nestebehsvarframe = QtWidgets.QFrame(self.pasientstatus)
        self.nestebehsvarframe.setStyleSheet("border-radius:0px;""border-top-right-radius:10px;""border-bottom-right-radius:10px;")

        # Set grid layout

        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.nestebehsvarframe)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
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

        self.verticalLayout_12.addWidget(self.nestebehsvarlabel, 0, QtCore.Qt.AlignHCenter)
        self.gridLayout.addWidget(self.nestebehsvarframe, 2, 1, 1, 1)
        self.verticalLayout_4.addWidget(self.pasientstatus)

########################################################################################################################
# Create the timer
########################################################################################################################

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
        self.minus.setStyleSheet("QPushButton{\n""border:1px solid;\n""border-color: rgb(39, 39, 39);\n"
                                 "border-radius:0px;\n""border-radius:15px;\n""background-color: rbg(0,0,0,80);\n"
                                 "}\n""QPushButton:hover{\n""background-color: rgba(255, 2, 2, 100);\n""}")

        self.horizontalLayout_6.addWidget(self.minus)

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
        self.textenter.setStyleSheet("border-radius:5px;\n""background-color: rgba(0, 0, 0, 120); \n"
                                     "color: rgb(255, 255, 255);")

        self.textenter.setAlignment(QtCore.Qt.AlignCenter)
        self.horizontalLayout_6.addWidget(self.textenter)

        # Create an input mask:
        self.textenter.setInputMask("99:99:99")


        #connect enter pressed to start:
        self.textenter.returnPressed.connect(lambda: self.timerFunctions("start"))


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
        self.plus.setStyleSheet("QPushButton{\n""border:1px solid;\n""border-color: rgb(39, 39, 39);\n"
                                "border-radius:0px;\n""border-radius:15px;\n""background-color: rgb(0,0,0,80);\n"
                                "}\n""QPushButton:hover{\n""background-color: rgba(0, 255, 0, 100);\n""};")
        self.plus.setAutoRepeatDelay(0)

        self.horizontalLayout_6.addWidget(self.plus)
        self.verticalLayout_44.addWidget(self.addtimeframe)
        self.verticalLayout_4.addWidget(self.timer)

        self.plus.clicked.connect(lambda: self.ui.overview.patients.addTime(self.ui.overview.navninput.text(),self.textenter.text()))

################################################################################################################
# This one thing I have no idea of what does
#################################################################################################################

        QtCore.QMetaObject.connectSlotsByName(self)

################################################################################################################
# Translate protocol
#################################################################################################################

        self.label_2.setText(self._translate("MainWindow", "Injeksjonsrom 1"))
        self.pasientlabel.setText(self._translate("MainWindow", "Pasient:"))
        self.pasientsvarlabel.setText(self._translate("MainWindow", "Magnus Støleggen"))
        self.statuslabel.setText(self._translate("MainWindow", "Status"))
        self.statussvarlabel.setText(self._translate("MainWindow", "Under behandling"))
        self.nestebehlabel.setText(self._translate("MainWindow", "Neste behandling"))
        self.nestebehsvarlabel.setText(self._translate("MainWindow", "PET-Scan - 14:45"))
        self.start.setText(self._translate("MainWindow", "START"))
        self.stop.setText(self._translate("MainWindow", "STOP"))
        self.reset.setText(self._translate("MainWindow", "RESET"))
        self.minus.setText(self._translate("MainWindow", "-"))
        self.plus.setText(self._translate("MainWindow", "+"))

        ########### Set start button


        self.lcdtime.setText(self._translate("MainWindow", "0:00:00"))

    # Define a function that tells the timer how to operate:
    def timerFunctions(self, work):

        # When the start-button is pressed:
        if work == 'start':

            # First check if the entrybox is empty and timer is started for the first timer:
            if self.textenter.text() != '' and len(self.textenter.text()) == 8:

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

                    # Clear the entrybox and disable: (entrybox is set to one space to
                    # differentiate if it's started the first or n-th time.
                    self.textenter.setText(self._translate("MainWindow", ' '))
                    self.textenter.setEnabled(False)

                # Start the count() function:
                self.count()

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

                # Display "00:00:00"
                self.lcdtime.setText(self._translate("MainWindow", f'00:00:00'))

                #Enable/Disable buttons
                self.start.setEnabled(True)
                self.reset.setEnabled(False)

                # Enable the entrybox again:
                self.textenter.setEnabled(True)

                # Clear the entrybox (no spaces):
                self.textenter.setText(self._translate("MainWindow", ''))

    # Define a function that runs once a seconnd whenever the timer is on:
    def count(self):

        # Check if timer is running:
        if self.timer_running == True:

            # Run the reset function when time runs out:
            if self.timer_counter_num == 0:

                self.timerFunctions('reset')

            # If time hasn't run out, set display variable to the current time:
            else:

                display = datetime.timedelta(seconds=self.timer_counter_num)
                self.timer_counter_num -= 1

        # Display the current time
        self.lcdtime.setText(self._translate("MainWindow", f'{display}'))

        # Create a thread that can run the count() function once a second:
        # Create a thread that can run the count() function once a second:
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.count)
        self.timer.setInterval(1000)  # 1000ms = 1s

        # Run the count() function once a second
        self.timer.start()

    # Define the color of the timer according to time left:
    def timerColors(self):

        if self.timer_counter_num==0:

            # # Set the framerate of the color animation
            self.framerate = 20

            # Duration of each pulse in second:
            self.seconds     = 1 #seconds
            self.period      = (2*sympy.pi)/(self.framerate*self.seconds)
            self.sineValue   = 3*sympy.pi/2

            # Define the biggest alpha value
            self.alphaMax = 255

            # Create a thread that can run the color animation:
            self.colorTimer = QtCore.QTimer()
            self.colorTimer.timeout.connect(lambda:self.alphaWave())

            # Apply the framerate
            self.colorTimer.setInterval(int(1000/self.framerate))
            self.colorTimer.start()

            # if self.timer_counter_num >= 1:
            #     self.colorTimer.start()
            # else:
            #     self.colorTimer.stop()
            #

            self.colorTimer.start()

    # Creating the sinewave that controls the pulsating colors
    def alphaWave(self):

        greenTime   = 30 * 60  # 30 minutes
        redTime     = 10 * 60  # 10 minutes
        offColor    = 0        # seconds

        pulse = sympy.sin(self.sineValue)
        pulse = float((pulse + 1) / 2)
        self.sineValue += self.period
        alpha = int(self.alphaMax * pulse)

        if self.sineValue == 7*sympy.pi/2:
            self.sineValue = 3*sympy.pi/2

        if   self.timer_counter_num >= greenTime:

            self.timerframe.setStyleSheet(f"""  border-radius:40px; background:none; border:2px solid;
                                                        border-color: qlineargradient(spread:reflect, x1:0.5, y1:0, x2:1,
                                                        y2:0, stop:0 rgba(0, {alpha}, 0, {alpha / 2}), stop:1 rgba(120, 255, 120, {(alpha + 200) / 2}));""")

        elif self.timer_counter_num >= redTime:

            self.timerframe.setStyleSheet(f"""  border-radius:40px; background:none; border:2px solid;
                                                        border-color: qlineargradient(spread:reflect, x1:0.5, y1:0, x2:1,
                                                        y2:0, stop:0 rgba({alpha}, 255, 0, {alpha / 2}), stop:1 rgba(255, 255, 0, {(alpha + 200) / 2}));""")

        elif self.timer_counter_num <= redTime and self.timer_counter_num > 0:

            self.timerframe.setStyleSheet(f"""  border-radius:40px; background:none; border:2px solid;
                                            border-color: qlineargradient(spread:reflect, x1:0.5, y1:0, x2:1,
                                            y2:0, stop:0 rgba({alpha}, 0, 0, {alpha / 2}), stop:1 rgba(255, 120, 120, {(alpha + 200) / 2}));""")

        elif self.timer_counter_num == 0:
            self.timerframe.setStyleSheet(f"""border-radius:40px; background:none; border:2px solid;
                                                                  border-color: qlineargradient(spread:reflect, x1:0.5, y1:0, x2:1,
                                                                  y2:0, stop:0 rgba(255, 255, 255, 120), stop:1 rgba(255, 255, 255, 120));""")
            self.colorTimer.stop()







