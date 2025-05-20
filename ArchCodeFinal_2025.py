'''
This is my code for my last year of Destination Imagination. 
My sister and I created this project (I coded it). This device assembles an arch by itself, using window motors, electro magnets, magnets, raspberry pi, and more. 
If you want to see how it works, check my instagram account where a video will be uploaded soon.
This is the final draft, and what we used for our Globals Competition
'''
from threading import Thread
import sys
import smbus
import RPi.GPIO as GPIO
import time
from time import sleep


I2C_ADR = 0x11
I2C_ADR2 = 0x10
I2C_BUS = 1
bus = smbus.SMBus(I2C_BUS)


def bothForward():
	# TODO: this has to have two of the realys open but for the forward
	bus.write_byte_data(I2C_ADR, 1, 0xFF)
	bus.write_byte_data(I2C_ADR, 2, 0x00)
	bus.write_byte_data(I2C_ADR, 3, 0x00)
	bus.write_byte_data(I2C_ADR, 4, 0xFF)

def bothBackward():
	#TODO: this one also needs two of the relays open but for the backward
	bus.write_byte_data(I2C_ADR, 1, 0x00)
	bus.write_byte_data(I2C_ADR, 2, 0xFF)
	bus.write_byte_data(I2C_ADR, 3, 0xFF)
	bus.write_byte_data(I2C_ADR, 4, 0x00)

def leftForward():
	bus.write_byte_data(I2C_ADR, 1, 0x00)
	bus.write_byte_data(I2C_ADR, 2, 0x00)
	bus.write_byte_data(I2C_ADR, 3, 0x00)
	bus.write_byte_data(I2C_ADR, 4, 0xFF)

def rightForward():
	bus.write_byte_data(I2C_ADR, 1, 0xFF)
	bus.write_byte_data(I2C_ADR, 2, 0x00)
	bus.write_byte_data(I2C_ADR, 3, 0x00)
	bus.write_byte_data(I2C_ADR, 4, 0x00)


def leftBackward():
	bus.write_byte_data(I2C_ADR, 1, 0x00)
	bus.write_byte_data(I2C_ADR, 2, 0x00)
	bus.write_byte_data(I2C_ADR, 3, 0xFF)
	bus.write_byte_data(I2C_ADR, 4, 0x00)

def rightBackward():
	bus.write_byte_data(I2C_ADR, 1, 0x00)
	bus.write_byte_data(I2C_ADR, 2, 0xFF)
	bus.write_byte_data(I2C_ADR, 3, 0x00)
	bus.write_byte_data(I2C_ADR, 4, 0x00)

# this stops all the motors, and closes all the relays
def bothStop():
    bus.write_byte_data(I2C_ADR, 1, 0x00)
    bus.write_byte_data(I2C_ADR, 2, 0x00)
    bus.write_byte_data(I2C_ADR, 3, 0x00)
    bus.write_byte_data(I2C_ADR, 4, 0x00)
    bus.write_byte_data(I2C_ADR2, 1, 0x00)
    bus.write_byte_data(I2C_ADR2, 2, 0x00)
    bus.write_byte_data(I2C_ADR2, 3, 0x00)
    bus.write_byte_data(I2C_ADR2, 4, 0x00)


# this assembles the majority of the arch
def fullThing():
    bus.write_byte_data(I2C_ADR, 3, 0xFF)
    sleep(3)
    bus.write_byte_data(I2C_ADR, 3, 0x00)
    sleep(1)
    bus.write_byte_data(I2C_ADR, 4, 0xFF)
    sleep(4)
    bus.write_byte_data(I2C_ADR, 4, 0x00)
    sleep(2)
    
    bus.write_byte_data(I2C_ADR, 1, 0xFF)
    sleep(3.1)
    bus.write_byte_data(I2C_ADR, 1, 0x00)
    sleep(1)
    bus.write_byte_data(I2C_ADR, 2, 0xFF)
    sleep(4)
    bus.write_byte_data(I2C_ADR, 2, 0x00)
    sleep(3)
    
def trySomething():
    bus.write_byte_data(I2C_ADR, 3, 0xFF)
    sleep(4)
    bus.write_byte_data(I2C_ADR, 3, 0x00)
    sleep(1)
    bus.write_byte_data(I2C_ADR, 4, 0xFF)
    sleep(2)
    bus.write_byte_data(I2C_ADR, 4, 0x00)
    sleep(3)

# this brings the window motor with the electromagnet down
def topWindowMotorDown():
    bus.write_byte_data(I2C_ADR2, 1, 0x00)
    bus.write_byte_data(I2C_ADR2, 2, 0x00)
    bus.write_byte_data(I2C_ADR2, 3, 0xFF)
    bus.write_byte_data(I2C_ADR2, 4, 0x00)

# this brings the widow motor with the electromagnet up
def topWindowMotorUp():
    bus.write_byte_data(I2C_ADR2, 1, 0x00)
    bus.write_byte_data(I2C_ADR2, 2, 0x00)
    bus.write_byte_data(I2C_ADR2, 3, 0x00)
    bus.write_byte_data(I2C_ADR2, 4, 0xFF)


def magnetOn():
    bus.write_byte_data(I2C_ADR2, 1, 0x00)
    bus.write_byte_data(I2C_ADR2, 2, 0xFF)
    bus.write_byte_data(I2C_ADR2, 3, 0x00)
    bus.write_byte_data(I2C_ADR2, 4, 0x00)
    
def magnetOff():
    bus.write_byte_data(I2C_ADR2, 2, 0x00)
    bus.write_byte_data(I2C_ADR2, 1, 0x00)
    bus.write_byte_data(I2C_ADR2, 3, 0x00)
    bus.write_byte_data(I2C_ADR2, 4, 0x00)
    
def fullThing2():
    bus.write_byte_data(I2C_ADR, 3, 0xFF)
    sleep(3)
    bus.write_byte_data(I2C_ADR, 3, 0x00)
    sleep(1)
    bus.write_byte_data(I2C_ADR, 4, 0xFF)
    sleep(4)
    bus.write_byte_data(I2C_ADR, 4, 0x00)
    sleep(2)
    #####
    bus.write_byte_data(I2C_ADR, 1, 0xFF)
    sleep(3.1)
    bus.write_byte_data(I2C_ADR, 1, 0x00)
    sleep(1)
    bus.write_byte_data(I2C_ADR, 2, 0xFF)
    sleep(4)
    bus.write_byte_data(I2C_ADR, 2, 0x00)
    sleep(3)
    bus.write_byte_data(I2C_ADR2, 3, 0xFF)
    sleep(3)
    bus.write_byte_data(I2C_ADR2, 3, 0x00)
    #####
    bus.write_byte_data(I2C_ADR2, 4, 0xFF)
    sleep(3)
    bus.write_byte_data(I2C_ADR2, 4, 0x00)


# these are the keys to make it move, where you can control it
while True:
    try:
        option = input()

        if option == 'a':
            bothForward()
            print("both forward")

        elif option == 'd':
            bothBackward()
            print("both backward")

        elif option == 's':
            bothStop()
            print("both stop")

        elif option == 'r':
            rightForward()
            print("right forward")

        elif option == 't':
            rightBackward()
            print("right backward")

        elif option == 'l':
            leftForward()
            print("left foward")

        elif option == 'k':
            leftBackward()
            print("left backward")
   
        elif option == 'p':
            fullThing()
            print("full thing")
        elif option == 'y':
            trySomething()
            print("left backward")
            
        elif option == 'h':
            topWindowMotorDown()
            print("top window motor down")
            
        elif option == 'g':
            topWindowMotorUp()
            print("top window motor up")
            
        elif option == "m":
            magnetOn()
            print("magnet on")
            
        elif option == "n":
            magnetOff()
            print("magnet off")
            
        elif option == "y":
            fullThing2()
            print("full thing #2")
   

    except KeyboardInterrupt as e:
        print("Interrupted")
        sys.exit()
