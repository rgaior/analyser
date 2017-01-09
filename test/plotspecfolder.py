import matplotlib.pyplot as plt
import matplotlib
matplotlib.rc('xtick', labelsize=15)
matplotlib.rc('ytick', labelsize=15)
import numpy as np
import os
import sys
import glob
cwd = os.getcwd()
classpath = cwd + '/../classes/'
utilspath = cwd + '/../utils/'
sys.path.append(utilspath)
sys.path.append(classpath)
import utils
import spectrum

files = sys.argv[1::3]
leg = sys.argv[2::3]
fileorfold = sys.argv[3::3]
fileorfold = np.asarray(fileorfold,dtype=int)

fig = plt.figure(figsize=(8,6))
ax = plt.subplot(111)
folder = '/Users/romain/Dropbox/Public/EASIER/malargue2016/onsite/20160525/spectrum/'
#files = ['pampa.spa','pampa_#1.spa']
#leg = ['0','1']

count = 0
for f,l,t in zip(files,leg,fileorfold):
    if t == 0:
        name = folder  + f
        s = spectrum.Spectrum(name)
        s.load('sa')
        ax.plot(s.freq,s.power,label=l)
    elif t == 1:
        print folder  + f+'/*'
        names = glob.glob(folder  + f+'/*')
        for n in names:
            s = spectrum.Spectrum(n)
            s.load('sa')
            ax.plot(s.freq,s.power,label=l)
            

plt.xlabel('frequency [MHz]')
plt.ylabel('power [dBm/RBW]')
plt.legend()
plt.show()
