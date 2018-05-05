import lightsensor
import humidsensor
import tmprsensor

def modules ():
    return [lightsensor, humidsensor, tmprsensor]
def get(idx = 0) :
    if idx is not None:
        mds = modules()
        rt = []
        name = None
        getval = None
        for md in mds :
            try :
                name = md.name()
                getval = md.get()
            except Exception as e:
                print(e)
            rt.append((name, getval))
        return rt