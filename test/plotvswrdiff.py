import matplotlib.pyplot as plt
import matplotlib
import matplotlib.gridspec as gridspec
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

files = sys.argv[1::2]
leg = sys.argv[2::2]

fig = plt.figure()
#fig.suptitle('gain',fontsize=15,fontweight='bold')
gs = gridspec.GridSpec(2, 1,height_ratios=[3,1])
ax2 = plt.subplot(gs[1])
ax1 = plt.subplot(gs[0],sharex=ax2)
plt.setp(ax1.get_xticklabels(), visible=False)
folder = '/Users/romain/work/Auger/EASIER/data/20161012/'

iname = folder + 'i.txt'
tname = folder + 't.txt'
ispec = spectrum.Spectrum(iname)
ispec.load('s11','txt')
tspec = spectrum.Spectrum(tname)
tspec.load('s11','txt')


count = 0
sref = spectrum.Spectrum()
for f,l in zip(files,leg):
    name = folder  + f
    s = spectrum.Spectrum(name)
    s.load('s11','txt')
    s.power = s.power
    if count == 0:
        sref = s
    ax1.plot(s.freq,s.power,label=l)
    ax2.plot(s.freq,s.power-sref.power,label=l)
    count +=1



ax2.set_xlabel('frequency [GHz]')
ax1.set_ylabel('vswr')
ax2.set_ylabel('diff')
plt.grid(True)
#plt.ylabel('power [dBm/100kHz]')
plt.legend(loc=3)
ax1.set_xlim(0.900,1.500)
ax1.set_ylim(1,2)
ax2.set_ylim(-2,1)

plt.show()
