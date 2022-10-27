#### Imports
import sys
sys.path
sys.path.append('C:\\Users\\mgnso\\AppData\\Local\\Programs\\Python\\Python310\\lib\\site-packages')
#from PyQt5 import QtCore, QtGui, QtWidgets
import Bakgrunnsbilde
from gui import GUI
from Functions import *

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = GUI()
        self.ui.setupUi(self)
        self.show()

        Ui_Functions.Ui_definitions(self)

        ########## move the window

        def moveWindow(event):
            if event.buttons() == QtCore.Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        self.ui.frame.mouseMoveEvent = moveWindow

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

#### Run Aplication

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MainWindow()
    MainWindow.show()
    sys.exit(app.exec_())