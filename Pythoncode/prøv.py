from PyQt5 import QtWidgets as qw, QtGui as qg, QtCore as qc
import sys

class A(qw.QMainWindow):
    def __init__(self):

        qw.QMainWindow.__init__(self)
        self.resize(700, 500)

        cw     =   qw.QWidget(self)
        cwl    =   qw.QVBoxLayout(cw)
        cwl.setContentsMargins(5, 5, 5, 5)
        cwl.setSpacing(5)

        self.timer = qc.QTimer()
        self.timer.setInterval(500)

        self.frames = {}
        for i in range(0,4):
            frame = f"frame{i}"
            self.frames[frame] = B(cw, cwl, A)


        self.timer.timeout.connect(lambda: self.frames["frame1"].noe())
        self.timer.timeout.connect(lambda: self.frames["frame2"].noe())

        self.timer.start()

        self.setCentralWidget(cw)






class B(qw.QFrame):

    value = 5

    def __init__(self, master, lay, A):
            qw.QFrame.__init__(self, master)
            self.setStyleSheet(f"background-color: rgb({B.value}, 255, 0);")
            layout = qw.QHBoxLayout(self)
            layout.setContentsMargins(5, 5, 5, 5)
            self.button = qw.QPushButton(self)
            self.button.setText(f"{B.value}")
            layout.addWidget(self.button)
            lay.addWidget(self)
            self.button.clicked.connect(lambda: self.changeValue())

    def noe(self):

        self.button.setText(f"{B.value}")


    @classmethod
    def changeValue(cls):
        cls.value = 50










if __name__ == "__main__":
    app = qw.QApplication(sys.argv)
    main = A()
    main.show()
    sys.exit(app.exec_())