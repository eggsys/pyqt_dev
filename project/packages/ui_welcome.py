
# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie



class Ui_WelcomeScreen(object):

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(1024, 600)

        self.lbl_bg_image_id00 = QtWidgets.QLabel(Form)
        self.lbl_bg_image_id00.setGeometry(QtCore.QRect(0, 0, 1024, 600))             
        self.gif_welcome_id00 = QMovie('project/images/background/racha_screen.gif')

        

        self.gif_welcome_id00.setCacheMode(QMovie.CacheAll)
        self.gif_welcome_id00.setSpeed(100)
        #self.gif_welcome_id00 = QMovie.setFormat(GIF)
        self.lbl_bg_image_id00.setMovie(self.gif_welcome_id00)
        
        self.gif_welcome_id00.start()        
        self.lbl_bg_image_id00.setScaledContents(True)
        self.lbl_bg_image_id00.setObjectName("lbl_bg_image_id00")






       

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))


class App_WelcomeScreen(QtWidgets.QWidget, Ui_WelcomeScreen):

    switch_btnstart_window = QtCore.pyqtSignal()
    switch_btnstart2_window = QtCore.pyqtSignal()
    switch_btnregister_window = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.CustomizeWindowHint)
        self.setupUi(self)
