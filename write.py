from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import modbus
from pymodbus.client.sync import ModbusSerialClient as ModbusSerialClient

class modbusRTU(QThread):
    
    def __init__(self):
        super().__init__()
        
        val = [0, 0, 0, 0]
        file = open("efb.txt", "w")
        for num in val:
            file.write(str(num) + "\n")
        file.close()
        
        self.client = ModbusSerialClient(method = 'rtu', port = "COM1",  baudrate = 9600,
                        bytesize = 8, parity = "N", stopbits = 1, timeout = 1)
        print(self.client.connect())
        
    def run(self):
        print(self.client.connect())
        file = open("efb.txt", "r")
        val = file.readlines()
        print(val)
        
        val1 = int(val[0])
        val2 = int(val[1])
        val3 = int(val[2])
        val4 = int(val[3])
        
        
        print(val1)
        print(val2)
        print(val3)
        print(val4)
        file.close()
        try:
            print(self.client.write_register(100, val1, unit=1))
            print(self.client.write_register(101, val2, unit=1))
            print(self.client.write_register(102, val3, unit=1))
            print(self.client.write_register(103, val4, unit=1))
        except:
                print("Modbus fail")
                pass
        self.terminate()
        
    def disconnect(self):
        self.client.close()