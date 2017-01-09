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

#files = sys.argv[1::2]
#leg = sys.argv[2::2]

folder = '/Users/romain/work/Auger/EASIER/data/20161012/'
folder1 = '/Users/romain/work/Auger/EASIER/data/20161012/'
folder2 = '/Users/romain/work/Auger/EASIER/data/20161028/'
files1 = [folder1 + '2sf.txt',folder1 + '3sf.txt',folder2 + '4sf.txt',folder2 + '5sf.txt',folder2 + '6sf.txt',folder2 + '7sf.txt',folder2 + '8sf.txt',folder2 + '9sf.txt']
leg = ['2','3','4','5','6','7','8','9']
iname = folder + 'i.txt'
tname = folder + 't.txt'
ispec = spectrum.Spectrum(iname)
ispec.load('vna','txt')
tspec = spectrum.Spectrum(tname)
tspec.load('vna','txt')

count = 0
fig = plt.figure()
gs = gridspec.GridSpec(2, 1,height_ratios=[3,1])
ax2 = plt.subplot(gs[1])
ax1 = plt.subplot(gs[0],sharex=ax2)
plt.setp(ax1.get_xticklabels(), visible=False)

for f1,l in zip(files1,leg):
    name1 = f1
    s1 = spectrum.Spectrum(name1)
    s1.load('vna','txt')
    s1.power = s1.power - ispec.power - tspec.power
    ax1.plot(s1.freq,s1.power,label=l)
#    ax2.plot(s1.freq,s1.power-s2.power)
    count +=1

    ax2.set_xlabel('frequency [GHz]')
    ax1.set_ylabel('gain [dB]')
    ax2.set_ylabel('diff [dB]')
    plt.grid(True)
#plt.ylabel('power [dBm/100kHz]')
    plt.legend()
    ax1.set_xlim(0.900,1.500)
    ax1.set_ylim(-6,6)
    ax2.set_ylim(-0.5,0.5)

plt.show()
