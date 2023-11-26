from threading import Thread
import time
import smbus
import sys
import RPi.GPIO as GPIO
from time import sleep

ARD_PIN3 = 23
ARD_PIN2 = 22
LIMIT_SWITCH_L = 26
LIMIT_SWITCH_K = 5
POSITION_SWITCH = 24
SERVO = 21
I2C_BUS = 1
I2C_ADR = 0x10
I2C_ADR_2 = 0x11
bus = smbus.SMBus(I2C_BUS)

GPIO.setmode(GPIO.BCM)
GPIO.setup(POSITION_SWITCH, GPIO.IN)
status = 0
done = 0
def new_parallel_function(my_arg):
	global done
	global POSITION_SWITCH
	global I2C_ADR
	global status
	while done == 0:
		# check the switch
		sleep(0.01)
		if GPIO.input(POSITION_SWITCH) == True:
			if status == 0:
				status = 1
				bus.write_byte_data(I2C_ADR, 1, 0x0)
				bus.write_byte_data(I2C_ADR, 2, 0x0)
				bus.write_byte_data(I2C_ADR, 3, 0x0)
				bus.write_byte_data(I2C_ADR, 4, 0x0)
		else:
			status = 0
t = Thread(target=new_parallel_function, args=[1])
t.start()


def servo_on():
	bus.write_byte_data(I2C_ADR_2, 1, 0xFF)
	p.ChangeDutyCycle(5)
	sleep(0.5)
	p.ChangeDutyCycle(7.5)
	sleep(0.5)
	p.ChangeDutyCycle(10)
	sleep(0.5)
	p.ChangeDutyCycle(12.5)
	sleep(0.5)
	p.ChangeDutyCycle(10)
	sleep(0.7)
	p.ChangeDutyCycle(7.5)
	sleep(0.6)
	p.ChangeDutyCycle(5)
	sleep(0.5)
	p.ChangeDutyCycle(2.5)
	sleep(0.5)
	bus.write_byte_data(I2C_ADR_2, 1, 0x00)

def slide_left():
	bus.write_byte_data(I2C_ADR, 1, 0xFF)
	bus.write_byte_data(I2C_ADR, 2, 0x0)
	bus.write_byte_data(I2C_ADR, 3, 0x0)
	bus.write_byte_data(I2C_ADR, 4, 0x0)

def slide_left_little():
	bus.write_byte_data(I2C_ADR, 1, 0xFF)
	bus.write_byte_data(I2C_ADR, 2, 0x00)
	bus.write_byte_data(I2C_ADR, 3, 0x00)
	bus.write_byte_data(I2C_ADR, 4, 0x00)
	sleep(0.3)
	bus.write_byte_data(I2C_ADR, 1, 0x00)

def slide_right():
	bus.write_byte_data(I2C_ADR, 1, 0x0)
	bus.write_byte_data(I2C_ADR, 2, 0xFF)
	bus.write_byte_data(I2C_ADR, 3, 0x0)
	bus.write_byte_data(I2C_ADR, 4, 0x0)

def slide_right_little():
	bus.write_byte_data(I2C_ADR, 1, 0x00)
	bus.write_byte_data(I2C_ADR, 2, 0xFF)
	bus.write_byte_data(I2C_ADR, 3, 0x00)
	bus.write_byte_data(I2C_ADR, 4, 0x00)
	sleep(0.3)
	bus.write_byte_data(I2C_ADR, 2, 0x00)

def stop():
	bus.write_byte_data(I2C_ADR, 1, 0x0)
	bus.write_byte_data(I2C_ADR, 2, 0x0)
	bus.write_byte_data(I2C_ADR, 3, 0x0)
	bus.write_byte_data(I2C_ADR, 4, 0x0)
	GPIO.output(ARD_PIN2, GPIO.LOW)
	GPIO.output(ARD_PIN3, GPIO.LOW)

def forward():
	GPIO.output(ARD_PIN3, GPIO.LOW)
	GPIO.output(ARD_PIN2, GPIO.HIGH)

	for y in range(durationFwd):
		sleep(delay)
		#if GPIO.input(LIMIT_SWITCH_K) == True:
		#	break
	GPIO.output(ARD_PIN2, GPIO.LOW)
	#print('ENA set to LOW - Controller Disabled')
	sleep(.5)

def backward():
        GPIO.output(ARD_PIN2, GPIO.LOW)
        GPIO.output(ARD_PIN3, GPIO.HIGH)

        for y in range(durationBwd):
            sleep(delay)
            # if GPIO.input(LIMIT_SWITCH_L) == True:
            #    break
        GPIO.output(ARD_PIN3, GPIO.LOW)
        sleep(.5)


#GPIO.setmode(GPIO.BCM)
#GPIO.setmode(GPIO.BOARD)
GPIO.setup(SERVO, GPIO.OUT)
GPIO.setup(ARD_PIN3, GPIO.OUT)
GPIO.setup(ARD_PIN2, GPIO.OUT)
GPIO.setup(LIMIT_SWITCH_L, GPIO.IN)
GPIO.setup(LIMIT_SWITCH_K, GPIO.IN)

p = GPIO.PWM(SERVO, 50)
p.start(2.5)
durationFwd = 500
durationBwd = 500
delay = 0.003

while True:
	try:
		option = input()

		if option == 'd':
			slide_right()

		elif option == 'a':
			slide_left()

		elif option == 's':
			stop()

		elif option == 'p':
			servo_on()

		elif option == 'l':
			forward()

		elif option == 'k':
			backward()

		elif option == 'aa':
			slide_left_little()

		elif option == 'dd':
			slide_right_little()



	except KeyboardInterrupt as e:
		print("quit")
		p.stop()
		GPIO.cleanup()
		sys.exit()

