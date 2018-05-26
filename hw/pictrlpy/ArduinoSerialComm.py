import serial

serialcomm = serial.Serial('/dev/ttyACM0', 9600)

MAX_BUF = 20
ardubuff = [None] * MAX_BUF
buffidx = 0

def loop():
    global MAX_BUF, ardubuff, buffidx
    while True:
        try:
            ardubuff[buffidx] = serialcomm.readline()
            if __name__ == '__main__': print(getsensorval())

            buffidx = (buffidx + 1) % MAX_BUF
        except KeyboardInterrupt as ctrlc:
            if __name__ == '__main__': print(ctrlc)
            exit()

def getsensorval():
    global ardubuff, buffidx
    if ardubuff[buffidx] is not None: return int("".join(filter(str.isdigit, str(ardubuff[buffidx].strip()))))
    else : return 0
if __name__ == '__main__':
    loop()
