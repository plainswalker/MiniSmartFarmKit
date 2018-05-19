import RPi.GPIO as GPIO
import time
import os

sensorval = None

DEBUG = 1
GPIO.setmode(GPIO.BCM)


def RCtime(RCpin):
    global DEBUG
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
    global sensorval
    return sensorval

def loop():
    global sensorval, DEBUG
    while True:
        try:
            sensorval = RCtime(18)
            if __name__ == '__main__': print(sensorval)  # Read RC timing using pin #18
        except KeyboardInterrupt as ctrlc:
            if __name__ == '__main__': print(ctrlc)
            exit()

if __name__ == '__main__':
    loop()