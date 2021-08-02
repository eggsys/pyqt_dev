
# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie



class Ui_WelcomeScreen2(object):

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



        self.lbl_btn_start = QtWidgets.QLabel(Form)
        self.lbl_btn_start.setGeometry(QtCore.QRect(560, 480, 341, 91))
        self.lbl_btn_start.setText("")
        self.lbl_btn_start.setPixmap(QtGui.QPixmap("project/images/button/full_check_in-01.png"))
        self.lbl_btn_start.setScaledContents(True)
        self.lbl_btn_start.setObjectName("lbl_btn_start")







       

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))


class App_WelcomeScreen2(QtWidgets.QWidget, Ui_WelcomeScreen2):

    switch_btnstart_window = QtCore.pyqtSignal()
    switch_btnstart2_window = QtCore.pyqtSignal()
    switch_btnregister_window = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.CustomizeWindowHint)
        self.setupUi(self)

