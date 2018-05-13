import CdSphotoresistor
import threading

def name():
    return "illuminance"

sensorloop = threading.Thread(None,CdSphotoresistor.loop, 'thread_' +  name())

def get():
    if not sensorloop.is_alive():
        return None
    return CdSphotoresistor.getsensorval()

def run():
    sensorloop.start()

if __name__ == '__main__':
    run()