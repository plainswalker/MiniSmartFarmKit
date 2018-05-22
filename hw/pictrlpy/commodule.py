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
        run()

def get(key):
    return server.get(['Plants', key])

def update():
    global id, numOfPlant, Plants
    for k in list(inmodules.keys()):
        val = inmodules[k].get()
        if val is not None:
            server.set(['userFarm', id, 'Plants', '1', '0001', k], val)
def run():
    while True:
        update()
        time.sleep(1)

if __name__ == '__main__':
    init()