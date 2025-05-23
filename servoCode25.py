'''
this is the part 1 code for the dissasebly device
2025
'''
from threading import Thread
import time
import smbus
import sys
import RPi.GPIO as GPIO
from time import sleep


SERVO16 = 16
SERVO25 = 25
SERVO6 = 6
SERVO4 = 4
I2C_BUS = 1
#bus = smbus.SMBus(I2C_BUS)


GPIO.setmode(GPIO.BCM)

def servoForward():
	#bus.write_byte_data(I2C_ADR2, 1, 0xFF)
	p.start(2.5)
	s.start(2.5)
	q.start(2.5)
	w.start(2.5)
	p.ChangeDutyCycle(3)
	s.ChangeDutyCycle(3)
	q.ChangeDutyCycle(3)
	w.ChangeDutyCycle(3)
	sleep(0.5)

def servoForward2():
	p.start(2.5)
	s.start(2.5)
	q.start(2.5)
	w.start(2.5)

def servoBackwards():
	p.ChangeDutyCycle(30)
	s.ChangeDutyCycle(30)
	q.ChangeDutyCycle(30)
	w.ChangeDutyCycle(30)
	p.start(2)
	s.start(2)
	w.start(2)
	q.start(2)
	sleep(0.5)


GPIO.setup(SERVO16, GPIO.OUT)
GPIO.setup(SERVO25, GPIO.OUT)
GPIO.setup(SERVO6, GPIO.OUT)
GPIO.setup(SERVO4, GPIO.OUT)
p = GPIO.PWM(SERVO16, 50)
s = GPIO.PWM(SERVO25, 50)
q = GPIO.PWM(SERVO6, 50)
w = GPIO.PWM(SERVO4, 50)
p.start(2.5)
s.start(2.5)
q.start(2.5)
w.start(2.5)

while True:
	try:
		option = input()

		if option == 'w':
			servoForward()

		elif option == 's':
			p.stop()
			s.stop()

		elif option == 'q':
			servoForward()
		elif option == 'z':
			servoBackwards()

	except KeyboardInterrupt as e:
		print("quit")
		p.stop()
		s.stop()
		q.stop()
		w.start()
		GPIO.cleanup()
		sys.exit()
