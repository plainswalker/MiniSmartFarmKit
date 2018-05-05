import lightsensor
import humidsensor
import tmprsensor

def modules ():
    return [lightsensor, humidsensor, tmprsensor]

def run(name = ''):
    mds = modules()
    for md in mds :
        if name == md.name():
            try :
                md.run()
            except Exception as e:
                print(e)
    return

def get(name = ''):
    mds = modules()
    rt = []
    for md in mds :
        if name == md.name():
            try :
                getval = md.get()
            except Exception as e:
                getval = None
                print(e)
            rt.append((name, getval))
    return rt