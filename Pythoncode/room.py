from PyQt5 import QtCore as qc, QtGui as qg, QtWidgets as qw
import datetime


class Room(qw.QFrame):

    # Initialization sequence
    def __init__(self, Master, gui, ow):

        # Instance variable that defines the room number:
        self.roomnr = 1

        # Initialize the main frame:
        qw.QFrame.__init__(self, Master)

        # Initialize global timer variables:
        self.timer_counter_num = 0
        self.timer_running = False

        # Initialize global translation variable:
        self._translate = qc.QCoreApplication.translate

        # Run boot-up functions:
        self.createMainframe()

        # Confiugre buttons:
        self.textenter.returnPressed.connect(lambda: self.timerFunctions('start', ow, gui))
        self.start.clicked.connect( lambda: self.timerFunctions('start', ow, gui))
        self.stop.clicked.connect(  lambda: self.timerFunctions('stop', ow, gui))
        self.reset.clicked.connect( lambda: self.timerFunctions('reset', ow, gui))
        self.plus.clicked.connect(  lambda: self.addTime(ow))
        self.minus.clicked.connect( lambda: self.negTime(ow, gui))
        self.startPet.clicked.connect(lambda: self.patient2pet(name=self.pasientsvarlabel.text(), ow=ow, gui=gui))

       # Connect the global glock to the patient2room() function

        gui.clock.timeout.connect(lambda: self.patient2room(gui, ow))

########################################################################################################################
#   Configuring boot-up functions. Each part of the object has it's own function. One function runs the next and so on
#   These could all be in one function, but i found it much more tidy to divide them into distinct functions.
########################################################################################################################
    def createMainframe(self):

        self.setObjectName("MainWindow")

        # Set the size of the window and size constraints

        self.setGeometry(qc.QRect(0, 0, 259, 316))
        self.setMinimumSize(qc.QSize(250, 0))
        self.setMaximumSize(qc.QSize(16777215, 16777215))

        # Set Grid layout

        self.verticalLayout_4 = qw.QVBoxLayout(self)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(1)
        self.verticalLayout_4.setObjectName("verticalLayout_4")

        ################################################################################################################
        # Create the title label
        ################################################################################################################

        self.roomlabel = qw.QFrame(self)

        # Size constraints

        self.roomlabel.setMinimumSize(qc.QSize(0, 25))
        self.roomlabel.setMaximumSize(qc.QSize(16777215, 25))

        # Set style

        self.roomlabel.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.539773, y1:1, x2:0.523, y2:0, stop:0.676136 rgba(0, 0, 0, 120), "
                                     "stop:0.881356 rgba(112, 112, 112, 60), stop:1 rgba(255, 255, 255, 0));" "border-radius:2px;" "border-bottom-left-radius:15px;"
                                     "border-bottom-right-radius:15px;")

        # Set grid layout

        self.verticalLayout_6 = qw.QVBoxLayout(self.roomlabel)
        self.verticalLayout_6.setContentsMargins(0, 4, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")

        # Create the label itself and define font and style

        self.label_2 = qw.QLabel(self.roomlabel)
        font = qg.QFont()
        font.setFamily("Roboto")
        font.setPixelSize(13)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)

        self.font = font
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background:none;""color: rgb(255, 255, 255);")

        # Add label widget to the layout
        self.verticalLayout_6.addWidget(self.label_2, 0, qc.Qt.AlignHCenter)
        self.verticalLayout_4.addWidget(self.roomlabel)


        self.pasientstatus = qw.QFrame(self)

        # Set size constraints and style

        self.pasientstatus.setMinimumSize(qc.QSize(0, 85))
        self.pasientstatus.setMaximumSize(qc.QSize(16777215, 85))
        self.pasientstatus.setStyleSheet("border-radius:15px;""border-bottom-right-radius:0px;""border-bottom-left-radius:0px;""background-color: rgba(0, 0, 0, 120);")

        # Set grid Layout
        self.gridLayout = qw.QGridLayout(self.pasientstatus)
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.gridLayout.setHorizontalSpacing(1)
        self.gridLayout.setVerticalSpacing(3)

        ################################################################################################################
        # Create the frame with "Pasient:" and "<patient name>"
        ################################################################################################################

        self.pasientframe = qw.QFrame(self.pasientstatus)
        self.pasientframe.setStyleSheet("border-radius:0px;""border-top-left-radius:10px;""border-bottom-left-radius:10px;")
        self.pasientframe.setMaximumSize(75,85)

        # Set grid layout

        self.verticalLayout_7 = qw.QVBoxLayout(self.pasientframe)
        self.verticalLayout_7.setContentsMargins(8, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)


        # Create the label that displays "Pasient:"

        self.pasientlabel = qw.QLabel(self.pasientframe)
        font = qg.QFont()
        font.setFamily("Roboto Cn")
        font.setPixelSize(13)
        self.pasientlabel.setFont(font)
        self.pasientlabel.setStyleSheet("background:none;""color: rgb(217, 217, 217);")
        self.verticalLayout_7.addWidget(self.pasientlabel, 0, qc.Qt.AlignLeft)
        self.gridLayout.addWidget(self.pasientframe, 0, 0, 1, 1)

        # Create the frame with the patients's name/pseudonym

        self.pasientsvarframe = qw.QFrame(self.pasientstatus)
        self.pasientsvarframe.setStyleSheet("border-radius:0px;""border-top-right-radius:10px;""border-bottom-right-radius:10px;")
        self.verticalLayout_8 = qw.QVBoxLayout(self.pasientsvarframe)
        self.verticalLayout_8.setContentsMargins(8, 3, 0, 0)

        # Create the label with the patient's name/pseudonym

        self.pasientsvarlabel = qw.QLabel(self.pasientsvarframe)
        font = qg.QFont()
        font.setFamily("Roboto Cn")
        font.setPixelSize(13)
        self.pasientsvarlabel.setFont(font)
        self.pasientsvarlabel.setStyleSheet("background:none;""color: rgb(255, 255, 255);")
        self.pasientsvarlabel.setAlignment(qc.Qt.AlignLeft)
        self.verticalLayout_8.addWidget(self.pasientsvarlabel)
        self.gridLayout.addWidget(self.pasientsvarframe, 0, 1, 1, 1)

        ################################################################################################################
        # Create the frame with "Status:" and "<patient status>"
        ################################################################################################################

        self.statusframe = qw.QFrame(self.pasientstatus)
        self.statusframe.setStyleSheet("border-radius:15px;""border-top-left-radius:10px;"
                                       "border-bottom-left-radius:10px;")

        # Set grid layout

        self.verticalLayout_9 = qw.QVBoxLayout(self.statusframe)
        self.verticalLayout_9.setContentsMargins(8, 0, 0, 0)
        self.verticalLayout_9.setSpacing(0)

        # Create label to display "Status:"

        self.statuslabel = qw.QLabel(self.statusframe)
        font = qg.QFont()
        font.setFamily("Roboto Cn")
        font.setPixelSize(13)
        self.statuslabel.setFont(font)
        self.statuslabel.setStyleSheet("background:none;""color: rgb(217, 217, 217);")
        self.verticalLayout_9.addWidget(self.statuslabel, 0, qc.Qt.AlignLeft)
        self.gridLayout.addWidget(self.statusframe, 1, 0, 1, 1)

        # Create the frame to display "<patient status>"

        self.statussvarframe = qw.QFrame(self.pasientstatus)
        self.statussvarframe.setStyleSheet("border-radius:0px;""border-top-right-radius:10px;""border-bottom-right-radius:10px;")

        # Set grid layout

        self.verticalLayout_10 = qw.QVBoxLayout(self.statussvarframe)
        self.verticalLayout_10.setContentsMargins(8, 3, 0, 0)
        self.verticalLayout_10.setSpacing(0)

        # Create the button to declare injection treatment finished:
        self.startPet = qw.QPushButton()
        self.startPet.setText("Trykk for å sende til PET-Scan")
        self.startPet.setFont(font)
        self.startPet.setMinimumSize(0, 23)
        self.startPet.setStyleSheet(""" 
                                    QPushButton:disabled   {    background-color:   rgba(255, 255, 255, 80)         }
                                    QPushButton:hover      {    background-color:   rgba(0, 0, 0, 120);             }
                                    QPushButton:pressed    {    background-color:   rgba(0, 0, 0, 200);             } 
                                    QPushButton            {    background-color:   rgb(0,0,0,80); 
                                                                border-color:       rgb(39, 39, 39);
                                                                border:             1px solid;   
                                                                border-top-right-radius:      10px;  
                                                                border-bottom-rightradius:      15px;
                                                                color:              rgba(255, 255, 255, 255)        }      
                                """)


        # Create the label to display "<patient status>"

        self.statussvarlabel = qw.QLabel(self.statussvarframe)
        font = qg.QFont()
        font.setFamily("Roboto Cn")
        font.setPixelSize(13)
        self.statussvarlabel.setFont(font)
        self.statussvarlabel.setStyleSheet("background:none;""color: rgb(255, 255, 255);")
        self.statussvarlabel.setAlignment(qc.Qt.AlignLeft)

        # Set grid layout

        self.verticalLayout_10.addWidget(self.statussvarlabel, 0, qc.Qt.AlignLeft)
        self.gridLayout.addWidget(self.statussvarframe, 1, 1, 1, 1)

        ################################################################################################################
        # Create the frame with "Neste behandling:" and "<next treatment>"
        ################################################################################################################

        self.nestebeh = qw.QFrame(self.pasientstatus)
        self.nestebeh.setStyleSheet("border-radius:0px;""border-top-left-radius:10px;""border-bottom-left-radius:10px;")

        # Set grid layout

        self.verticalLayout_11 = qw.QVBoxLayout(self.nestebeh)
        self.verticalLayout_11.setContentsMargins(8, 0, 0, 0)
        self.verticalLayout_11.setSpacing(0)

        # Create the label to display "Neste behandling:"

        self.nestebehlabel = qw.QLabel(self.nestebeh)
        font = qg.QFont()
        font.setFamily("Roboto Cn")
        font.setPixelSize(13)
        self.nestebehlabel.setFont(font)
        self.nestebehlabel.setStyleSheet("background:none;""color: rgb(217, 217, 217);")

        # Set grid layout

        self.verticalLayout_11.addWidget(self.nestebehlabel, 0, qc.Qt.AlignLeft)
        self.gridLayout.addWidget(self.nestebeh, 2, 0, 1, 1)

        # Create frame to display "<next treatment>"

        self.nestebehsvarframe = qw.QFrame(self.pasientstatus)
        self.nestebehsvarframe.setStyleSheet("border-radius:0px;""border-top-right-radius:10px;""border-bottom-right-radius:10px;")

        # Set grid layout

        self.verticalLayout_12 = qw.QVBoxLayout(self.nestebehsvarframe)
        self.verticalLayout_12.setContentsMargins(8, 0, 0, 0)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")

        # Create label to display "<next treatment>"

        self.nestebehsvarlabel = qw.QLabel(self.nestebehsvarframe)
        font = qg.QFont()
        font.setFamily("Roboto Cn")
        font.setPixelSize(13)
        self.nestebehsvarlabel.setFont(font)
        self.nestebehsvarlabel.setStyleSheet("background:none;""color: rgb(255, 255, 255);")

        # Set grid layout

        self.verticalLayout_12.addWidget(self.nestebehsvarlabel, 0, qc.Qt.AlignLeft)
        self.gridLayout.addWidget(self.nestebehsvarframe, 2, 1, 1, 1)
        self.verticalLayout_4.addWidget(self.pasientstatus)



        self.timer = qw.QFrame(self)
        self.timer.setStyleSheet("border-radius:0px;""background-color: rgba(0, 0, 0, 120);"
                                 "border-bottom-left-radius:15px;""border-bottom-right-radius:15px;")

        # Set grid layout

        self.verticalLayout_44 = qw.QVBoxLayout(self.timer)
        self.verticalLayout_44.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_44.setSpacing(4)

        # Create frame to containt the timer label

        self.timerframe = qw.QFrame(self.timer)
        self.timerframe.setMinimumSize(qc.QSize(250, 80))
        self.timerframe.setMaximumSize(qc.QSize(250, 80))

        self.timerframe.setStyleSheet(f"""border-radius:40px; background:none; border:2px solid;
                                          border-color: rgba(255, 255, 255, 255)""")

        # Set grid layout

        self.verticalLayout_49 = qw.QVBoxLayout(self.timerframe)
        self.verticalLayout_49.setObjectName("verticalLayout_49")

################################################################################################################
# Create the timer label
#################################################################################################################


        self.lcdtime = qw.QLabel(self.timerframe)

        # Set style and font

        self.lcdtime.setStyleSheet("color: rgba(255, 255, 255, 200);border:none;")
        font = qg.QFont()
        font.setFamily("Roboto Cn")
        font.setPixelSize(45)
        self.lcdtime.setFont(font)

        # Set grid layout

        self.verticalLayout_49.addWidget(self.lcdtime)
        self.lcdtime.setAlignment(qc.Qt.AlignHCenter)
        self.lcdtime.setAlignment(qc.Qt.AlignCenter)
        self.verticalLayout_44.addWidget(self.timerframe, 0, qc.Qt.AlignHCenter)

################################################################################################################
# Create buttons
#################################################################################################################

        # Frame for start and stop

        self.startstopframe = qw.QFrame(self.timer)

        self.startstopframe.setMinimumSize(qc.QSize(0, 30))
        self.startstopframe.setMaximumSize(qc.QSize(16777215, 30))
        self.startstopframe.setStyleSheet("background:none;")

        self.horizontalLayout_11 = qw.QHBoxLayout(self.startstopframe)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setSpacing(0)

        ################################################################################################################
        # Create the start button
        #################################################################################################################

        self.start = qw.QPushButton(self.startstopframe)

        self.start.setMinimumSize(qc.QSize(50, 30))
        self.start.setMaximumSize(qc.QSize(50, 30))

        font = qg.QFont()
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

        self.stop = qw.QPushButton(self.startstopframe)

        self.stop.setMinimumSize(qc.QSize(50, 30))
        self.stop.setMaximumSize(qc.QSize(50, 30))

        font = qg.QFont()
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

        self.reset = qw.QPushButton(self.startstopframe)

        self.reset.setMinimumSize(qc.QSize(50, 30))
        self.reset.setMaximumSize(qc.QSize(50, 30))

        font = qg.QFont()
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

        self.addtimeframe = qw.QFrame(self.timer)

        self.addtimeframe.setMinimumSize(qc.QSize(0, 30))
        self.addtimeframe.setMaximumSize(qc.QSize(16777215, 30))

        self.addtimeframe.setStyleSheet("background:none")

        self.horizontalLayout_6 = qw.QHBoxLayout(self.addtimeframe)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")

        # Initialize the button as disabled:
        self.reset.setEnabled(False)

        ################################################################################################################
        # Create the minus time button
        #################################################################################################################

        self.minus = qw.QPushButton(self.addtimeframe)

        self.minus.setMinimumSize(qc.QSize(30, 30))
        self.minus.setMaximumSize(qc.QSize(30, 30))

        font = qg.QFont()
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

        self.textenter = qw.QLineEdit(self.addtimeframe)

        self.textenter.setMinimumSize(qc.QSize(0, 30))
        self.textenter.setMaximumSize(qc.QSize(120, 16777215))

        font = qg.QFont()
        font.setFamily("Roboto Cn")
        font.setPixelSize(13)
        self.textenter.setFont(font)
        self.textenter.setStyleSheet("border-radius:5px;\n" 
                                     "background-color: rgba(0, 0, 0, 120); \n"
                                     "color: rgb(255, 255, 255);")

        self.textenter.setAlignment(qc.Qt.AlignCenter)
        self.horizontalLayout_6.addWidget(self.textenter)

        # Create a layout inside the textenter:
        self.textenterlay = qw.QHBoxLayout(self.textenter)
        self.textenterlay.setContentsMargins(15, 0,0, 0)
        self.textenterlabel = qw.QLabel(self.textenter)
        self.textenterlabel.setFont(font)
        self.textenterlay.addWidget(self.textenterlabel)
        self.textenterlabel.setStyleSheet("background:none")
        self.textenter.setFont(font)



        # Create an input mask:
        self.textenter.setText("00:00:00")
        self.textenter.setInputMask("99:99:99")

        # Define the initial input validator
        self.reg_ex = qc.QRegExp("[0-2]{1}[0-3]{1}"+":"+"[0-5]{1}[0-9]{1}"+":"+"[0-5]{1}[0-9]{1}")
        self.input_validator1 = qg.QRegExpValidator(self.reg_ex, self.textenter)
        self.textenter.setValidator(self.input_validator1)

        # Define the input validator for when the timer is running:
        self.reg_ex2 = qc.QRegExp("[0-9]{2}")
        self.input_validator2 = qg.QRegExpValidator(self.reg_ex2, self.textenter)

        # Initialize enterbox as disabled
        self.textenter.setEnabled(False)


        ################################################################################################################
        # Create the plus time button
        #################################################################################################################

        self.plus = qw.QPushButton(self.addtimeframe)

        self.plus.setMinimumSize(qc.QSize(30, 30))
        self.plus.setMaximumSize(qc.QSize(30, 30))

        font = qg.QFont()
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

        qc.QMetaObject.connectSlotsByName(self)

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


# ########################################################################################################################
#   Configuring other functions:
# ########################################################################################################################

    # Tells the timer how to operate
    def timerFunctions(self, work, ow, gui):

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

            gui.colorTimer.timeout.connect(lambda: self.changeColors(gui, ow))

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
            #gui.colorTimer.timeout.disconnect(self.changeColors)

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
                display = f"0{display}"
                self.timer_counter_num -= 1

        # Display the current time
        self.lcdtime.setText(self._translate("MainWindow", f'{display}'))

        # Create a thread that can run the count() function once a second:
        # Create a thread that can run the count() function once a second:
        self.timer = qc.QTimer()
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
    def negTime(self, ow, gui):

        timeint = int(self.textenter.text())
        sec = timeint * 60

        if self.timer_counter_num - sec <= 0:

            ow.patients.subTime(self.pasientsvarlabel.text(), self.timer_counter_num, self.timer_counter_num)
            nexttreatment = ow.patients.string2Min(ow.patients.dict[f'{self.pasientsvarlabel.text()}'][0])
            nexttreatment = nexttreatment + 45
            nexttreatment = ow.patients.min2String(nexttreatment)
            self.nestebehsvarlabel.setText(self._translate("MainWindow", f"{nexttreatment}"))
            self.timerFunctions("reset", ow, gui)

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

        # Iterate through the patient schedule to move patients from the schedule to the designated room
        for i in ow.patients.dict:

            # Don't run the code below for the PET-Scan room:
            if self.roomnr == "PET-Scan" or ow.patients.dict[i][5]==True:
                continue

            # Convert the scheduled time to minutes past midnight
            Hours, Minutes = ow.patients.dict[i][0].split(':')
            patienttime = (int(Hours) * 60) + int(Minutes)


            # Run code below only if the clock is in the period where the patient is scheduled to be treated (or if the treatment isn't finished yet)
            if ow.patients.dict[i][1] == self.roomnr   and     ow.patients.dict[i][4]==False:# and  (    (gui.clockNum >= patienttime)           and     ( ((patienttime+45)>=gui.clockNum) or self.timer_counter_num!=0)) :
                pass
            else:
                continue


            # Find the time for PET-Scan:
            petTime = str(datetime.timedelta(minutes=(patienttime + 45)))
            if len(petTime) == 7:
                petTime = f"0{petTime}"
            petTime = petTime[:5]

            # Don't swap patient if the countdown isn't finished
            self.pasientsvarlabel.setText(self._translate("MainWindow", f"{i}"))
            self.textenter.setEnabled(True)

            ################################
            #     Configure status text    #
            ################################

            # If the treatment isn't startet yet, the status is "Waiting for treatment"
            if ow.patients.dict[i][3] == False:

                self.statussvarlabel.setText(self._translate("MainWindow", "Venter på injeksjon"))

            # When the treatment is over status is "Waiting for PET-Scan
            elif self.timer_counter_num == 0 and ow.patients.dict[i][4] == False:

                ow.patients.dict[i][4] = True

                self.statussvarlabel.setParent(None)
                self.startPet.setParent(self.statussvarframe)
                self.verticalLayout_10.setContentsMargins(0,0,0,0)
                self.verticalLayout_10.addWidget(self.startPet)
                #gui.colorTimer.timeout.disconnect(self.changeColors)

            # When the treatment is started and there is more than 15 min left: the status is "Under treatment"
            elif self.timer_counter_num >= (15 * 60):

                self.statussvarlabel.setText(self._translate("MainWindow", "Under behandling"))

            # When there is less than 15 minutes left, status is "WC and water"
            elif self.timer_counter_num < (15 * 60) and self.timer_counter_num > 0:

                self.statussvarlabel.setText(self._translate("MainWindow", "Vann og WC"))

            # Next treatment is patients.dict index 0 + 45 min and any possible delays
            self.nestebehsvarlabel.setText(self._translate("MainWindow", f"{petTime}"))
    def changeColors(self, gui, ow):

        # Define time intervals:
        greenTime = 15 * 60  # 30 minutes
        redTime = 5 * 60  # 10 minutes

        # Only run code below if the patient label is not empty. If it does the program crashes
        if self.pasientsvarlabel.text() == "":
            return

        # Change the color of all rooms in synchronization

        if self.timer_counter_num >= greenTime:

            self.timerframe.setStyleSheet(f"""  border-radius:40px; background:none; border:2px solid;
                                                                border-color: qlineargradient(spread:reflect, x1:0.5, y1:0, x2:1,
                                                                y2:0, stop:0 rgba(0, {gui.alpha}, 0, {gui.alpha / 2}), 
                                                                stop:1 rgba(120, 255, 120, {(gui.alpha + 200) / 2}));""")

        elif self.timer_counter_num >= redTime:

            self.timerframe.setStyleSheet(f"""  border-radius:40px; background:none; border:2px solid;
                                                                border-color: qlineargradient(spread:reflect, x1:0.5, y1:0, x2:1,
                                                                y2:0, stop:0 rgba({gui.alpha}, 255, 0, {gui.alpha / 2}), 
                                                                stop:1 rgba(255, 255, 0, {(gui.alpha + 200) / 2}));""")

        elif self.timer_counter_num <= redTime and self.timer_counter_num > 0:

            self.timerframe.setStyleSheet(f"""  border-radius:40px; background:none; border:2px solid;
                                                    border-color: qlineargradient(spread:reflect, x1:0.5, y1:0, x2:1,
                                                    y2:0, stop:0 rgba({gui.alpha}, 0, 0, {gui.alpha / 2}), 
                                                    stop:1 rgba(255, 120, 120, {(gui.alpha + 200) / 2}));""")

        elif self.timer_counter_num == 0:
            self.timerframe.setStyleSheet(f"""border-radius:40px; background:none; border:2px solid;
                                                                          border-color: rgb(255, 255, 255, 255);""")
        if ow.patients.dict[self.pasientsvarlabel.text()][4] == True:

            self.startPet.setStyleSheet(f""" 
                                    QPushButton:hover      {{    background-color:   rgba(252, 190, 3, 150);           }}
                                    QPushButton:pressed    {{    background-color:   rgba(252, 190, 3, 100);             }} 
                                    QPushButton            {{    background-color:   rgba(252, 190, 3, {gui.alpha}); 
                                                                border-color:       rgb(39, 39, 39);
                                                                border:             none;   
                                                                border-top-right-radius:      10px;  
                                                                border-bottom-rightradius:      15px;
                                                                color:              rgba(255, 255, 255, 255)        }}      
                                """)
    def patient2pet(self, name, ow, gui):

        ow.patients.dict[name][5] = True

        if gui.rooms["room5"].timer_counter_num == 0:
            gui.rooms["room5"].pasientsvarlabel.setText(name)
            gui.rooms["room5"].statussvarlabel.setText("Venter på behandling")
            gui.rooms["room5"].textenter.setEnabled(True)
            self.startPet.setParent(None)
            self.verticalLayout_10.setContentsMargins(8, 3, 0, 0)
            self.statussvarlabel.setParent(self.statussvarframe)
            self.verticalLayout_10.addWidget(self.statussvarlabel)
            self.statussvarlabel.setText("")
            self.pasientsvarlabel.setText("")
            self.nestebehsvarlabel.setText("")
            self.textenter.setEnabled(False)
        else:
            self.startPet.setText("I kø til PET-Scan...")







