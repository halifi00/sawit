from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import modbus
from pymodbus.client.sync import ModbusSerialClient as ModbusSerialClient

        
client = ModbusSerialClient(method = 'rtu', port = "COM1",  baudrate = 9600,
                bytesize = 8, parity = "N", stopbits = 1, timeout = 1)
print(client.connect())
print(client.is_socket_open())

print(client.write_register(100, 1111, unit=1))
print(client.write_register(101, 222, unit=1))
print(client.write_register(102, 333, unit=1))
print(client.write_register(103, 444, unit=1))

client.close()
print(client.is_socket_open())
