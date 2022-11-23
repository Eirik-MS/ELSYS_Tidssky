from gui import *
from main import *
from gui import *
from overview import *

GLOBAL_STATE = 0

class Ui_Functions(MainWindow):
    def __init__(self):
        self.patientdict = {}
    def maximize_restore(self):
        global GLOBAL_STATE
        status = GLOBAL_STATE

        if status == 0:



            GLOBAL_STATE = 1

            self.ui.drop_shadow_layout.setContentsMargins(0, 0, 0, 0)
            self.ui.mainwindow.setStyleSheet("border-image: url(:/images/Background3.jpg);border-radius: 0px;")
            self.showMaximized()


        else:
            GLOBAL_STATE = 0
            self.showNormal()
            self.resize(self.width()+1, self.height()+1)
            self.ui.drop_shadow_layout.setContentsMargins(10, 10, 10, 10)
            self.ui.mainwindow.setStyleSheet("border-image: url(:/images/Background3.jpg);border-radius: 15px;")


    def buttonDefinitions(self):

        # close/maximize/minimize buttons:

        self.ui.maximize.clicked.connect(lambda: Ui_Functions.maximize_restore(self))






