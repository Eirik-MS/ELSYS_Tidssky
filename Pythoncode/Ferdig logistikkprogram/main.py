from Classes import *
if __name__ == "__main__":
    application = qw.QApplication(sys.argv)
    Main = Main()
    Main.show()
    sys.exit(application.exec_())