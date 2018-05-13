import os

import CdSphotoresistor
import threading
import signal

def name():
    return "illuminance"

sensorloop = threading.Thread(None,CdSphotoresistor.loop, 'thread_' +  name())

def get():
    if not sensorloop.is_alive():
        return None
    return CdSphotoresistor.getsensorval()

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