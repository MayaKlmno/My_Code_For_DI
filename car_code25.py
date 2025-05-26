"""
this code makes a car move. The car uses 2 window motors, and a raspberry pi.
I used this code for my 2025 Destination Imagination

 Things:
 	- to check the location of the relays type: i2cdetect -y 1    into the terminal. This gives the addreses for the relays being used. 
"""

import time
import smbus
import sys
import RPi.GPIO as GPIO
from time import sleep

I2C_BUS = 1
I2C_BUS2 = 1
I2C_ADR = 0x10
I2C_ADR2 = 0x12

bus = smbus.SMBus(I2C_BUS)
bus2 = smbus.SMBus(I2C_BUS2)

def turnLeft():
	bus.write_byte_data(I2C_ADR, 1, 0xFF)
	bus.write_byte_data(I2C_ADR, 2, 0x00)
	bus.write_byte_data(I2C_ADR, 3, 0x00)
	bus.write_byte_data(I2C_ADR, 4, 0x00)

def turnRight():
	bus.write_byte_data(I2C_ADR, 1, 0x00)
	bus.write_byte_data(I2C_ADR, 2, 0x00)
	bus.write_byte_data(I2C_ADR, 3, 0xFF)
	bus.write_byte_data(I2C_ADR, 4, 0x00)

def forward():
	bus.write_byte_data(I2C_ADR, 1, 0xFF)
	bus.write_byte_data(I2C_ADR, 3, 0xFF)
	bus.write_byte_data(I2C_ADR, 2, 0x00)
	bus.write_byte_data(I2C_ADR, 4, 0x00)

def backward():
	bus.write_byte_data(I2C_ADR, 2, 0xFF)
	bus.write_byte_data(I2C_ADR, 4, 0xFF)
	bus.write_byte_data(I2C_ADR, 1, 0x00)
	bus.write_byte_data(I2C_ADR, 3, 0x00)


def stop():
	bus.write_byte_data(I2C_ADR, 1, 0x00)
	bus.write_byte_data(I2C_ADR, 2, 0x00)
	bus.write_byte_data(I2C_ADR, 3, 0x00)
	bus.write_byte_data(I2C_ADR, 4, 0x00)
	bus.write_byte_data(I2C_ADR2, 1, 0x00)
	bus.write_byte_data(I2C_ADR2, 2, 0x00)
	bus.write_byte_data(I2C_ADR2, 3, 0x00)
	bus.write_byte_data(I2C_ADR2, 4, 0x00)

def flap1():
	bus.write_byte_data(I2C_ADR2, 1, 0x00)
	bus.write_byte_data(I2C_ADR2, 2, 0x00)
	bus.write_byte_data(I2C_ADR2, 3, 0x00)
	bus.write_byte_data(I2C_ADR2, 4, 0x00)

def flap2():
	bus.write_byte_data(I2C_ADR2, 1, 0x00)
	bus.write_byte_data(I2C_ADR2, 2, 0x00)
	bus.write_byte_data(I2C_ADR2, 3, 0x00)
	bus.write_byte_data(I2C_ADR2, 4, 0x00)


while True:
	try:
		option = input()

		if option == 'd':
			turnRight()
		elif option == 'a':
			turnLeft()
		elif option == 's':
			stop()
		elif option == 'x':
			backward()
		elif option == 'w':
			forward()
		elif option == 'j':
			flap1()
		elif option == 'k':
			flap2()
	except KeyboardInterrupt as e:
		print("quit")
		sys.exit()
