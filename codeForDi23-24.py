# Here is my code for my Destination Imagination year 3. 2023-2024
# this code's use is this:
# #1 one of the uses is to move a stepper motor back and forth
    # the stepper motor is using a conveyer belt like mechanism. 
    # you can see the video.
# #2 this is using a motion sensor which will start everything
# when the soccar ball or anything triggers the motion sensor, everything else will start
# 3 the I2C is what will help all of the led's trigger, since the rasperri pi cannot give enough power

# If you want to see how that worked out look at the video, for this year, and or the video of specificaly my creation. 


from gpiozero import MotionSensor
from gpiozero import LED
from time import sleep
from time import sleep
import RPi.GPIO as GPIO
import smbus
import sys



pir = MotionSensor(22)

led = LED(12)

PUL = 19
DIR = 20

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(PUL, GPIO.OUT)
GPIO.setup(DIR, GPIO.OUT)
#GPIO.setup(ENA, GPIO.OUT)

I2C_BUS = 1
I2C_ADR = 0x10
bus = smbus.SMBus(I2C_BUS)

durationFwd = 3000
durationBwc = 3000
delay = 0.0005
cycles = 100
cyclecount = 0

def forward():
#    GPIO.output(ENA, GPIO.HIGH)
#    GPIO.output(ENAI, GPIO.HIGH)

    sleep(.5)
    GPIO.output(DIR, GPIO.LOW)
    GPIO.output(DIR, GPIO.LOW)
    sleep(.5)
    #GPIO.output(DIRI, GPIO.LOW)

    for x in range(durationFwd):
        GPIO.output(PUL, GPIO.HIGH)
        GPIO.output(PUL, GPIO.HIGH)
        sleep(delay)
        GPIO.output(PUL, GPIO.LOW)
        GPIO.output(PUL, GPIO.LOW)
        sleep(delay)
#    GPIO.output(ENA, GPIO.LOW)
#    GPIO.output(ENAI, GPIO.LOW)
    sleep(.5)
#    return

def reverse():
#    GPIO.output(ENA, GPIO.HIGH)
#    GPIO.output(ENAI, GPIO.HIGH)

    sleep(.5)
    GPIO.output(DIR, GPIO.HIGH)
    GPIO.output(DIR, GPIO.HIGH)
    sleep(.5)
    #GPIO.output(DIRI, GPIO.HIGH)
    for y in range(durationBwc):
        GPIO.output(PUL, GPIO.LOW)
        GPIO.output(PUL, GPIO.LOW)
        sleep(delay)
        GPIO.output(PUL, GPIO.HIGH)
        GPIO.output(PUL, GPIO.HIGH)
        sleep(delay)
#    GPIO.output(ENA, GPIO.LOW)
#    GPIO.output(ENAI, GPIO.LOW)
    sleep(.5)

bus.write_byte_data(I2C_ADR, 1, 0x00)
bus.write_byte_data(I2C_ADR, 2, 0x00)
bus.write_byte_data(I2C_ADR, 3, 0x00)
bus.write_byte_data(I2C_ADR, 4, 0x00)

while True:
    pir.wait_for_motion()
    print("You moved!!")

    led.on()
    sleep(0.3)
    led.off()
    sleep(0.2)

    bus.write_byte_data(I2C_ADR, 1, 0xFF)
    sleep(0.3)
    bus.write_byte_data(I2C_ADR, 1, 0x00)


    forward()
    sleep(0.5)
    reverse()
    sleep(1.2)
#    cyclecount = (cyclecount + 1)

GPIO.cleanup()