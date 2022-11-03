#### Imports
from Functions import *
from Classes import Patients
from PyQt5 import QtCore, QtGui, QtWidgets

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = GUI()
        self.ui.setupUi(self)
        self.show()



        Ui_Functions.buttonDefinitions(self)

        ########## Move the window

        def moveWindow(event):
            if event.buttons() == QtCore.Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        self.ui.frame.mouseMoveEvent = moveWindow

        self.ui.close.clicked.connect(self.close)
        self.ui.minimize.clicked.connect(self.showMinimized)

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()


#### Run Aplication

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindoww = MainWindow()
    MainWindoww.show()
    sys.exit(app.exec_())