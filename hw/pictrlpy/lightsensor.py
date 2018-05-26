import os

import CdSphotoresistor
import threading
import signal

def name():
    return "illuminance"

sensorloop = threading.Thread(None,CdSphotoresistor.loop, 'thread_' +  name())
threshold = 1500
range = 1500
currentstate = None


def setcond(thr = None, rng = None):
    global threshold, range
    if thr is not None:
        threshold = thr
    if range is not None:
        range = rng

def getval():
    if not sensorloop.is_alive():
        return None
    return CdSphotoresistor.getsensorval()

def getstate():
    if not sensorloop.is_alive():
        return None
    val = getval()
    if val > threshold + range:
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