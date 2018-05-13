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
            print(ardubuff[buffidx])

            buffidx = (buffidx + 1) % MAX_BUF
        except KeyboardInterrupt as ctrlc:
            print(ctrlc)
            exit()

def getsensorval():
    global ardubuff, buffidx
    return ardubuff[buffidx]

if __name__ == '__main__':
    loop()