#!/usr/bin/env python3
from pymodbus.client import ModbusSerialClient
import time

#init modbus device
client = ModbusSerialClient(method='rtu', port='/dev/ttyACM0', baudrate=9600)
client2 = ModbusSerialClient(method='rtu', port='/dev/ttyUSB1', baudrate=9600)
loop = False

def testBatch():
    #writeRly = client.write_coil(1, True, slave = 1)
    #writeRly = client.write_coil(2, True, slave = 1)
    #writeRly = client.write_coil(3, True, slave = 1)
    #writeRly = client.write_coil(4, True, slave = 1)
    #writeRly = client.write_coil(5, True, slave = 1)
    #print(writeRly)
    
    getElect = client.read_holding_registers(0, 29, slave = 2)
    print(getElect.registers)
    getTemp = client.read_holding_registers(4, 3, slave = 3)   
    print(getTemp.registers) 
    getH2 = client2.read_holding_registers(0, 10, slave = 4)
    print(getH2.registers)
    getMoist = client2.read_input_registers(0, 3, slave = 5)
    print(getMoist.registers[0])
    print(getMoist.registers[2])
    
    print("~~~")

#Loop
if loop:
    while True:
        testBatch()
        time.sleep(2)
else:   
    testBatch()
