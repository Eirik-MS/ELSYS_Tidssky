from PyQt5 import QtWidgets as qw, QtGui as qg, QtCore as qc
from datetime import datetime
import sys


class Main(qw.QMainWindow):



    def __init__(self):

        self.time = "00:00:00"

        qw.QMainWindow.__init__(self)
        self.resize(500, 500)

        cw      = qw.QWidget(self)

        layout  = qw.QVBoxLayout(cw)
        layout.setContentsMargins(0, 0, 0, 0)

        label   = qw.QLabel(cw)
        label.setText(f"{self.time}")
        layout.addWidget(label, 0, qc.Qt.AlignHCenter)

        self.setCentralWidget(cw)



if __name__ == "__main__":

    app = qw.QApplication(sys.argv)
    main = Main()
    setattr(main, main.time, "01:00:00")
    main.show()
    sys.exit(app.exec_())


