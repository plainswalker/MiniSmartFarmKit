import pyrebase
import sys

def setconfig(key=None, domain=None, URL=None, ID=None, storbuck=None, sender=None, accnt=None):
    global config
    if key is not None:
        config['apiKey'] = key
    if domain is not None:
        config['authDomain'] = domain
    if URL is not None:
        config['databaseURL'] = URL
    if ID is not None:
        config['projectId'] = ID
    if storbuck is not None:
        config['storageBucket'] = storbuck
    if sender is not None:
        config['messagingSenderId'] = sender
    if accnt is not None:
        config['serviceAccount'] = accnt
key = ''
if len(sys.argv) > 1 :
    key = sys.argv[1]
elif __name__ == '__main__' :
    key = input('input apikey : ')
else :
    try :
        keyfile = open('.apikey', 'r')
        key = keyfile.readline().strip()
    except FileNotFoundError :
        pass

config = {
    'apiKey': key,
    'authDomain' : "capstonemaster-3b52b.firebaseapp.com",
    'databaseURL': "https://capstonemaster-3b52b.firebaseio.com",
    'projectId': "capstonemaster-3b52b",
    'storageBucket' : "capstonemaster-3b52b.appspot.com",
    'messagingSenderId': "463496465390"
}

def get(key=[]):
    res=db
    for k in key:
        res = res.child(k)
    return res.get().val()

def set(key=[], val=None):
    res = db
    for k in key:
        res = res.child(k)
    res.set(val)

def init():
    global fb, db
    fb = pyrebase.initialize_app(config)
    db = fb.database()

if __name__ == '__main__':
    init()



