import numpy as np
def readRSspec(name):
    f = open(name,'r')
    lines = f.readlines()
    start = 34
    freq = np.array([])
    power = np.array([])
    for l in lines[start:]:
        lsplit = l.split('\t')
        lsplit[0] = lsplit[0].replace(',','.')
        lsplit[1] = lsplit[1].replace(',','.')
        freq = np.append(freq,float(lsplit[0]))
        power = np.append(power,float(lsplit[1]))

    return [freq,power]

def readVNAspec(name,type=None):
    print name
    f = open(name,'r')
    lines = f.readlines()
    start = 42
    freq = np.array([])
    power = np.array([])
    for l in lines[start:-1]:
        if type == 'csv':
            lsplit = l.split(',')
        elif type == 'txt':
            lsplit = l.split('\t')
        fr = float(lsplit[3])
        p = float(lsplit[4])
        freq = np.append(freq,fr)
        power = np.append(power,p)

    return [freq,power]

def readVNAs11(name, type=None):
    print name
    f = open(name,'r')
    lines = f.readlines()
    start = 42
    freq = np.array([])
    power = np.array([])
    for l in lines[start:-1]:
        if type == 'csv':
            lsplit = l.split(',')
        elif type == 'txt':
            lsplit = l.split('\t')
        fr = float(lsplit[1])
        p = float(lsplit[2])
        freq = np.append(freq,fr)
        power = np.append(power,p)

    return [freq,power]
        
def readSAspec(name):
    f = open(name,'r')
    lines = f.readlines()
    nrpoint = 0
    freq = np.array([])
    power = np.array([])
    read =False
    count = 0
    for l in lines:
        if 'UI_DATA_POINTS' in l:
            nrpoint = int(float(l.split('=')[1][:-2]))
        if read == True and count < nrpoint:
            count +=1
            data = l.split('=')[1]
            f = float(data.split(',')[1][:-6])
            pow = float(data.split(',')[0])
            freq = np.append(freq,f)
            power = np.append(power,pow)
        if '# Begin TRACE A Data' in l:
            read = True
    return [freq,power]
