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

#name = sys.argv[1]
fig = plt.figure(figsize=(8,6))
ax = plt.subplot(111)
folder='/Users/romain/Dropbox/Public/EASIER/malargue2016/lab/spectrum/'
files = ['s11_fpv01_#1.csv','s11_fpv02.csv','s11_fpv03.csv','s11_fpv04.csv','s11_fpv05.csv','s11_fpv07.csv','s11_fpv08.csv']
leg = ['fpv01','fpv02','fpv03','fpv04','fpv05','fpv07','fpv08']
for f,legend in zip(files,leg):
    name = folder  + f
    s = spectrum.Spectrum(name)
    s.load('s11')
    ax.plot(s.freq[s.freq < 1.5],s.power[s.freq < 1.5],label=legend)
    
plt.xlabel('frequency [GHz]')
#plt.ylabel('gain - 50 [dB]')
plt.ylabel('vswr')
plt.ylim(0.5,6)
plt.legend(loc=1)
plt.show()
