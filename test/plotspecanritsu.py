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
folder='/Users/romain/work/Auger/EASIER/data/20161012/'
#files = ['spec0sf.spa', 'spec1sf.spa', 'spec2sf.spa', 'spec3sf.spa', 'spec0af.spa', 'spec1af.spa', 'spec2af.spa', 'spec3af.spa']
#leg = ['0 no filter','1 no filter','2 no filter','3 no filter','0 with filter','1 with filter','2 with filter', '3 with filter']
#files = ['f1sf_#1.spa', 'f1af_#1.spa','avide.spa']
#leg = ['1 no filter','1 with filter','no input']
#files = ['g1af.spa', 'g1af_#1.spa','g1af_#2.spa','g1af_#3.spa','g1af_#4.spa']
#leg = ['-100dBm','-50dBm','-30dBm','-20dBm','-10dBm']
files = ['g1sf.spa', 'g1sf_#1.spa','g1sf_#2.spa']
leg = ['-100dBm','-80dBm','-50dBm']
for f,legend in zip(files,leg):
    name = folder  + f
    s = spectrum.Spectrum(name)
    s.load('sa')
    ax.plot(s.freq/1000,s.power,label=legend)
#    ax.plot(s.freq[s.freq < 1.5],s.power[s.freq < 1.5],label=legend)
    
plt.xlabel('frequency [GHz]')
#plt.ylabel('gain - 50 [dB]')
plt.ylabel('power [dBm/100kHz]')
plt.ylim(-110,-20)
plt.legend(loc=1)
plt.show()
