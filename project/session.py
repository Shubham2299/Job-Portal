uid=''
cid=0
month=''
desig=''
year=''
count=0
def setUid(u_id):
    global uid
    uid=u_id
def getUid():
    global uid
    return uid

def setCid(c_id):
    global cid
    cid=c_id
def getCid():
    global cid
    return cid

def setMon(mon):
    global month
    month=mon
def getMon():
    global month
    return month

def setDeg(deg):
    global desig
    desig=deg
def getDeg():
    global desig
    return desig

def setYear(y):
    global year
    year=y
def getYear():
    global year
    return year


def setCount():
    global count
    count+=1
def getCount():
    global count
    return count
def backCount():
    global count
    count=0

