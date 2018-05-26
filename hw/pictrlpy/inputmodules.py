import lightsensor
import humidsensor
import tmprsensor



def modules ():
    return [lightsensor, humidsensor, tmprsensor]

def run(name = ''):
    mds = modules()
    for md in mds :
        if name == '' or name == md.name():
            try :
                md.run()
            except Exception as e:
                print(e)
    return

def setcond(name = '', thr = None, rng = None):
    mds = modules()
    for md in mds:
        if name == md.name():
            try:
                md.setcond(thr, rng)
            except Exception as e:
                val = None
                print(e)

def getval(name = ''):
    mds = modules()
    rt = []
    for md in mds :
        if name == md.name():
            try :
                val = md.getval()
            except Exception as e:
                val = None
                print(e)
            rt.append((name, val))
    return rt

def getstate(name = ''):
    mds = modules()
    rt = []
    for md in mds :
        if name == md.name():
            try :
                st = md.getstate()
            except Exception as e:
                st = None
                print(e)
            rt.append((name, st))
    return rt