import RPi.GPIO as GPIO
import time
import os

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


while True:
    try:
        print(RCtime(18))  # Read RC timing using pin #18
    except KeyboardInterrupt as ctrlc:
        print(ctrlc)
        exit()
