from customQtWidgets import *
from BlurWindow.blurWindow import blur
import datetime
import sympy
import sys

class Main(qw.QMainWindow):
    def __init__(self):

        # Bool to know if the window is maximized or normal
        self.maximized = False

        # initialize the main window, remove frames, make translucent, set size
        qw.QMainWindow.__init__(self)
        self.setWindowFlags(qc.Qt.FramelessWindowHint), self.setAttribute(qc.Qt.WA_TranslucentBackground), self.resize(1500, 1000)

        hWnd = self.winId()
        blur(hWnd)
        blur(False)

        # Run the gui init
        GUI.init(self)

        # Link some functions
        self.mainframe["1"].mouseMoveEvent = self.moveWindow
        functions.buttonconfig(self)

    # Make sure the window can be moved
    def moveWindow(self,event):

            if event.buttons() == qc.Qt.LeftButton:

                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

    # Define function every time the mouse is pressed
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

class functions(Main):

    def max_restore(self):

        if self.maximized == False:
            self.cw.radius(0),      self.cf.radius(0),          self.mainframe["1"].customradius(0, 0, 0, 0),       self.showMaximized()
            self.maximized = True

        else:
            self.cw.radius(10),     self.cf.radius(10),         self.mainframe["1"].customradius(10, 10, 0, 0),     self.showNormal()
            self.resize(self.width() + 1, self.height() + 1)
            self.maximized = False

    def buttonconfig(self):
        # close/maximize/minimize buttons:
        self.button["1"].clicked.connect(self.showMinimized),   self.button["2"].clicked.connect(lambda: functions.max_restore(self))
        self.button["3"].clicked.connect(self.close)

class GUI(Main):
    def init(self):

#### Init a centralwidget, add to main, init central frame, add to central widget
        self.cw  =  mywidget(self, "v", radius=10)
        self.cf  =  myframe(self.cw, "v", "cf", add=True, radius=10, color=(0,0,0, 100))
        self.setCentralWidget(self.cw)#,  self.cf.addstyle("image", "border-image: url(:/images/Background3.jpg);")

#### Create 4 main frames
        mainframe = {}
        for i in range(1, 5):
            mainframe[str(i)] = myframe(self.cf, "h", f"mainframe{i}", add=True)

        mainframe["1"].customradius(9, 9, 0, 0),    mainframe["1"].setFixedHeight(30),      mainframe["1"].bg(0, 0, 0, 100)
        mainframe["4"].customradius(0, 0, 10, 10),  mainframe["4"].setFixedHeight(20),      mainframe["2"].margins(10,10,10,0)
        mainframe["2"].spacing(10),                 mainframe["3"].margins(10,10,10,10),    mainframe["2"].setMaximumHeight(350)
        self.mainframe = mainframe

#### Create 3 frames in the top mainframe
        topframe = {}
        for i in range(1, 4):
            topframe[str(i)] = myframe(mainframe["1"], "h", f"topframe{i}", add=True)

        topframe["3"].setFixedWidth(200),           topframe["3"].margins(135, 0, 0, 0)
        topframe["1"].customradius(0, 0, 10, 0),    topframe["1"].setFixedWidth(500)
        self.topframe = topframe

#### Create three buttons in the top right frame, set radius, individual colors, hover- and pressed color
        button = {}
        for i in range(1, 4):
            button[str(i)] = mybutton(topframe["3"],    objectName=f"button{i}",            radius=7, add=True, align="center")
            button[str(i)].setFixedSize(14, 14)

        button["1"].bg(255, 255, 0, 255),           button["1"].hcolor(255, 255, 0, 150),   button["1"].pcolor(255, 255, 0, 50)
        button["2"].bg(0, 255, 0, 255),             button["2"].hcolor(0, 255, 0, 150),     button["2"].pcolor(0, 255, 0, 50)
        button["3"].bg(255, 0, 0, 255),             button["3"].hcolor(255, 0, 0, 150),     button["3"].pcolor(255, 0, 0, 50)
        self.button = button

#### Create a title label
        title = mylabel(topframe["1"], font=("Roboto", "Light", 100), size=15, text="Logistikk PET-Scan St. Olavs", add=True, align="left")
        topframe["1"].margins(10, 0, 0, 0)

#### Create a schedule in the bottom middle frame from the Schedule() class
        self.schedule   = Schedule(mainframe["3"], self, "v", "sched", add=True)

#### Create five rooms from the Room() class in the top middle frame
        room    =   {}
        for i in range(1,6):
            room[str(i)]      =   Room(mainframe["2"], self, self.schedule.patients, "v", f"room{i}", add=True)
            room[str(i)].name =   str(i)
            room[str(i)].title.setText(f"Injeksjonsrom {i}"), room[str(i)].margins(2,2,2,2)

        room["5"].title.setText("PET-Scan")
        self.room = room

#### Create 2 frames in the bottom mainframe
        btmframe = {}
        for i in range(1, 3):
            btmframe[str(i)] = myframe(mainframe["4"], "v", f"btmframe{i}", add=True)
        btmframe["2"].setFixedWidth(20)

#### Create a label with credits
        credits = mylabel(btmframe["1"],    text="Av: Silnes, Chewiejczak, Nore, Singh Sidhu, Støleggen, Gripsgård",
                                            font=("Roboto", "Italic", 50), size=13, add=True, color=(255,255,255,100))
        btmframe["1"].margins(5, 0, 0, 0)

#### Add size-grip to the bottom right corner
        sizegrip = qw.QSizeGrip(btmframe["2"])
        sizegrip.setStyleSheet("background-color: rgba(0,0,0,0);"), btmframe["2"].lay.addWidget(sizegrip, 0, qc.Qt.AlignBottom)

#### Initialize the timer that runs the colorChange() function across all rooms. Set to 24fps:
        self.sineValue = 3 * sympy.pi / 2
        self.framerate = 20
        self.colortimer = Countdown(self, int(1000/20), "fps", pat=self.schedule.patients)
        self.colortimer.start()

    def run(self, pat):

        # Define max alpha value and set the period
        period, alphaMax   = ((2 * sympy.pi) / (self.framerate)),    255

        pulse = sympy.sin(self.sineValue)
        pulse = float((pulse + 1) / 2)
        self.sineValue += period
        alpha = int(alphaMax * pulse)

        if self.sineValue == 7 * sympy.pi / 2:
            self.sineValue = 3 * sympy.pi / 2

        for i in self.room:
            self.room[i].changeColors(alpha, pat)
        self.alpha = alpha

class Room(myframe):

    def __init__(self, Master, Main, pat, *args, **kwargs):

#### Initialize the timer object and essential variables for the timer to work, also the timer to run patient2room()
        self.timernum, self.timerr, self.timerOn = 0, Countdown(self, 1000, "time", master=pat), False
        self.p2r = Countdown(self, 1000, "p2r", master=pat, main=Main)
        self.p2r.start()

#### Initialize the room object as self

        myframe.__init__(self, Master, *args, **kwargs)
        self.name = "1"

#### Create central frame and add it to master layout
        rcf = myframe(self, "v", color=(0,0,0,120), radius=10, add=True, align="top")

#### Create five frames and add them verticaly
        mainframe = {}
        for i in range(1,6):
            if i == 2 or i == 3:
                mainframe[str(i)] = myframe(rcf, "g", f"rmainframe{i}", add=True)
            else:
                mainframe[str(i)] = myframe(rcf, "h", f"rmainframe{i}", add=True)

        mainframe["1"].setFixedHeight(30),      mainframe["2"].setFixedHeight(80),  mainframe["2"].spacing(1)
        mainframe["3"].setMaximumHeight(150),   mainframe["3"].margins(5,5,5,5),    mainframe["4"].spacing(5)
        mainframe["4"].margins(0,0,0,5),        mainframe["5"].spacing(5),          mainframe["5"].margins(0,0,0,10)

#### Create title
        self.title      = mylabel(mainframe["1"], text="Injeksjonsrom 1", align="center", size=14, add=True, font=("Roboto","Bold",100))

#### Create frames for statuses
        statusframe = {}
        for i in range(1, 7):
            statusframe[str(i)] = myframe(mainframe["2"],   "g",    f"statusframe{i}",      color=(255, 255, 255, 100))
            statusframe[str(i)].margins(4, 0, 0, 0)
        for i in [1, 3, 5]:
            statusframe[str(i)].setFixedWidth(63)

        # Fix custom corners
        statusframe["1"].customradius(5,0,0,0),                         statusframe["5"].customradius(0,0,0,5)
        statusframe["2"].customradius(0,5,0,0),                         statusframe["6"].customradius(0,0,5,0)
        # Add rooms to grid
        mainframe["2"].lay.addWidget(statusframe["1"], 0, 0),           mainframe["2"].lay.addWidget(statusframe["2"], 0, 1)
        mainframe["2"].lay.addWidget(statusframe["3"], 1, 0),           mainframe["2"].lay.addWidget(statusframe["4"], 1, 1)
        mainframe["2"].lay.addWidget(statusframe["5"], 2, 0),           mainframe["2"].lay.addWidget(statusframe["6"], 2, 1)
        mainframe["3"].margins(15,15,15,15)
        self.statusframe = statusframe
        # Add static text
        patient         = mylabel(statusframe["1"], text="Pasient:",    add=True,    font=("Roboto", "Normal", 100), size=12, align=qc.Qt.AlignLeft,   color=(255,255,255,255))
        status          = mylabel(statusframe["3"], text="Status:",     add=True,    font=("Roboto", "Normal", 100), size=12, align=qc.Qt.AlignLeft,   color=(255,255,255,255))
        neste           = mylabel(statusframe["5"], text="PET-Scan:",   add=True,    font=("Roboto", "Normal", 100), size=12, align=qc.Qt.AlignLeft,   color=(255,255,255,255))
        # Add dynamic text
        self.patient    = mylabel(statusframe["2"], "patient",          align="left",       add=True,    color=(255,255,255,255))
        self.status     = mylabel(statusframe["4"], "status",           align="left",                    color=(255,255,255,255))
        self.statusb    = mybutton(statusframe["2"],"statusb",                                           color=(255,255,255,0))
        self.neste      = mylabel(statusframe["6"], "neste",            align="left",       add=True,    color=(255,255,255,255))

        self.statusb.setMinimumHeight(25)
        statusframe["4"].lay.addWidget(self.status, 0, 0),              statusframe["4"].lay.addWidget(self.statusb, 0, 0)

#### Create frame for timer and timer text
        # Create a regular frame with label
        self.tframe     = myframe(  mainframe["3"], "v",    "tframe",       radius=20)
        self.timer      = mylabel(  self.tframe,            "timer",        align="center", text="00:00:00",    color=(255,255,255,180),
                                                                            font=("Roboto", "Thin", 100),       size=60,        add=True)
        # Create another label to be used as a feather/blur effect
        self.blurframe  = myframe(  mainframe["3"], "v",    "blurframe",    radius=20,      blur=True)
        self.blurtimer  = mylabel(  self.blurframe,         "blurtimer",    align="center", text="00:00:00",    color=(255,255,255,180),
                                                                            font=("Roboto", "Thin", 100),       size=60,        add=True)
        self.blurtimer.blur(True)
        # Add the elements to the grid
        mainframe["3"].lay.addWidget(self.blurframe, 0, 0),                 self.blurframe.blur(True, radius=5),      mainframe["3"].lay.addWidget(self.tframe, 0, 0)

        # Set some style from the timer frame
        self.tframe.addstyle(   "border",       "border: 2px solid; border-color: rgba(255,255,255,0);"),               self.tframe.setMinimumSize(280,105)
        self.blurframe.addstyle("border",       "border: 2px solid; border-color: rgba(255,255,255,0);")

#### Create start, stop, and reset buttons
        self.start  = mybutton(mainframe["4"],  radius=5,                   text="Start",               color=(255,255,255,100),        objectName="start",
                                                hover=(255,255,255,70),     pressed=(255,255,255,50),   disabled=(0,0,0,60),            add=True, size=15)
        self.stop   = mybutton(mainframe["4"],  radius=5,                   text="Stop",                color=(255,255,255,100),        objectName="stop",
                                                hover=(255,255,255,120),    pressed=(255,255,255,80),   disabled=(0,0,0,60),            add=True)
        self.reset  = mybutton(mainframe["4"],  radius=5,                   text="Reset",               color=(255,255,255,100),        objectName="reset",
                                                hover=(255,255,255,120),    pressed=(255,255,255,80),   disabled=(0,0,0,60),            add=True)

        self.start.customradius(0, 5, 5, 0),    self.reset.customradius(5, 0, 0, 5)

#### Create inputbox and plus/minus buttons
        self.minus   = mybutton(mainframe["5"], radius=5,                   text="Trekk fra",           color=(255,255,255,100),        objectName="minus",
                                                hover=(255,255,255,70),     pressed=(0,0,0,150),        disabled=(0,0,0,60),            add=True)

        self.input   = myinput(mainframe["5"],  color=(0  ,0  ,0  ,60),     add=True,                   objectName="timerinput",
                                                label=True,                 radius=5)

        self.input.align("center"),             self.input.setFixedHeight(30),                          self.input.addstyle("font-size","font-size: 13px;")
        self.input.addstyle("font-family",      "font-family: Roboto;"),                                self.input.setEnabled(False)

        self.plus   = mybutton(mainframe["5"],  radius=5,                   text="Legg til",            color=(255,255,255,100),        objectName="plus",
                                                hover=(255,255,255,70),     pressed=(0,0,0,150),        disabled=(0,0,0,60),            add=True)

        self.minus.customradius(0,5,5,0),       self.plus.customradius(5,0,0,5),                        self.plus.setMinimumWidth(60)
        self.minus.setMinimumWidth(60),         self.stop.setEnabled(False),                            self.reset.setEnabled(False)
        self.minus.setEnabled(False),           self.plus.setEnabled(False)

#### Collectively configure some style in all Room() buttons
        for i in [self.start,self.stop,self.reset,self.plus,self.minus]:
            i.setFixedHeight(30),                                   i.addstyle("color", "color: rgb(255, 255, 255);")
            i.addstyle("font-family","font-family: Roboto;"),       i.addstyle("font-size", "font-size: 13px;")

#### Configure button functions

        self.buttonConfig(pat)

    #### Variable to know if button should blink or not
        self.blink = False

    # Configure buttons
    def buttonConfig(self, pat):
        self.start.clicked.connect(lambda: self.Start(pat)),    self.stop.clicked.connect(lambda: self.Stop())
        self.reset.clicked.connect(lambda: self.Reset()),       self.input.returnPressed.connect(lambda: self.Start(pat))

    # Starting timer
    def Start(self, pat):
        #Dont't start if nothing has been entered
        if self.input.text() == "00:00:00":
            return
        # When started for the first time
        if   self.timernum == 0 and self.timerOn   == False:
             self.timernum,         self.timerOn    = self.string2sec(),    True
             self.timerr.start(),   self.input.setText("00:00:00"),         self.changeInput("running")
             pat[self.patient.text()][4] = True
        # When starting after a pause
        elif self.timerOn == False:
             self.timerr.start()
             self.timerOn = True
        # When timer runs out
        elif self.timernum == 0 and self.timerOn == True:
            self.Reset()
            return

        self.start.setEnabled(False),   self.stop.setEnabled(True),     self.reset.setEnabled(False)
        self.timer.setText(self.sec2string(self.timernum, "s")),        self.blurtimer.setText(self.sec2string(self.timernum, "s"))
        self.timernum -= 1

    # Stopping timer
    def Stop(self):
        self.timerr.stop(),             self.start.setEnabled(True),    self.reset.setEnabled(True),    self.stop.setEnabled(False)
        self.timerOn = False

    # Resetting timer
    def Reset(self):
        self.timerOn,                   self.timernum   =               False,      0
        self.timerr.stop(),             self.start.setEnabled(True),    self.stop.setEnabled(False)
        self.reset.setEnabled(False),   self.timer.setText("00:00:00"), self.blurtimer.setText("00:00:00")
        self.changeInput("off")

    # Change the input when starting/stopping the timer
    def changeInput(self, direction):
        if direction == "running":
            self.input.setPlaceholderText("MM"),    self.input.setInputMask("")
            self.input.setText(""),                 self.input.valida("[0-9]{2}")
            self.plus.setEnabled(True),             self.minus.setEnabled(True)
        elif direction == "off":
            self.input.setInputMask("99:99:99"),    self.input.valida("[0-2]{1}[0-3]{1}:[0-5]{1}[0-9]{1}:[0-5]{1}[0-9]{1}")
            self.input.setText("00:00:00"),         self.plus.setEnabled(False),               self.minus.setEnabled(False)

    # Turn string with time format into seconds as integer number
    def string2sec(self):
        input = self.input.text()
        h, m, s = input.split(":")
        secs = (int(h)*60*60)+(int(m)*60)+int(s)
        return secs

    # Turn seconds as integer number into time formated string
    def sec2string(self, unit, mode):
        if mode == "s":
            display = datetime.timedelta(seconds=unit)
        elif mode == "m":
            display = str(datetime.timedelta(minutes=unit))
            display = display[:5]
        return str(display)

    # Change colors of the frame around the timer
    def changeColors(self, alpha, pat):

        greenTime = 15 * 60  # 30 minutes
        redTime = 5 * 60  # 10 minutes
        
        if self.timernum >= greenTime:
            self.tframe.addstyle(   "border-color", f"""border-color:   qlineargradient(spread:reflect, x1:0.5, y1:0, x2:1, y2:0, 
                                                                        stop:0 rgba(0, {alpha}, 0, {int(alpha/3)}), 
                                                                        stop:1 rgba(120, 255, 120, {int(alpha/3)}));                    """)
            self.blurframe.addstyle("border-color", f"""border-color:   qlineargradient(spread:reflect, x1:0.5, y1:0, x2:1, y2:0, 
                                                                        stop:0 rgba(0, {alpha}, 0, {int(alpha / 2)}), 
                                                                        stop:1 rgba(120, 255, 120, {int((alpha + 200) / 2)}));          """)
        elif self.timernum >= redTime:
            self.tframe.addstyle(   "border-color", f"""border-color:   qlineargradient(spread:reflect, x1:0.5, y1:0, x2:1, y2:0, 
                                                                        stop:0 rgba({alpha}, 255, 0, {int(alpha/3)}), 
                                                                        stop:1 rgba(255, 255, 0, {int(alpha/3)}));                      """)
            self.blurframe.addstyle("border-color", f"""border-color:   qlineargradient(spread:reflect, x1:0.5, y1:0, x2:1, y2:0, 
                                                                        stop:0 rgba({alpha}, 255, 0, {int(alpha / 2)}), 
                                                                        stop:1 rgba(255, 255, 0, {(alpha + 200) / 2}));                 """)
        elif self.timernum <= redTime and self.timernum > 0:
            self.tframe.addstyle(   "border-color", f"""border-color:   qlineargradient(spread:reflect, x1:0.5, y1:0, x2:1, y2:0, 
                                                                        stop:0 rgba({alpha}, 0, 0, {int(alpha/3)}), 
                                                                        stop:1 rgba(255, 120, 120, {int(alpha/3)}));                    """)
            self.blurframe.addstyle("border-color", f"""border-color:   qlineargradient(spread:reflect, x1:0.5, y1:0, x2:1, y2:0, 
                                                                        stop:0 rgba({alpha}, 0, 0, {int(alpha / 2)}), 
                                                                        stop:1 rgba(255, 120, 120, {int((alpha + 200) / 2)}));          """)
        elif self.timernum == 0 and self.timerOn == False:
            self.tframe.addstyle(   "border-color", f"""                border-color: rgba(255, 255, 255, 0);                           """)
            self.blurframe.addstyle("border-color", f"""                border-color: rgba(255, 255, 255, 255);                         """)

        if self.patient.text() != "":
            if self.blink == True:
                self.statusframe["4"].bg(100,100,0,alpha)
        else:
            self.statusframe["4"].bg(255,255,255,100)


    def string2min(self, ptime):
        inputs = ptime
        h, m = inputs.split(":")
        mins = (int(h)*60)+(int(m))
        return mins

    def patient2room(self, Main, main, pat):

        # Stop here if dictionary is empty, for cpu purposes
        if pat == {}:
            return

        currenttime = datetime.datetime.now()
        currenttime = self.string2min(currenttime.strftime("%H:%M"))

        for i in pat:

        # to be deleted:
            if pat[i][9]==True:
                continue

            if pat[i][1] != self.name:
                continue
            elif pat[i][6]==True and pat[i][7] == False:
                self.statusb.clicked.connect(lambda: self.room2pet(Main, i, pat))
            elif pat[i][8]==True:
                Main.room["5"].input.setEnabled(False)
                main.room["5"].input.bg(0,0,0,60)
                Main.room["5"].patient.setText(""), Main.room["5"].statusb.setText(""), Main.room["5"].neste.setText("")
                pat[i][9] =True
                continue

            if pat[i][6]==True:
                continue

            if pat[i][2] <= currenttime and (pat[i][2]+45) >= currenttime and (self.patient.text() == i or self.patient.text()==""):
                self.patient.setText(i),    self.neste.setText(self.sec2string(pat[i][3], "m"))
                self.input.setEnabled(True)
                self.input.bg(255, 255, 255, 100)
            else:
                continue

            if pat[i][4] == False:
                self.status.setText("Venter på behandling...")
            elif self.timernum > (15*60):
                self.status.setText("Under behandling")
            elif self.timernum > (5*60):
                self.status.setText("Vann og WC")
            elif self.timernum > 0:
                self.status.setText("Gjør klar til PET-Scan")
            elif self.timernum == 0 and pat[i][5] == False:
                self.status.setText("Trykk for å sende til PET-scan")
                self.blink=True
                self.statusb.clicked.connect(lambda: self.room2pet(Main, i, pat))
            elif pat[i][5] == True and pat[i][6]==False and Main.room["5"].patient.text() == "":
                self.room2pet(Main, i, pat)

        if Main.room["5"].patient.text()!="":

            if Main.room["5"].timernum != 0 and pat[Main.room["5"].patient.text()][8] == False:
                pat[Main.room["5"].patient.text()][7] = True
                Main.room["5"].status.setText("Under behandling")

            if pat[Main.room["5"].patient.text()][7]==True and Main.room["5"].timernum==0:
                pat[Main.room["5"].patient.text()][8]=True
        else:
            Main.room["5"].status.setText("")


    def room2pet(self, main, name, pat):
        if self.patient.text() != "":
            namm = self.patient.text()
        else:
            return

        if main.room["5"].patient.text()=="" and pat[self.patient.text()][6]==False:

            self.patient.setText(""), self.status.setText(""), self.neste.setText(""), self.Reset()
            self.input.setEnabled(False)
            self.input.bg(0,0,0,60)
            main.room["5"].patient.setText(namm)
            main.room["5"].status.setText("Venter på behandling...")
            pat[namm][5] = True
            pat[namm][6] = True
            self.senttopet = True
            main.room["5"].input.setEnabled(True)
            main.room["5"].input.bg(255,255,255,100)

        elif main.room["5"].patient.text()!="" and pat[namm][6]==False:
            self.input.setEnabled(False)
            main.room["5"].input.bg(0,0,0,60)
            self.status.setText("Venter på PET-Scan...")
            pat[namm][5] = True
        self.blink = False

class Schedule(myframe):
    def __init__(self, Master, Main, *args, **kwargs):
        myframe.__init__(self, Master, *args, **kwargs)

        #### Create central frame and add it to master layout
        scf     = myframe(self, "v", radius=10, add=True)

#### Create 4 content frames withing the central frame
        contframe   = {}
        for i in range(1,5):
            contframe[str(i)] = myframe(scf, "h", f"contframe{i}", color=(0,0,0,60), add=True)

        contframe["1"].customradius(8,8,0,0),       contframe["1"].setFixedHeight(50),          contframe["2"].setFixedHeight(25)
        contframe["2"].transp(),                    contframe["4"].setFixedHeight(15),          contframe["4"].customradius(0,0,10,10)
        contframe["1"].bg(0, 0, 0, 120),            contframe["3"].margins(0, 0, 0, 0)
        schedtitle  = mylabel(  contframe["1"],     font=("Roboto", "Bold", 100),   size=30,    text="Timeplan",    add=True,   align="center"  )

        #### Create 7 frames in frame 2
        labelframe, labbs = {}, {}
        for i in range(1, 8):
            labelframe[str(i)] = myframe(contframe["2"],    "h",    f"labelframe{i}",   color=(0,0,0,120),  add=True)
            labbs[str(i)] = mylabel(labelframe[str(i)],     "h",    f"labbsframe{i}",   add=True,           font=("Roboto", "Normal", 100))
            labbs[str(i)].addstyle("color", "color: rgb(255,255,255);"),                labelframe[str(i)].margins(5,0,0,0)

        labbs["2"].setText("Navn:"),                                labbs["3"].setText("Injeksjonsrom:"),   labelframe["1"].setFixedWidth(45)
        labbs["4"].setText("Tid for injeksjonsbehandling:"),        labbs["5"].setText("Tid for PET-Scan:"),labelframe["3"].setFixedWidth(160)
        labelframe["6"].setFixedWidth(45),                          labelframe["7"].setFixedWidth(10),      labbs["6"].setText("Fjern:")

        self.scrollarea = myscroll(contframe["3"])
        contframe["3"].lay.addWidget(self.scrollarea)

#Add entries
        self.enter = Schedentry(self.scrollarea.scrollframe,        self,       color=(0,0,0,120), objectName="starter")
        self.scrollarea.scrollframeLay.addWidget(self.enter,        0,          qc.Qt.AlignTop)
        self.patients = {}

    def add(self, name, room, itime, ptime):

        #Only add patient if a name is typed in
        if self.enter.inputs["2"].text() == "" or self.enter.inputs["2"].text().strip()=="":
            return
        # Remove whitespaces from start and end of name
        name = name.strip()
        # If a patient with same name exists -> add () containing number of patients with same name as a suffix
        if name in self.patients:
            suffix = 2
            while name in self.patients:
                if f"{name} ({suffix})" in self.patients:
                    pass
                else:
                    name = f"{name} ({suffix})"
                suffix += 1

        # Add the patient to both the dictionary and the gui
        if name not in self.patients:

            self.patients[name] = [Schedentry(  self.scrollarea.scrollframe,  self, objectName=f"{name}")]

            #Add room, injection- and pet-time
            self.patients[name].append(room),   self.patients[name].append( self.string2min(itime)),     self.patients[name].append(self.string2min(ptime))
            # Add Bools: [4]: treatment started, [5]: request sent to PET-Scan, [6]: has been sent to Pet-scan, [7]: PET-Scan started, [8]: PET-Scan finished
            self.patients[name].append(False),  self.patients[name].append(False),  self.patients[name].append(False), self.patients[name].append(False), self.patients[name].append(False)
            self.patients[name].append(False)
            # Set the labels to display this
            self.patients[name][0].labels["2"].setText(name),               self.patients[name][0].labels["3"].setText(room)
            self.patients[name][0].labels["4"].setText(itime),              self.patients[name][0].labels["5"].setText(ptime)
            # Insert the widget into the layout and flip the stacked widget over
            self.scrollarea.scrollframeLay.insertWidget(self.scrollarea.scrollframeLay.count() - 1, self.patients[name][0])
            self.patients[name][0].setCurrentIndex(1)
            # Reconfigure the entry widget
            self.enter.inputs["2"].setText(None),       self.enter.inputs["3"].setText("1"),        self.enter.inputs["4"].setText("00:00")
            self.enter.inputs["5"].setText("00:00"),    self.enter.inputs["2"].setFocus(),          self.recolor(name)

    def remove(self, name):
        pass

    def recolor(self, name):
        s = 0
        for i in self.patients:
            if s%2==0:
                self.patients[i][0].Theme("light")
            else:
                self.patients[i][0].Theme("dark")
            s+=1

    def string2min(self, ptime):
        inputs = ptime
        h, m = inputs.split(":")
        mins = (int(h)*60)+(int(m))
        return mins

    def sec2string(self):
        display = datetime.timedelta(seconds=self.timernum)
        return str(display)

class Schedentry(mystack):

    def __init__(self, Master, main, objectName, *args, **kwargs):

        mystack.__init__(self, Master, objectName, *args, **kwargs)
        self.setFixedHeight(30)

        self.theme = (0,0,0,80)

        # Create the input side of the stacked widget:
        schedinput = myframe(self, "h", color=(0,0,0,0))
        # Make 5 frames
        schedframe = {}
        for i in range(1, 7):
            schedframe[str(i)] = myframe(schedinput, "h", f"schedframe{i}", color=(255, 255, 255, 255), add=True)
            schedframe[str(i)].margins(5, 0, 0, 0)
        schedframe["1"].setFixedWidth(39),  schedframe["3"].setFixedWidth(160), schedframe["6"].setFixedWidth(45)

        self.inputs = {}
        for i in range(2, 6):
            self.inputs[str(i)] = myinput(schedframe[str(i)], f"input{i}", color=(255, 255, 255, 255), add=True, textcolor=(0,0,0,255), size=15)
            self.inputs[str(i)].setValidator(None), self.inputs[str(i)].setInputMask(None), self.inputs[str(i)].setMinimumHeight(30)

        self.inputs["3"].setText("1"),       self.inputs["3"].valida("[1-4]{1}"),      self.inputs["2"].setPlaceholderText("Pasientens navn:")
        self.inputs["4"].setText("00:00"),   self.inputs["4"].setInputMask("99:99"),   self.inputs["4"].valida("[0-2]{1}[0-9]{1}:[0-5]{1}[0-9]{1}")
        self.inputs["5"].setText("00:00"),   self.inputs["5"].setInputMask("99:99"),   self.inputs["5"].valida("[0-2]{1}[0-9]{1}:[0-5]{1}[0-9]{1}")

        for i in range(2,6):
            self.inputs[str(i)].returnPressed.connect(lambda: main.add(self.inputs["2"].text(), self.inputs["3"].text(), self.inputs["4"].text(), self.inputs["5"].text()))

        self.schedframe=schedframe

        # Create the display side of the stacked widget:
        schedie = myframe(self, "h", color=(0, 0, 0, 0))
        # Make 6 frames
        sched = {}
        self.labels = {}
        for i in range(1, 7):
            sched[str(i)] = myframe(schedie, "h", f"schedframe{i}", color=self.theme, add=True)
            if i != 1:
                self.labels[str(i)] = mylabel(sched[str(i)], add=True, size=15)
            sched[str(i)].margins(5, 0, 0, 0)

        sched["1"].setFixedWidth(40), sched["1"].margins(10,0,0,0), sched["2"].margins(10,0,0,0), sched["3"].setFixedWidth(160), sched["6"].setFixedWidth(45)

        rediger = mybutton(sched["1"], text="Edit", add=True, color=(255,255,255,100), hover=(255,255,255,70), pressed=(255,255,255,50), radius=5, align="left")
        rediger.setFixedHeight(20), rediger.setFixedWidth(26), rediger.addstyle("color", "color: rgb(255, 255, 255);")

        self.sched=sched
        self.addstack(schedinput, "Input")
        self.addstack(schedie, "Show")
        self.setCurrentIndex(0)

    def Theme(self, key):
        if key == "dark":
            for i in self.schedframe:
                self.sched[i].bg(0,0,0,120)
        elif key == "light":
            for i in self.schedframe:
                self.sched[i].bg(0, 0, 0, 50)

    def edit(self):
        self.setCurrentIndex(0)

        for i in range(2,6):
            self.inputs[str(i)].returnPressed.connect(lambda: main.edit(self.inputs["2"].text(), self.inputs["3"].text(), self.inputs["4"].text(),self.inputs["5"].text()))

class Countdown(qc.QTimer):

    def __init__(self, parent, interval, mode, master=None, main=None, pat=None):

        qc.QTimer.__init__(self)

        if mode == "time":
            self.setInterval(interval),     self.timeout.connect(lambda: self.run(parent, master))
        if mode == "fps":
            self.setInterval(interval),     self.timeout.connect(lambda: self.run2(parent, pat))
        if mode == "p2r":
            self.setInterval(interval),     self.timeout.connect(lambda: self.run3(main, parent, master))

    def run(self, parent, master):
        parent.Start(master)
    def run2(self, parent, pat):
        GUI.run(parent, pat)
    def run3(self, main, parent, master):
        parent.patient2room(main, parent, master)








