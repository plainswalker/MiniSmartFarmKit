import RPi.GPIO as GPIO
import time
import os

sensorval = None

DEBUG = 1
GPIO.setmode(GPIO.BCM)


def RCtime(RCpin):
    reading = 0
    try:
        GPIO.setup(RCpin, GPIO.OUT)
    except Exception as e:
        print(e)
        return e
    GPIO.output(RCpin, GPIO.LOW)
    time.sleep(0.1)

    GPIO.setup(RCpin, GPIO.IN)

    # This takes about 1 millisecond per loop cycle
    while (GPIO.input(RCpin) == GPIO.LOW):
        reading += 1
    return reading

def getsensorval():
    return sensorval

while True:
    try:
        sensorval = RCtime(18)
        print(sensorval)  # Read RC timing using pin #18
    except KeyboardInterrupt as ctrlc:
        print(ctrlc)
        exit()
