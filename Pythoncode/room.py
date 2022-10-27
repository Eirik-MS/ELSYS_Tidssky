from PyQt5 import QtCore, QtGui, QtWidgets
import Bakgrunnsbilde
import datetime


class Room(QtWidgets.QFrame):
    def __init__(self, *args, **kwargs):

        #### Timer global values

        self.timer_counter_num = 0
        self.stopwatch_counter_num = 0
        self.stopwatch_running = False
        self.timer_running = False

########################################################################################################################
# Create the main frame
########################################################################################################################

        QtWidgets.QFrame.__init__(self, *args, **kwargs)
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
        font.setPointSize(10)
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
        font.setPointSize(10)
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
        font.setPointSize(10)
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
        font.setPointSize(10)
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
        font.setPointSize(10)
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
        font.setPointSize(10)
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
        font.setPointSize(10)
        self.nestebehsvarlabel.setFont(font)
        self.nestebehsvarlabel.setStyleSheet("background:none;""color: rgb(255, 255, 255);")

        # Set grid layout

        self.verticalLayout_12.addWidget(self.nestebehsvarlabel)
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
        self.timerframe.setStyleSheet("border-radius:40px;""background:none;""border:2px solid;"
                                      "border-color: qlineargradient(spread:reflect, x1:0.5, y1:0, x2:1, "
                                      "y2:0, stop:0 rgba(255, 2, 2, 255), stop:1 rgba(255, 120, 120, 255));")

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
        font.setPointSize(35)
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
        font.setPointSize(10)
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
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.stop.setFont(font)

        self.stop.setStyleSheet("QPushButton{\n""border:1px solid;\n""border-color: rgb(39, 39, 39);\n"
                                "border-radius:0px;\n""border-radius:15px;\n""background-color: rbg(0,0,0,80);\n"
                                "    color: rgb(217, 217, 217);\n""}\n""QPushButton:hover{\n"
                                "background-color: rgba(0, 0, 0, 120);\n""}")

        self.horizontalLayout_11.addWidget(self.stop)

        ################################################################################################################
        # Create the reset button
        #################################################################################################################

        self.reset = QtWidgets.QPushButton(self.startstopframe)

        self.reset.setMinimumSize(QtCore.QSize(50, 30))
        self.reset.setMaximumSize(QtCore.QSize(50, 30))

        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
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

        ################################################################################################################
        # Create the minus time button
        #################################################################################################################

        self.minus = QtWidgets.QPushButton(self.addtimeframe)

        self.minus.setMinimumSize(QtCore.QSize(30, 30))
        self.minus.setMaximumSize(QtCore.QSize(30, 30))

        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
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
        font.setPointSize(10)
        self.textenter.setFont(font)
        self.textenter.setStyleSheet("border-radius:5px;\n""background-color: rgba(0, 0, 0, 120); \n"
                                     "color: rgb(255, 255, 255);")

        self.textenter.setAlignment(QtCore.Qt.AlignCenter)
        self.horizontalLayout_6.addWidget(self.textenter)

        ################################################################################################################
        # Create the plus time button
        #################################################################################################################

        self.plus = QtWidgets.QPushButton(self.addtimeframe)

        self.plus.setMinimumSize(QtCore.QSize(30, 30))
        self.plus.setMaximumSize(QtCore.QSize(30, 30))

        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
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

################################################################################################################
# This one thing I have no idea of what does
#################################################################################################################

        QtCore.QMetaObject.connectSlotsByName(self)

################################################################################################################
# Translate protocol
#################################################################################################################

        _translate = QtCore.QCoreApplication.translate
        self.label_2.setText(_translate("MainWindow", "Injeksjonsrom 1"))
        self.pasientlabel.setText(_translate("MainWindow", "Pasient:"))
        self.pasientsvarlabel.setText(_translate("MainWindow", "Magnus Støleggen"))
        self.statuslabel.setText(_translate("MainWindow", "Status"))
        self.statussvarlabel.setText(_translate("MainWindow", "Under behandling"))
        self.nestebehlabel.setText(_translate("MainWindow", "Neste behandling"))
        self.nestebehsvarlabel.setText(_translate("MainWindow", "PET-Scan - 14:45"))
        self.start.setText(_translate("MainWindow", "START"))
        self.stop.setText(_translate("MainWindow", "STOP"))
        self.reset.setText(_translate("MainWindow", "RESET"))
        self.minus.setText(_translate("MainWindow", "-"))
        self.plus.setText(_translate("MainWindow", "+"))

        ########### Set start button

        self.start.clicked.connect(lambda:timer('start'))
        self.lcdtime.setText(_translate("MainWindow", "0:00:00"))

        def timer(work):

                #### Define what to do if the start button is pressed:

                if work == 'start':

                        self.timer_running = True

                        if self.timer_counter_num == 0:

                                timer_time_str = self.textenter.text()
                                hours, minutes, seconds = timer_time_str.split(':')
                                minutes = int(minutes) + (int(hours) * 60)
                                seconds = int(seconds) + (minutes * 60)
                                self.timer_counter_num = self.timer_counter_num + seconds
                        #print('hei')
                        timer_counter()

                # elif work == 'stop':
                #         self.timer_running = False
                #         self.start.configure(state='normal')
                #         self.stop.configure(state='disabled')
                #         self.reset.configure(state='normal')
                #
                # elif work == 'reset':
                #         self.timer_running = False
                #         self.timer_counter_num = 0

        def timer_counter():
                def count():

                        if self.timer_running:

                                if self.timer_counter_num == 0:

                                        self.timer_running = False
                                        self.timer('reset')
                                        display = '00:00:00'

                                else:
                                        tt = datetime.timedelta(seconds=self.timer_counter_num)
                                        display = tt
                                        self.timer_counter_num -= 1


                        self.lcdtime.setText(_translate("MainWindow", f'{display}'))
                        self.timer = QtCore.QTimer()
                        self.timer.timeout.connect(count)
                        self.timer.setInterval(1000)  # 1000ms = 1s
                        self.timer.start()


                count()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Room()
    ui.show()
    sys.exit(app.exec_())
