import OneWireSensor
import threading
import signal

def name():
    return "temperature"

sensorloop = threading.Thread(None,OneWireSensor.loop,'thread_' + name())


def get():
    if not sensorloop.is_alive():
        return None
    return OneWireSensor.getsensorval()

def run():
    try:
        sensorloop.start()
        sensorloop.setDaemon(True)
        while sensorloop.is_alive():
            pass
    except (KeyboardInterrupt, SystemExit):
        exit(0)

if __name__ == '__main__':
    run()