import sys

import server
import protocol

import time

if len(sys.argv) > 1:
    id = sys.argv[1]
else :
    id = 'hwtest00'
numOfPlant = 1
Plants = {
    '1' : 1
}
uprate = 1

inmodules = {} # modules : {'name' : module, ...}
outmodules = {}

def init(ims = [], oms = []):
    server.init()
    for m in ims:
        inmodules[m.name()] = m
    for m in oms:
        outmodules[m.name()] = m
    if __name__ == '__main__':
        loop()

def get(key):
    return server.get(['Plants', key])

def update():
    global id, numOfPlant, Plants
    for k in list(inmodules.keys()):
        val = inmodules[k].getval()
        state = inmodules[k].getstate()
        if val is not None:
            server.set(['userFarm', id, k, 'sensorvalue'], val)
            server.set(['userFarm', id, k, 'status'], state)
def loop():
    while True:
        update()
        time.sleep(1)

if __name__ == '__main__':
    init()
