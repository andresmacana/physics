#varias graficas usando data from NIST y latex!

import numpy as np
import pylab as pl
from matplotlib import rc
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
## for Palatino and other serif fonts use:
#rc('font',**{'family':'serif','serif':['Palatino']})
rc('text', usetex=True)
import matplotlib.pyplot as plt

#data = np.loadtxt('electron_stp-power.txt',skiprows=3)
data = np.loadtxt('Silicon_stp_power_Protons.txt',skiprows=8)

#varias graficas
plt.figure(1)
#columna 1 y 2
plt.subplot(221)
plt.plot(data[:,0],data[:,1],'b-')
plt.xscale('log')
plt.yscale('log')
plt.xlabel(r'\textit{Energy} (MeV)')
plt.ylabel(r'\textit{Stopping Power}(MeV cm^2/g)')
plt.title(r'Electron Stopping Power')

#columna 1 y 3
plt.subplot(222)
plt.plot(data[:,0],data[:,2],'b-')
plt.xscale('log')
plt.yscale('log')
plt.xlabel(r'\textit{Energy} (MeV)')
plt.ylabel(r'\textit{Stopping Power}(MeV cm^2/g)')
plt.title(r'Nuclear Stopping Power')

#columna 1 y 4
plt.subplot(223)
plt.plot(data[:,0],data[:,3],'b-')
plt.xscale('log')
plt.yscale('log')
plt.xlabel(r'\textit{Energy} (MeV)')
plt.ylabel(r'\textit{Stopping Power}(MeV cm^2/g)')
plt.title(r'Total Stopping Power')

pl.show()
