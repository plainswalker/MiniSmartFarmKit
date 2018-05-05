import ArduinoSerialComm
import threading



def name() :
    return "humidity"

sensorloop = threading.Thread(None, ArduinoSerialComm.loop, 'thread_' +  name())

def get() :
    if not sensorloop.is_alive():
        return None
    return ArduinoSerialComm.getsensorval()

def run():
    sensorloop.start()

if __name__ == '__main__':
    run()