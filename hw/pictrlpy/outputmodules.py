
def modules():
    return []

def set(name, val = None):
    if val :
        try:
            for md in modules() :
                if name == md.name():
                    md.set(val)
        except Exception as e:
            print(e)
    return