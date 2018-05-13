import OneWireSensor
import threading

def name():
    return "temperature"

sensorloop = threading.Thread(None,OneWireSensor.loop,'thread_' + name())


def get():
    if not sensorloop.is_alive():
        return None
    return OneWireSensor.getsensorval()

def run():
    sensorloop.start()

if __name__ == '__main__':
    run()