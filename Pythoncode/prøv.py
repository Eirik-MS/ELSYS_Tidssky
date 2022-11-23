from PyQt5 import QtWidgets as qw, QtCore as qc, QtGui as qg
from datetime import datetime
import sys

class App(qw.QMainWindow):

    def __init__(self):

        # Init Main Window, define name, style, make frameless and transparent:
        qw.QMainWindow.__init__(self)
        self.setWindowFlags(qc.Qt.FramelessWindowHint)
        self.setAttribute(qc.Qt.WA_TranslucentBackground)
        self.resize(1000, 500)

        # Init the central widget. Also define the styles of the thre child frames cwf(1-3)
        cw =   qw.QWidget(self)
        cw.setObjectName("cw")
        cw.setStyleSheet("""QWidget#cw    { border-radius:              8px;    
                                            background-color:           rgb(100, 0, 0); }
                            QFrame#cwf1   { border-top-right-radius:    8px;
                                            border-top-left-radius:     8px;
                                            background-color:           rgb(0, 100, 0); }
                            QFrame#cwf2   { background:                 none;           }
                            QFrame#cwf3   { background:                 none;           }
                            QFrame#cwf4   { border-bottom-left-radius:  8px;
                                            border-bottom-right-radius: 8px;
                                            background-color:           rgb(0, 100, 0); }
                            QFrame#bf1    { border-bottom-left-radius:  8px;            }
                            QFrame#bf2    { border-bottom-right-radius: 8px;
                                            background-color:           rgb(0, 0, 100); }   )""")
        self.setCentralWidget(cw)

        # Init cw layout:
        cwl     =   qw.QVBoxLayout(cw)
        cwl.setContentsMargins(0, 0, 0, 0)
        cwl.setSpacing(0)


        # Init 3 frames, top, middle and bottom. Make layouts and
        # set style and appearance. Fix height of the top and bottom frame
        mframe  =   {}
        for i in range(1,5):

            mframe[str(i)] = [qw.QFrame(cw)]
            mframe[str(i)][0].setObjectName(f"cwf{i}")

            mframe[str(i)].append(qw.QHBoxLayout(mframe[str(i)][0]))
            mframe[str(i)][1].setContentsMargins(0, 0, 0, 0)
            mframe[str(i)][1].setSpacing(5)

            cwl.addWidget(mframe[str(i)][0])


        mframe["1"][0].setFixedHeight(50)
        mframe["4"][0].setFixedHeight(20)

        # Make two frames inside cwf3. Create layouts and put credits in the left and a stretch-tool in the right
        bf  =   {}
        for i in range(1,3):
            bf[str(i)]  =   [qw.QFrame(mframe["4"][0])]
            bf[str(i)][0].setObjectName(f"bf{i}")

            bf[str(i)].append(qw.QVBoxLayout(bf[str(i)][0]))
            bf[str(i)][1].setContentsMargins(0, 0, 0, 0)
            bf[str(i)][1].setSpacing(0)
            mframe["4"][1].addWidget(bf[str(i)][0])
        bf["2"][0].setFixedWidth(20)

if __name__ == "__main__":

    application =   qw.QApplication(sys.argv)
    program     =   App()

    program.show()
    sys.exit(application.exec_())