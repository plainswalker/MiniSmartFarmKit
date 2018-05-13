import os

import ArduinoSerialComm
import threading
import signal


def name() :
    return "humidity"

sensorloop = threading.Thread(None, ArduinoSerialComm.loop, 'thread_' +  name())

def get() :
    if not sensorloop.is_alive():
        return None
    return ArduinoSerialComm.getsensorval()

def run():
    try:
        sensorloop.start()
        sensorloop.setDaemon(True)
        while sensorloop.is_alive():
            pass
    except (KeyboardInterrupt, SystemExit):
        os.kill(os.getpgid(), signal.SIGKILL)

if __name__ == '__main__':
    run()