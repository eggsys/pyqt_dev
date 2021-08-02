# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie


class Ui_usermenuScreen(object):

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(1024, 600)

        self.lbl_bg_image_id00 = QtWidgets.QLabel(Form)
        self.lbl_bg_image_id00.setGeometry(QtCore.QRect(0, 0, 1024, 600))        
        self.gif_welcome_id00 = QMovie('images/background/user-menu01.gif')
        self.lbl_bg_image_id00.setMovie(self.gif_welcome_id00)
        self.gif_welcome_id00.start()        
        self.lbl_bg_image_id00.setScaledContents(True)
        self.lbl_bg_image_id00.setObjectName("lbl_bg_image_id00")

        self.btn_option1 = QtWidgets.QLabel(Form)
        self.btn_option1.setGeometry(QtCore.QRect(120, 280, 221, 91))
        self.btn_option1.setText("")
        self.btn_option1.setPixmap(QtGui.QPixmap("images/button/user-menu-btn-have.png"))
        self.btn_option1.setScaledContents(True)
        self.btn_option1.setObjectName("btn_option1")

        self.btn_option2 = QtWidgets.QLabel(Form)
        self.btn_option2.setGeometry(QtCore.QRect(390, 280, 221, 91))
        self.btn_option2.setText("")
        self.btn_option2.setPixmap(QtGui.QPixmap("images/user-menu-btn-donthave.png"))
        self.btn_option2.setScaledContents(True)
        self.btn_option2.setObjectName("btn_option2")

        self.btn_option3 = QtWidgets.QLabel(Form)
        self.btn_option3.setGeometry(QtCore.QRect(730, 280, 221, 91))
        self.btn_option3.setText("")
        self.btn_option3.setPixmap(QtGui.QPixmap("images/user-menu-btn-guest.png"))
        self.btn_option3.setScaledContents(True)
        self.btn_option3.setObjectName("btn_option3")

        self.btn_option4 = QtWidgets.QLabel(Form)
        self.btn_option4.setGeometry(QtCore.QRect(260, 410, 211, 91))
        self.btn_option4.setText("")
        self.btn_option4.setPixmap(QtGui.QPixmap("images/user-menu-btn-check_out.png"))
        self.btn_option4.setScaledContents(True)
        self.btn_option4.setObjectName("btn_option4")


        self.btn_back = QtWidgets.QLabel(Form)
        self.btn_back.setGeometry(QtCore.QRect(50, 60, 170, 71))
        self.btn_back.setText("")
        self.btn_back.setPixmap(QtGui.QPixmap("images/button/back-button.png"))
        self.btn_back.setScaledContents(True)
        self.btn_back.setObjectName("btn_back")






       

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))


class App_usermenuScreen(QtWidgets.QWidget, Ui_usermenuScreen):

    switch_btn1_window = QtCore.pyqtSignal()
    switch_btn2_window = QtCore.pyqtSignal()
    switch_btn3_window = QtCore.pyqtSignal()
    switch_btn4_window = QtCore.pyqtSignal()
    switch_back_window = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.CustomizeWindowHint)
        self.setupUi(self)

        self.btn_option1.mousePressEvent = self.pushbutton_btn1_handler
        self.btn_option2.mousePressEvent = self.pushbutton_btn2_handler
        self.btn_option3.mousePressEvent = self.pushbutton_btn3_handler
        self.btn_option4.mousePressEvent = self.pushbutton_btn4_handler
        self.btn_back.mousePressEvent = self.pushbutton_back_handler
    
    def pushbutton_btn1_handler(self):
        print(" button press !")
        self.switch_btn1_window.emit()
    
    def pushbutton_btn2_handler(self):
        print(" button press !")
        self.switch_btn2_window.emit()

    def pushbutton_btn3_handler(self):
        print(" button press !")
        self.switch_btn3_window.emit()

    def pushbutton_btn4_handler(self):
        print(" button press !")
        self.switch_btn4_window.emit()

    def pushbutton_back_handler(self):
        print(" button press !")
        self.switch_back_window.emit()

        

       
	            
    