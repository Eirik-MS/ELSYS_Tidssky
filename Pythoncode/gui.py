import sys
import Bakgrunnsbilde
from room import Room
from overview import Overview
from addpatient import Addpatient
from PyQt5 import QtCore, QtGui, QtWidgets
from Classes import Patients
import sympy
import time
import datetime

#### The main structure of the Graphical User Interface

class GUI(object):

    def __init__(self):

        # Definere hvor lang tid det er mellom to behandlinger på samme injeksjonsrom
        self.tidMellomInjeksjoner = 30

    # Setup the GUI
    def setupUi(self, MainWindow):

########################################################################################################################
#   Set the initial size of the main window and remove the window frames
########################################################################################################################

        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        MainWindow.resize(1340, 768)

########################################################################################################################
# Since PyQt5 originally is written for CSS we need to format strings to be displayed correctly in python
# Here we create a variable with a shorter name for that process.
########################################################################################################################

        _translate = QtCore.QCoreApplication.translate
        self._translate = QtCore.QCoreApplication.translate

########################################################################################################################
# Make the frame that is going to serve as the main window
########################################################################################################################

        self.centrawidget = QtWidgets.QWidget(MainWindow)
        self.centrawidget.setStyleSheet("background:none;")

        #### Making the grid layout of the frame

        self.drop_shadow_layout = QtWidgets.QVBoxLayout(self.centrawidget)
        self.drop_shadow_layout.setContentsMargins(10, 10, 10, 10)

########################################################################################################################
# Making the frame that is going to serve as the application window
########################################################################################################################

        self.mainwindow = QtWidgets.QFrame(self.centrawidget)

        #### Set corner roundness and background image

        self.mainwindow.setStyleSheet("border-image: url(:/images/Background3.jpg);border-radius: 15px;")

        #### Create the grid layout of the application window. The window is divided into
        #### three frames stacked on topof each other

        self.verticalLayout = QtWidgets.QVBoxLayout(self.mainwindow)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)

########################################################################################################################
#   Creating the top frame
########################################################################################################################

        self.top = QtWidgets.QFrame(self.mainwindow)

        #### Set size constraints

        self.top.setMinimumSize(QtCore.QSize(0, 50))
        self.top.setMaximumSize(QtCore.QSize(16777215, 50))

        #### Unable backgrounds so that the main background image is not repeated within this frame

        self.top.setStyleSheet("border-image:none; background:none;")

        #### Create the grid layout of the frame

        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.top)
        self.horizontalLayout_3.setContentsMargins(4, 4, 0, 0)
        self.horizontalLayout_3.setSpacing(0)

        ################################################################################################################
        # Creating the frame with the application title
        ################################################################################################################

        self.frame = QtWidgets.QFrame(self.top)
        self.frame.setStyleSheet("background:none;")

        #### Creating the grid layout inside this frame

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)

        #### Creating the label (text box) to display the application title

        self.title = QtWidgets.QLabel(self.frame)

        #### Set size constraints

        self.title.setMinimumSize(QtCore.QSize(155, 0))
        self.title.setMaximumSize(QtCore.QSize(155, 16777215))

        #### Set text to be displayed

            # This is done in the clock function at the bottom of the code

        #### Set fonts

        font = QtGui.QFont()
        font.setFamily("Roboto Cn")
        font.setPixelSize(30)
        font.setKerning(False)
        self.title.setFont(font)
        self.title.setStyleSheet(       "border-bottom-right-radius:15px;"      "border-bottom-left-radius:5px;"        "color: rgb(255, 255, 255);"            
                                        "background-color:rgba(0, 0, 0, 120);"  "border-bottom-right-radius:15px;"      "border-top-right-radius:15px;"
                                        "border-bottom-left-radius:0px;")

        #### Creating yet another layout in the frame so that the title is displayed in the middle verticaly

        self.verticalLayout_2.addWidget(self.title)
        self.horizontalLayout_3.addWidget(self.frame)

########################################################################################################################
# Creating a frame to hold the open, close, and minimize buttons
########################################################################################################################

        self.open_close = QtWidgets.QFrame(self.top)

        #### Size constraints

        self.open_close.setMinimumSize(QtCore.QSize(130, 50))
        self.open_close.setMaximumSize(QtCore.QSize(130, 50))

        #### Set transparent background

        self.open_close.setStyleSheet("background:none")

        ### Set a grid layout

        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.open_close)
        self.horizontalLayout_4.setContentsMargins(50, 5, 0, -1)
        self.horizontalLayout_4.setSpacing(0)

        ################################################################################################################
        # Create the minimize button
        ################################################################################################################

        self.minimize = QtWidgets.QPushButton(self.open_close)
        self.minimize.setMinimumSize(QtCore.QSize(16, 16))
        self.minimize.setMaximumSize(QtCore.QSize(16, 16))
        self.minimize.setStyleSheet(""" QPushButton{border-radius:8px;      background-color: rgb(255, 255, 0);}
                                        QPushButton:hover{background-color:rgb(236, 236, 0);}""")

        #### Set the text of the button to nothing

        self.minimize.setText("")

        #### Set alignment within the frame

        self.horizontalLayout_4.addWidget(self.minimize, 0, QtCore.Qt.AlignTop)

        ################################################################################################################
        # Create the maximize button
        ################################################################################################################

        self.maximize = QtWidgets.QPushButton(self.open_close)
        self.maximize.setMinimumSize(QtCore.QSize(16, 16))
        self.maximize.setMaximumSize(QtCore.QSize(16, 16))
        self.maximize.setStyleSheet(""" QPushButton{border-radius:8px;     background-color: rgb(2, 255, 2);}
                                        QPushButton:hover{background-color:rgb(1, 211, 1);}""")

        #### Set the button text to nothing

        self.maximize.setText("")

        #### Set the alignment within the frame

        self.horizontalLayout_4.addWidget(self.maximize, 0, QtCore.Qt.AlignTop)

        ################################################################################################################
        # Create the close button
        ################################################################################################################

        self.close = QtWidgets.QPushButton(self.open_close)
        self.close.setMinimumSize(QtCore.QSize(16, 16))
        self.close.setMaximumSize(QtCore.QSize(16, 16))
        self.close.setStyleSheet("""    QPushButton{border-radius:8px;        background-color: rgb(255, 2, 2);}
                                        QPushButton:hover{background-color:rgb(225, 1, 1);}                     """)

        #### Set button text to nothing

        self.close.setText("")

        #### Set the alignment inside the frame

        self.horizontalLayout_4.addWidget(self.close, 0, QtCore.Qt.AlignTop)
        self.horizontalLayout_3.addWidget(self.open_close, 0, QtCore.Qt.AlignTop)
        self.verticalLayout.addWidget(self.top)

########################################################################################################################
# Create the middle frame of the application. This is the frame that will contain the main contents of the application
########################################################################################################################

        self.middle = QtWidgets.QFrame(self.mainwindow)
        self.middle.setStyleSheet("border-image:none;   background:none;")

        #### Set the grid layout of the middle frame

        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.middle)
        self.verticalLayout_3.setContentsMargins(4, 0, 4, 0)
        self.verticalLayout_3.setSpacing(0)

        ################################################################################################################
        # Create the frame that will contain all of the five room() objects
        ################################################################################################################

        self.Rooms = QtWidgets.QFrame(self.middle)

        #### Set size constraints

        self.Rooms.setMinimumSize(QtCore.QSize(1300, 340))
        self.Rooms.setMaximumSize(QtCore.QSize(16777215, 500))

        #### Set transparent background

        self.Rooms.setStyleSheet("background-color:none;")

        #### Set the grid layout

        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.Rooms)
        self.horizontalLayout_5.setContentsMargins(0, 20, 0, 4)
        self.horizontalLayout_5.setSpacing(4)
        self.verticalLayout_3.addWidget(self.Rooms)

        ################################################################################################################
        # Create five rooms. The room object is imported from it's own class.
        ################################################################################################################

        #### Make separate variables for each room so they can be modified independently, and add these to a dictionary

        self.rooms = {}

        self.rooms["room1"] = Room()
        self.rooms["room2"] = Room()
        self.rooms["room3"] = Room()
        self.rooms["room4"] = Room()
        self.rooms["room5"] = Room()

        #### Add each room to the layout of self.Rooms

        self.horizontalLayout_5.addWidget(self.rooms["room1"])
        self.horizontalLayout_5.addWidget(self.rooms["room2"])
        self.horizontalLayout_5.addWidget(self.rooms["room3"])
        self.horizontalLayout_5.addWidget(self.rooms["room4"])
        self.horizontalLayout_5.addWidget(self.rooms["room5"])

        #### Change the titles of each room (Room nr. 1 already has the correct title)

        self.rooms["room2"].label_2.setText(_translate("MainWindow", "Injeksjonsrom 2"))
        self.rooms["room3"].label_2.setText(_translate("MainWindow", "Injeksjonsrom 3"))
        self.rooms["room4"].label_2.setText(_translate("MainWindow", "Injeksjonsrom 4"))
        self.rooms["room5"].label_2.setText(_translate("MainWindow", "PET-Scan"))

        ################################################################################################################
        # Create the frame that will contain the other contents in the application
        ################################################################################################################

        self.overview = Overview(self.middle)


        #### Set background color to be semi-transparent



        ### Set grid layout

        self.verticalLayout_3.addWidget(self.overview)
        self.verticalLayout.addWidget(self.middle)

########################################################################################################################
# Create the bottom of the three main frames. This frame will contain the credits and the widget to resize the frame
########################################################################################################################

        self.bottom = QtWidgets.QFrame(self.mainwindow)

        #### Set size constraints

        self.bottom.setMinimumSize(QtCore.QSize(0, 20))
        self.bottom.setMaximumSize(QtCore.QSize(16777215, 20))

        #### Set transparent background

        self.bottom.setStyleSheet("border-image:none;   background:none")

        #### Set grid layout

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.bottom)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        #### Create the frame that will contain the credits label

        self.creditframe = QtWidgets.QFrame(self.bottom)

        #### Set transparent background

        self.creditframe.setStyleSheet("border-image:none; background:none;")

        #### Set grid layout

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.creditframe)
        self.horizontalLayout_2.setContentsMargins(7, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        ################################################################################################################
        # Create the text label
        ################################################################################################################

        self.credits = QtWidgets.QLabel(self.creditframe)

        #### Set text to be displayed

        self.credits.setText(_translate("MainWindow", "Av: Silnes, Chewiejczak, Nore, Singh Sidhu, Gripsgård, Støleggen"))

        #### Set font

        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(7)
        self.credits.setFont(font)
        self.credits.setStyleSheet("border-image:none;  background:none;")

        ### Set grid of the text label for the text to be aligned properly

        self.horizontalLayout_2.addWidget(self.credits)
        self.horizontalLayout.addWidget(self.creditframe)

        ################################################################################################################
        # Create the frame that will hold the stretching widget
        ################################################################################################################

        self.stretch = QtWidgets.QFrame(self.bottom)

        #### Size constraints

        self.stretch.setMinimumSize(QtCore.QSize(30, 30))
        self.stretch.setMaximumSize(QtCore.QSize(30, 30))

        #### Set transparent background

        self.stretch.setStyleSheet("border-image:none;  background:none;")

        #### Add the frame to a layout

        self.horizontalLayout.addWidget(self.stretch)
        self.verticalLayout.addWidget(self.bottom)

        self.stretchLay = QtWidgets.QHBoxLayout(self.stretch)
        self.stretchLay.setContentsMargins(0, 0, 0, 0)
        self.stretchLay.setSpacing(0)

        ################################################################################################################
        # Create the sizeGrip widget and add it to the layout
        ################################################################################################################

        self.sizeGrip = QtWidgets.QSizeGrip(self.stretch)
        self.stretchLay.addWidget(self.sizeGrip)






########################################################################################################################
# Something i'm not quite sure what does, but needs to be here for everything to work
########################################################################################################################

        #### I think this adds the mainframe to the application window. Edit: Yes, it does. If this is not activated
        #### Every widget will try to fit into the same spot in the application window

        self.drop_shadow_layout.addWidget(self.mainwindow)

        #### I think this sets the centrawidget as the main widget, the one to contain all other widgets

        MainWindow.setCentralWidget(self.centrawidget)

        #### I searched up this one and had no clue what it meant. It is propably needed is all i could understand

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

########################################################################################################################
#   Configure the buttons
########################################################################################################################

        self.buttonConfig()

########################################################################################################################
#   Start the global clock
########################################################################################################################

        # I do this at the end and not the begining because the clock() function needs the title label to bed
        # created before it is called
        self.clock()

    # Create a function to check if all timers are on or off
    def timersOff(self):

        self.totalTimerCount = (self.rooms["room1"].timer_counter_num + self.rooms["room2"].timer_counter_num +
                                self.rooms["room3"].timer_counter_num + self.rooms["room4"].timer_counter_num +
                                self.rooms["room5"].timer_counter_num)
        if self.totalTimerCount == 0:
            return True
        else:
            return False

    #Create a timer that runs the alphaWave function at a custom framerate
    def timerColors(self):

        if self.timersOff() == False:
            # # Set the framerate of the color animation
            self.framerate = 20

            # Duration of each pulse in second:
            self.seconds = 1  # seconds
            self.period = (2 * sympy.pi) / (self.framerate * self.seconds)
            self.sineValue = 3 * sympy.pi / 2

            # Define the biggest alpha value
            self.alphaMax = 255

            # Create a thread that can run the color animation:
            self.colorTimer = QtCore.QTimer()
            self.colorTimer.timeout.connect(lambda: self.alphaWave())

            # Apply the framerate
            self.colorTimer.setInterval(int(1000 / self.framerate))
            self.colorTimer.start()

    # Function that creates a sinewave
    def alphaWave(self):

        greenTime   = 30 * 60  # 30 minutes
        redTime     = 10 * 60  # 10 minutes
        pulse = sympy.sin(self.sineValue)
        pulse = float((pulse + 1) / 2)
        self.sineValue += self.period
        self.alpha = int(self.alphaMax * pulse)

        if self.sineValue == 7*sympy.pi/2:
            self.sineValue = 3*sympy.pi/2

        if self.timersOff() == True:
            self.colorTimer.stop()

        self.changeColors()

    # Change the colors of the timerframe in according to the alphaWave
    def changeColors(self):

        # Define time intervals:
        greenTime = 15 * 60  # 30 minutes
        redTime = 5 * 60  # 10 minutes

        # Change the color of all rooms in synchronization
        for i in range(1,6):

                if self.rooms["room"+f"{i}"].timer_counter_num >= greenTime:

                    self.rooms["room"+f"{i}"].timerframe.setStyleSheet(f"""  border-radius:40px; background:none; border:2px solid;
                                                                border-color: qlineargradient(spread:reflect, x1:0.5, y1:0, x2:1,
                                                                y2:0, stop:0 rgba(0, {self.alpha}, 0, {self.alpha / 2}), 
                                                                stop:1 rgba(120, 255, 120, {(self.alpha + 200) / 2}));""")

                elif self.rooms["room"+f"{i}"].timer_counter_num >= redTime:

                    self.rooms["room"+f"{i}"].timerframe.setStyleSheet(f"""  border-radius:40px; background:none; border:2px solid;
                                                                border-color: qlineargradient(spread:reflect, x1:0.5, y1:0, x2:1,
                                                                y2:0, stop:0 rgba({self.alpha}, 255, 0, {self.alpha / 2}), 
                                                                stop:1 rgba(255, 255, 0, {(self.alpha + 200) / 2}));""")

                elif self.rooms["room"+f"{i}"].timer_counter_num <= redTime and self.rooms["room"+f"{i}"].timer_counter_num > 0:

                    self.rooms["room"+f"{i}"].timerframe.setStyleSheet(f"""  border-radius:40px; background:none; border:2px solid;
                                                    border-color: qlineargradient(spread:reflect, x1:0.5, y1:0, x2:1,
                                                    y2:0, stop:0 rgba({self.alpha}, 0, 0, {self.alpha / 2}), 
                                                    stop:1 rgba(255, 120, 120, {(self.alpha + 200) / 2}));""")

                elif self.rooms["room"+f"{i}"].timer_counter_num == 0:
                    self.rooms["room"+f"{i}"].timerframe.setStyleSheet(f"""border-radius:40px; background:none; border:2px solid;
                                                                          border-color: rgb(255, 255, 255, 255);""")

    # Configure buttons
    def buttonConfig(self):

        # Configure start-buttons to color function:
        for i in range(1, 6):
            self.rooms["room" + f"{i}"].start.clicked.connect(              lambda: self.timerColors())
            self.rooms["room" + f"{i}"].textenter.returnPressed.connect(    lambda: self.timerColors())

        ################################################################################################################
        #Configure the plus and minus buttons for each room. This got buggy with a for loop
        ################################################################################################################

        ##### Plus

        self.rooms["room1"].plus.clicked.connect(lambda:    self.overview.patients.addTime  (
                                                                self.rooms["room1"].pasientsvarlabel.text(),
                                                                self.rooms["room1"].textenter.text(),
                                                                self.rooms["room1"].timer_counter_num
                                                )                                           )
        self.rooms["room1"].plus.clicked.connect(lambda:    self.rooms["room1"].addTime()   )

        #### Minus

        self.rooms["room1"].minus.clicked.connect(lambda:    self.overview.patients.subTime  (
                                                                self.rooms["room1"].pasientsvarlabel.text(),
                                                                self.rooms["room1"].textenter.text(),
                                                                self.rooms["room1"].timer_counter_num
                                                )                                           )
        self.rooms["room1"].minus.clicked.connect(lambda:    self.rooms["room1"].negTime()   )










        self.rooms["room2"].plus.clicked.connect(
            lambda: self.addTime(self.rooms["room2"].pasientsvarlabel.text(),
                                 self.rooms["room2"].textenter.text()))
        self.rooms["room2"].plus.clicked.connect(
            lambda: self.overview.patients.addTime( self.rooms["room2"].pasientsvarlabel.text(),
                                            self.rooms["room2"].textenter.text()))

        self.rooms["room3"].plus.clicked.connect(
            lambda: self.addTime(self.rooms["room3"].pasientsvarlabel.text(),
                                 self.rooms["room3"].textenter.text()))
        self.rooms["room3"].plus.clicked.connect(
            lambda: self.overview.patients.addTime( self.rooms["room3"].pasientsvarlabel.text(),
                                            self.rooms["room3"].textenter.text()))


        self.rooms["room4"].plus.clicked.connect(
            lambda: self.addTime(self.rooms["room4"].pasientsvarlabel.text(),
                                 self.rooms["room4"].textenter.text()))
        self.rooms["room4"].plus.clicked.connect(
            lambda: self.overview.patients.addTime(self.rooms["room4"].pasientsvarlabel.text(),
                                            self.rooms["room4"].textenter.text()))

        self.rooms["room5"].plus.clicked.connect(
            lambda: self.addTime(self.rooms["room5"].pasientsvarlabel.text(),
                                 self.rooms["room5"].textenter.text()))
        self.rooms["room5"].plus.clicked.connect(
            lambda: self.overview.patients.addTime( self.rooms["room5"].pasientsvarlabel.text(),
                                            self.rooms["room5"].textenter.text()))

    # Make a global clock
    def clock(self):

        # Make a string with the current time
        def runClock():
            t = time.localtime()
            self.time = time.strftime("%H:%M:%S", t)
            self.title.setText(self._translate("MainWindow", f"  {self.time}"))

        # Run the string function once so the clock appears right from opening
        runClock()

        # Create the timer that runs the clock once a second
        self.clock = QtCore.QTimer()
        self.clock.timeout.connect(runClock)
        self.clock.timeout.connect(lambda: self.patient2Room())
        self.clock.setInterval(1000)
        self.clock.start()

    #Function that moves patients from the waiting list to thir specified treatment room
    # when the time for treatment has come
    def patient2Room(self):

        # Fetch the global current time and turn it into an integer value consisting of minutes from midnight:
        hours, minutes, seconds = self.time.split(':')
        self.clockNum           = int(minutes) + (int(hours) * 60)

        # Only run this function if the dictionary is not empty. If not the program would crash on opening since
        # no patients would be added yet
        if self.overview.patients.dict != {}:

            # Iterate through the patient schedule
            for i in self.overview.patients.dict:

                #Make a string that decides which room the for loop is at (index 1 = roomnumber)
                if self.overview.patients.dict[i][1] == "PET-Scan":
                    room = "room5"
                else:
                    room = f"room{self.overview.patients.dict[i][1]}"

                # Convert the scheduled time to minutes past midnight
                Hours, Minutes  = self.overview.patients.dict[i][0].split(':')
                patienttime     = (int(Hours)*60) + int(Minutes)

                # Make a list with all minutes from pasienttime to pasienttime+45
                timebuffer = []
                for j in range(patienttime, patienttime+45):
                    timebuffer.append(j)


                petTid = str(datetime.timedelta(minutes=(patienttime + 45)))
                if len(petTid) == 7:
                    time = f"0{petTid}"
                petTid = petTid[:5]


            # If the time (at keyword index 0) = current time:
                # switch out the label on patients room (keyword index 1)
                if self.clockNum in timebuffer:

                    # Only add the new patient if the old patient is finished
                    if self.rooms[room].timer_counter_num == 0 or self.rooms[room].pasientsvarlabel.text() == i:

                        self.rooms[room].pasientsvarlabel.setText(self._translate("MainWindow", f"{i}"))
                        self.rooms[room].textenter.setEnabled(True)

                        # If the treatment isn't startet yet, the status is "Waiting for treatment"
                        if self.rooms[room].timer_counter_num == 0 and self.rooms[room].treatmentstarted == False:

                            self.rooms[room].statussvarlabel.setText(self._translate("MainWindow", "Venter på injeksjon"))

                        # When the treatment is over status is "Waiting for PET-Scan
                        elif self.rooms[room].timer_counter_num == 0:

                            self.rooms[room].statussvarlabel.setText(
                                self._translate("MainWindow", "Avventer PET-Scan"))
                            self.rooms[room].treatmentstarted = False

                        # When the treatment is started and there is more than 15 min left: the status is "Under treatment"
                        elif self.rooms[room].timer_counter_num >= (15 * 60):

                            self.rooms[room].statussvarlabel.setText(self._translate("MainWindow", "Under behandling"))

                        # When there is less than 15 minutes left, status is "WC and water"
                        elif self.rooms[room].timer_counter_num < (15 * 60) and self.rooms[room].timer_counter_num > 0:

                            self.rooms[room].statussvarlabel.setText(self._translate("MainWindow", "Vann og WC"))

                        # Next treatment is patients.dict index 0 - the originally scheduled time for the PET-Scan plus
                        # any possible delays
                        self.rooms[room].nestebehsvarlabel.setText(self._translate("MainWindow", f"{petTid}"))
