# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from packages.controller import Controller

if __name__ == "__main__":
    import sys
    
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    #controller.run()
    sys.exit(app.exec_())