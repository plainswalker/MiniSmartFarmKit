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
    try:
        sensorloop.start()
        sensorloop.join()
    except (KeyboardInterrupt, SystemExit):
        exit(0)

if __name__ == '__main__':
    run()