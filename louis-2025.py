'''
This code is for a robot I created with my friend for our 2025 Globals. One team member crotcheted the body of a peanut, and I coded and wired.
This robot changes facial expressions from evil, to concerned while moving his arms. 
	Essentially, we created a toy, crotcheted, robot in the shape of a peanut. 
'''
from threading import Thread
import time
import smbus
import sys
import RPi.GPIO as GPIO
from time import sleep
import datetime

SERVO = 16
SERVO2 = 5
SERVO3 = 12
SERVO4 = 4
SERVO5 = 24

GPIO.setmode(GPIO.BCM)
status = 0
done = 0

start_time2 = time.time()

def sadServo():
	faceServo1.ChangeDutyCycle(5)
	faceServo2.ChangeDutyCycle(5)
	faceServo3.ChangeDutyCycle(5)
	sleep(0.5)
	faceServo1.ChangeDutyCycle(7.5)
	faceServo2.ChangeDutyCycle(7.5)
	faceServo3.ChangeDutyCycle(7.5)
	sleep(0.5)
	while time.time() - start_time2 < 6:
		print("working...")
		faceServo5.ChangeDutyCycle(7.6)
		faceServo4.ChangeDutyCycle(7.6)
		sleep(1)
		faceServo5.ChangeDutyCycle(5)
		faceServo4.ChangeDutyCycle(5)
		time.sleep(1)

def happyServo():
    faceServo1.ChangeDutyCycle(2.5)
    faceServo2.ChangeDutyCycle(2.5)
    faceServo3.ChangeDutyCycle(2.5)
    while time.time() - start_time2 < 6:
        print("working...")
        faceServo5.ChangeDutyCycle(7.6)
        faceServo4.ChangeDutyCycle(7.6)
        sleep(1)
        faceServo5.ChangeDutyCycle(5)
        faceServo4.ChangeDutyCycle(5)
        time.sleep(1)

def hands():
	while time_time() - start_time2 < 6:
		print("working...")
		faceServo5.ChangeDutyCycle(5)
		faceServo4.ChangeDutyCycle(5)

		faceServo5.ChangeDutyCycle(2)
		faceServo4.ChangeDutyCycle(2)
		time.sleep(1)

GPIO.setup(SERVO, GPIO.OUT)
GPIO.setup(SERVO2, GPIO.OUT)
GPIO.setup(SERVO3, GPIO.OUT)
GPIO.setup(SERVO4, GPIO.OUT)
GPIO.setup(SERVO5, GPIO.OUT)

faceServo1 = GPIO.PWM(SERVO, 50)
faceServo2 = GPIO.PWM(SERVO2, 50)
faceServo3 = GPIO.PWM(SERVO3, 50)
faceServo4 = GPIO.PWM(SERVO4, 50)
faceServo5 = GPIO.PWM(SERVO5, 50)


faceServo1.start(2.5)
faceServo2.start(2.5)
faceServo3.start(2.5)
faceServo4.start(2.5)
faceServo5.start(2.5)


durationFWD = 500
durationBWD = 500
delay = 0.003


while True:
	try:
		option = input()

		if option == 'd':
			happyServo()
			print("happy servo")

		elif option == 'a':
			sadServo()
			print("sad servo")

		elif option == 'h':
			hands()
			print("handsMoving")


	except KeyboardInterrupt as e:
		print("quit")
		faceServo1.stop()
		faceServo2.stop()
		faceServo3.stop()
