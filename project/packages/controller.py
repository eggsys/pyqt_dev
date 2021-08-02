from PyQt5 import QtCore, QtGui, QtWidgets 
from PyQt5.QtCore import (QCoreApplication, QObject, QRunnable, QThread, QThreadPool, pyqtSignal)

from packages.mainwindow import Mainwindow
from packages.ui_welcome import App_WelcomeScreen
from threading import Thread
import threading


class Controller:
    def __init__(self):
        self.WelcomeScreen = App_WelcomeScreen()
        print("run !")
        #Mainwindow()
        #self.WelcomeScreen.show()
        self.wtf()
        

    def show_Welcome(self):
        print("Show welcome")
        
        print("END!")

    def wtf(self):
        self.WelcomeScreen.show()
        print("WTF is here ")