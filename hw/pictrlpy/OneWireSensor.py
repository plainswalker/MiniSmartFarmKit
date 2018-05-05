import os
import glob
import time

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

sensorval = None

def read_temp_raw():
    global device_file
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines


def read_temp():
    global device_file
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos + 2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        return temp_c, temp_f

def getsensorval():
    global sensorval
    return sensorval

def loop():
    global base_dir, device_file, device_folder, sensorval
    while True:
        try:
            sensorval = read_temp()
            if __name__ == '__main__': print(sensorval)
            time.sleep(1)
        except KeyboardInterrupt  as ctrlc:
            exit()

if __name__ == '__main__':
    loop()