from PyQt5 import QtCore, QtGui, QtWidgets 
from PyQt5.QtCore import (QCoreApplication, QObject, QRunnable, QThread, QThreadPool, pyqtSignal)

import time
from packages.ui_welcome import App_WelcomeScreen
from packages.ui_welcome2 import App_WelcomeScreen2

from packages.ui_user_menu1 import App_usermenuScreen
#import RPi.GPIO as GPIO
#import serial

from threading import Thread
import threading


class Controller:
    def __init__(self):
        self.WelcomeScreen = App_WelcomeScreen()
        self.Screen2 = App_WelcomeScreen2()
        
        self.usermenuScreen = App_usermenuScreen()
          
        print("INIT")
        self.show_Welcome()
        

    def show_Welcome(self):
        print("Show welcome")
        self.WelcomeScreen.show()
        self.WelcomeScreen.lbl_btn_start.mousePressEvent = self.show_usermenuScreen
        self.WelcomeScreen.lbl_btn_start2.mousePressEvent = self.show_usermenuScreen
        self.WelcomeScreen.btn_register.mousePressEvent = self.show_usermenuScreen

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
        self.Screen2.lbl_btn_start.mousePressEvent = self.show_usermenuScreen





    def show_usermenuScreen(self, event):
        
        print("user menu")
        self.usermenuScreen.show()
        self.Screen2.close()
        self.WelcomeScreen.close()
        
        self.usermenuScreen.btn_option1.mousePressEvent = self.set_backTo1        
        self.usermenuScreen.btn_option2.mousePressEvent = self.set_backTo1
        self.usermenuScreen.btn_option3.mousePressEvent = self.set_backTo1
        self.usermenuScreen.btn_option4.mousePressEvent = self.set_backTo1
        self.usermenuScreen.btn_back.mousePressEvent = self.set_backTo1




    def alcohol_test(self, internet_status):
        print("alcohol_test## Internet :",internet_status)        
        print("alcohol_test## alcohol_active_var :",self.alcohol_active)
        while(self.alcohol_active == True ):            
            print("alcohol_test## ident_active :",self.ident_active)
            if self.ident_active == False:                
                print('START: CHECK_ALCOHOL_TESTER')

                self.ser_a = serial.Serial()
                self.ser_a.port = ALCOHOL_DEVICE_PORT
                self.ser_a.baudrate = ALCOHOL_DEVICE_BAUDRATE
                self.ser_a.bytesize = ALCOHOL_DEVICE_BYTESIZE
                self.ser_a.parity = ALCOHOL_DEVICE_PARITY
                self.ser_a.stopbits = ALCOHOL_DEVICE_STOPBITS
                self.ser_a.timeout = ALCOHOL_DEVICE_TIMEOUT

                if( self.ser_a.isOpen() == True ):
                    self.ser_a.close()
                    
                self.ser_a.open()

                command = b'\xAB\x05\xB1\x00\xFE'
                self.ser_a.write(command)

                while self.alcohol_active:
                    data_a = self.ser_a.readline()                    
                    if(len(data_a) > -1):
                        if(data_a.find(b'\xa2\x00') > 0):
                            print('---- CHECK_ALCOHOL_TESTER: START')
                            self.alcohol_test_step = 2
                            self.alcohol_show_step = 2
                            thr5 = Thread(target=self.run_blow_screen)
                            thr5.start()

                        if(data_a.find(b'\xa3\x00') > 0):
                            print('---- CHECK_ALCOHOL_TESTER: BLOW')
                            self.alcohol_test_step = 3
                            self.alcohol_show_step = 3
                            thr6 = Thread(target=self.run_alcohol_event_screen)
                            thr6.start()
                            #music = AudioSegment.from_mp3('sounds/blow.mp3')
                            #play(music)

                        if(data_a.find(b'\xa4\x00') > 0):
                            print('---- CHECK_ALCOHOL_TESTER: TIMEOUT')
                            self.alcohol_test_step = 4
                            
                            if( self.ser_a.isOpen() == True ):
                                self.ser_a.close()
                            time.sleep(1.0)                            
                            try:
                                if( self.ser_m.isOpen() == True ):
                                    self.ser_m.close()
                            except:
                                pass

                            try:
                                if( self.ser_a.isOpen() == True ):
                                    self.ser_a.close()
                            except:
                                pass
                            
                            try:
                                if(self.ser_r.isOpen() == True):
                                    self.ser_r.close()
                            except:
                                pass      

                            thrIdentS = Thread(target=self.show_Welcome())
                            thrIdentS.start()
                            thrIdentS.join()
                            self.alcohol_active = False
                            break

                        if(data_a.find(b'\xa5\x00') > 0):
                            print('---- CHECK_ALCOHOL_TESTER: CHECK')
                            self.alcohol_test_step = 5
                            try :
                                print("check_temp_dummy")
                                #check_temperature(self)
                            except :
                                self.temperature_value = 37.3
                                
                            self.plus_temperature = 1
                            self.get_camera()

                        if(data_a.find(b'\xa6\x00') > 0):
                            print('---- CHECK_ALCOHOL_TESTER: ERROR')
                            self.alcohol_test_step = 6

                            GPIO.output(18, GPIO.LOW)
                            GPIO.output(19, GPIO.LOW)
                            GPIO.cleanup()

                            time.sleep(1.0)
                            self.ser_a.write(command)

                        if(data_a.find(b'\x05\xa7\x00') > 0):
                            print('---- CHECK_ALCOHOL_TESTER: SUCCESS')
                            self.alcohol_test_step = 7
                            self.alcohol_show_step = 7

                            GPIO.output(18, GPIO.LOW)
                            GPIO.output(19, GPIO.LOW)
                            UVthread = Thread(target=self.uv_auto)
                            UVthread.start()                            
                            
                        if(self.alcohol_test_step == 7 and data_a.find(b'\xaa') > -1):
                            pos_a = data_a.find(b'\x05\xa7\x00')
                            if(pos_a == -1):
                                pos_a = 0

                            res_a = data_a[pos_a:]
                            pos_a = res_a.find(b'\xaa')
                            if(pos_a > -1):
                                if(self.ser_a.isOpen() == True):
                                    self.ser_a.close()
                                time.sleep(1.0)
                                self.ser_f = None
                                self.ser_a = None                                
                               
                                res_v = res_a[(pos_a+1):]
                                if not res_v[1] is None:
                                    self.alcohol_value = str(res_v[1])
                                if not res_v[2] is None:
                                    self.alcohol_value =  self.alcohol_value + '.' + str(res_v[2])
                                if not res_v[3] is None:
                                    self.alcohol_value =  self.alcohol_value + str(res_v[3])
                                print(self.alcohol_value)
                                self.alcohol_value = float(self.alcohol_value)   
                                self.alcohol_test_step = 8
                                self.alcohol_show_step = 8

                                print(" STEP == 7")
                                print(data_a)
                                print(pos_a)

                                print("######## I D ##########")                                
                                print(self.employee_id)                                                               
                                print("##################")
                                print("                     ")
                                print("######## ALCOHOL ##########")   
                                print(self.alcohol_value) 
                                print("##################")

                                thr701 = Thread(target=self.set_oxygenScreen(self.internet_status, self.input_type, self.test_mode_Full))  ##insert detail
                                thr701.start()

                                if(self.alcohol_value > MAXIMUM_ALCOHOL_VALUE):
                                    alcoholPlus = 1
                                    self.allog_sum_alcohol_detect = int(self.allog_sum_alcohol_detect) + alcoholPlus
                                    #music = AudioSegment.from_mp3('sounds/alcohol-failed-washhand.mp3')
                                    self.plus_alcohol = 1
                                    #play(music)
                                else:
                                    #music = AudioSegment.from_mp3('sounds/alcohol-passed-washhand.mp3')
                                    #play(music)
                                    self.plus_alcohol = 0
                                                               
                                 
                                self.alcohol_active = False                                
                                self.rfid_decimal = ''
                                self.ident_driver_id = ''
                                print("alcohol_test## CLEAR VALUE")
                                thrD1 = Thread(target=self.count_detail_screen(self.internet_status))
                                thrD1.start() 
                                self.employee_id = ''
                                break

                        elif(self.alcohol_test_step == 7 and self.alcohol_time_count < 1700):
                            self.alcohol_time_count += 1
                            print('self.alcohol_time_count = ' + str(self.alcohol_time_count))

                        elif(self.alcohol_time_count > 1699):
                            if(self.ser_a.isOpen() == True):
                                self.ser_a.close()
                            sleep(1.0)
                            self.ser_f = None
                            self.ser_a = None

                            print("alcohol_test ## TIME OUT ")
                            print(data_a)
                            print(pos_a)
                            print(" * * * R A W * * * ")
                            print(" ")
                            print(self.alcohol_value)
                            print(" ")
                            print(" * * * R A W * * * ")
                            
                            thr701 = Thread(target=self.set_oxygenScreen(self.internet_status, self.input_type, self.test_mode_Full))
                            thr701.start()

                            self.alcohol_value = 0.0
                            self.alcohol_test_step = 8
                            self.alcohol_show_step = 8
                            #music = AudioSegment.from_mp3('sounds/alcohol-passed-washhand.mp3')
                            #play(music)
                            self.alcohol_active = False
                            
                            print("CLEAR 604 ")
                            thrD1 = Thread(target=self.count_detail_screen(self.internet_status))
                            thrD1.start() 
                            break
                    else:
                        pass 