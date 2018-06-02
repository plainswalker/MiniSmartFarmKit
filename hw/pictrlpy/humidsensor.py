import os

import ArduinoSerialComm
import threading
import signal


def name() :
    return "humidity"

sensorloop = threading.Thread(None, ArduinoSerialComm.loop, 'thread_' +  name())
threshold = 0.6
range = 0.4
hi = 540
lo = 300

def setcond(thr = None, rng = None, dry = None, wet = None):
    global threshold, range
    if thr is not None:
        threshold = thr
    if range is not None:
        range = rng
    if dry  is not None:
        hi = dry
    if wet  is not None:
        lo = wet

def getval() :
    if not sensorloop.is_alive():
        return None
    ratio = 1.0 - (ArduinoSerialComm.getsensorval() - lo)/(hi - lo)
    return round(ratio, 2)

def getstate():
    if not sensorloop.is_alive():
        return None
    ratio = getval()
    if ratio > threshold + range or ratio < threshold - range:
        return 'bad'
    else :
        return 'good'

def run():
    try:
        sensorloop.setDaemon(True)
        sensorloop.start()
        if __name__ == '__main__':
            while sensorloop.is_alive():
                pass
    except (KeyboardInterrupt, SystemExit):
        exit(0)

if __name__ == '__main__':
    run()
