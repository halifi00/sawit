from operator import mod
import os
import cv2
import numpy as np
#import tensorflow as tf
# import tensorflow.compat.v1 as tf
# tf.disable_v2_behavior()
import sys
sys.path.append("..")
# from utils import label_map_util
# from utils import visualization_utils as vis_util
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from time import sleep
import modbus
from pymodbus.client.sync import ModbusSerialClient as ModbusSerialClient

from detect import Detect
from ui import Ui_MainWindow
# from write import modbusRTU

class EmbedYOLO(Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
    
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        # self.client = ModbusSerialClient(method = 'rtu', port = "COM1",  baudrate = 9600,
        #                 bytesize = 8, parity = "N", stopbits = 1, timeout = 1)
        # print(self.client.connect())
        self.start_btn.clicked.connect(self.StreamVideo)
    
    def ImageUpdateSlot(self, Image):
        self.labelFeed.setPixmap(QPixmap.fromImage(Image))

    def EFBCounterSlot(self):
        self.efb_counter.setProperty("value", self.Detect.efb_counter)

    def USBCounterSlot(self):
        self.not_efb_counter.setProperty("value", self.Detect.usb_counter)

    def TOTALCounterSlot(self):
        self.total_counter.setProperty("value", self.Detect.total_counter)

    def EFFICIENCYCounterSlot(self):
        self.efficiency_counter.setProperty("value", self.Detect.efficiency_counter)

    def CancelFeed(self):
        self.Detect.terminate()
        # self.modbusRTU.disconnect()
        # self.modbusRTU.terminate()
    
    def StreamVideo(self):
        if self.start_btn.text() == "START":
            self.start_btn.setText("LOADING")
            
            self.Detect = Detect(0, 0, 0, 100)
            self.Detect.start()
            
            # self.modbusRTU = modbusRTU()
            # self.modbusRTU.start()
            
            self.start_btn.setText("STOP")
            self.Detect.ImageUpdate.connect(self.ImageUpdateSlot)
            self.Detect.USBUpdate.connect(self.USBCounterSlot)
            self.Detect.EFBUpdate.connect(self.EFBCounterSlot)
            self.Detect.TOTALupdate.connect(self.TOTALCounterSlot)
            self.Detect.EFFupdate.connect(self.EFFICIENCYCounterSlot)
        

        elif self.start_btn.text() == "STOP":
            self.CancelFeed()
            self.start_btn.setText("START")
        else:    
            pass
        

        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = EmbedYOLO()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())