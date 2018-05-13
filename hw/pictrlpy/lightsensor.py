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
        signal.pause()
    except (KeyboardInterrupt, SystemExit):
        exit(0)

if __name__ == '__main__':
    run()