'''
This code is just the outline for when you want to use i2c
- to see the location of the relays you can type in: (i2cdetect -y 1) into the terminal to see the locations.
'''

import time
import smbus
import sys
import RPi.GPIO as GPIO
from time import sleep

I2C_BUS = 1
#I2C_ADR = 0x10
I2C_ADR = 0x11
bus = smbus.SMBus(I2C_BUS)

bus.write_byte_data(I2C_ADR, 1, 0xFF)
bus.write_byte_data(I2C_ADR, 2, 0x00)
bus.write_byte_data(I2C_ADR, 3, 0x00)
bus.write_byte_data(I2C_ADR, 4, 0x00)
