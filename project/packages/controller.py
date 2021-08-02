from PyQt5 import QtCore, QtGui, QtWidgets 
from PyQt5.QtCore import (QCoreApplication, QObject, QRunnable, QThread, QThreadPool, pyqtSignal)

import time
from packages.ui_welcome import App_WelcomeScreen
from packages.ui_welcome2 import App_WelcomeScreen2


from threading import Thread
import threading


class Controller:
    def __init__(self):
        self.WelcomeScreen = App_WelcomeScreen()
        self.Screen2 = App_WelcomeScreen2()
          
        print("INIT")
        self.show_Welcome()
        

    def show_Welcome(self):
        print("Show welcome")
        self.WelcomeScreen.show()
        self.WelcomeScreen.lbl_btn_start.mousePressEvent = self.set_nothing
        self.WelcomeScreen.lbl_btn_start2.mousePressEvent = self.set_nothing
        self.WelcomeScreen.btn_register.mousePressEvent = self.set_nothing

    def set_nothing(self, event):
        print("ping !")
        self.show_2()
        

        
        print("END!")

    def set_backTo1(self, event):
        self.WelcomeScreen.show()
        self.Screen2.close()

    def wtf(self):
        self.WelcomeScreen.show()
        print("WTF is here ")
        time.sleep(5)

    def show_2(self):        
        self.Screen2.show()
        self.Screen2.lbl_btn_start.mousePressEvent = self.set_backTo1