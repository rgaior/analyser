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
#folder1 = '/Users/romain/work/Auger/EASIER/data/20161012/'
#folder2 = '/Users/romain/work/Auger/EASIER/data/20161031/gain/'
#files1 = ['2af.txt','2sf.txt','3af.txt','3sf.txt']
#files2 = ['2af_#1.txt','2sf.txt','3af.txt','3sf.txt']

###############################
## specific case for LNA "0"###
folder1 = '/Users/romain/work/Auger/EASIER/data/20161012/'
#folder1 = '/Users/romain/work/Auger/EASIER/data/20161028/'
folder2 = '/Users/romain/work/Auger/EASIER/data/20161012/'
#folder2 = '/Users/romain/work/Auger/EASIER/data/20161102/'
files1 = ['0af.txt']
files2 = ['1af.txt']
###############################

iname = folder + 'i.txt'
tname = folder + 't.txt'
ispec = spectrum.Spectrum(iname)
ispec.load('vna','txt')
tspec = spectrum.Spectrum(tname)
tspec.load('vna','txt')

count = 0
for f1,f2 in zip(files1,files2):
    print f1
    print f2
    fig = plt.figure()
    gs = gridspec.GridSpec(2, 1,height_ratios=[3,1])
    ax2 = plt.subplot(gs[1])
    ax1 = plt.subplot(gs[0],sharex=ax2)
    plt.setp(ax1.get_xticklabels(), visible=False)
    name1 = folder1  + f1
    name2 = folder2  + f2
    s1 = spectrum.Spectrum(name1)
    s1.load('vna','txt')
    s1.power = s1.power - ispec.power - tspec.power
    s2 = spectrum.Spectrum(name2)
    s2.load('vna','txt')
    s2.power = s2.power - ispec.power - tspec.power
    ax1.plot(s1.freq,s1.power,label='no ESD protection')
    ax1.plot(s2.freq,s2.power,label='with ESD protection')
    ax2.plot(s1.freq,s1.power-s2.power)
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
