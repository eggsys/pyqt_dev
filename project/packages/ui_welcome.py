
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

        self.gif_welcome_id00 = QMovie('project/images/background/k-man-screen.gif')

        

        self.gif_welcome_id00.setCacheMode(QMovie.CacheAll)
        self.gif_welcome_id00.setSpeed(100)
        #self.gif_welcome_id00 = QMovie.setFormat(GIF)
        self.lbl_bg_image_id00.setMovie(self.gif_welcome_id00)
        
        self.gif_welcome_id00.start()        
        self.lbl_bg_image_id00.setScaledContents(True)
        self.lbl_bg_image_id00.setObjectName("lbl_bg_image_id00")


        #self.movie.stop()
        #self.movie.setFileName(self.gifFile)
        #self.movie.start()
       



        self.lbl_btn_start = QtWidgets.QLabel(Form)
        self.lbl_btn_start.setGeometry(QtCore.QRect(560, 480, 341, 91))
        self.lbl_btn_start.setText("")
        self.lbl_btn_start.setPixmap(QtGui.QPixmap("project/images/button/full_check_in-01.png"))
        self.lbl_btn_start.setScaledContents(True)
        self.lbl_btn_start.setObjectName("lbl_btn_start")

        self.lbl_btn_start2 = QtWidgets.QLabel(Form)
        self.lbl_btn_start2.setGeometry(QtCore.QRect(120, 480, 341, 91))
        self.lbl_btn_start2.setText("")
        self.lbl_btn_start2.setPixmap(QtGui.QPixmap("project/images/button/full_check_in-01.png"))
        self.lbl_btn_start2.setScaledContents(True)
        self.lbl_btn_start2.setObjectName("lbl_btn_start2")

                
        self.btn_register = QtWidgets.QLabel(Form)
        self.btn_register.setGeometry(QtCore.QRect(70, 40, 111, 101))
        self.btn_register.setText("")
        self.btn_register.setPixmap(QtGui.QPixmap("project/images/button/full_check_in-01.png"))
        self.btn_register.setScaledContents(True)
        self.btn_register.setObjectName("btn_back")





       

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

        self.lbl_btn_start.mousePressEvent = self.pushbutton_btnstart_handler
        self.lbl_btn_start2.mousePressEvent = self.pushbutton_btnstart2_handler
        self.btn_register.mousePressEvent = self.pushbutton_btnregister_handler


    def pushbutton_btnstart_handler(self):
        print(" button press Full FLOW!")
        self.switch_btnstart_window.emit()

    def pushbutton_btnstart2_handler(self):
        print(" button press Short FLOW !")
        self.switch_btnstart2_window.emit()


    def pushbutton_btnregister_handler(self):
        print(" button press Register !")
        self.switch_btnregister_window.emit()


