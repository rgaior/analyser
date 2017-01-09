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

name = sys.argv[1]
fig = plt.figure(figsize=(8,6))
ax = plt.subplot(111)
folder='/Users/romain/work/Auger/EASIER/data/analyser/transientsa/20160415/'
fnames = glob.glob(folder+name+'*txt')
if len(fnames) == 0:
    fnames = glob.glob(folder+name+'*TXT')
count = 0
for name in fnames:
    s = spectrum.Spectrum(name)
    s.loadinfo()
    s.load()
    leg = s.getinfo()
    ax.plot(s.freq[:-10]/1e9,s.power[:-10])
    if count == 0:
        count+=1
        a = ax.text(0.05, 0.85, leg,
                    verticalalignment='top', horizontalalignment='left',
                    transform=ax.transAxes,
                    color='black', fontsize=15)
        a.set_bbox(dict(color='white', alpha=1, edgecolor='black'))
    
plt.xlabel('frequency [GHz]')
plt.ylabel('power [dBm/RBW]')
plt.show()
