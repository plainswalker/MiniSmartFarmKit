import serial

serialcomm = serial.Serial('/dev/ttyACM0', 9600)

MAX_BUF = 20
ardubuff = []
buffidx = 0

while True:
    ardubuff[buffidx] = serialcomm.readline()
    print(buffidx)
    buffidx = (buffidx + 1) % MAX_BUF