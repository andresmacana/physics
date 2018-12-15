from pylab import*
from numpy import*

f = arange(0,2.1,0.1)
Ef = 1.0
kT1 = (1/40.0)*Ef
kT2 = (1/10.0)*Ef
kT3 = (1/4.0)*Ef
fE1 = []
fE2 = []
fE3 = []
print ("%8s %8s %8s %8s"%("f(E)","E1","E2","E3"))
for value in f:
    fE1.append(1/((exp((value-Ef)/kT1))+1))
    fE2.append(1/((exp((value-Ef)/kT2))+1))
    fE3.append(1/((exp((value-Ef)/kT3))+1))
for i in range(len(f)):
    print ("%8.1f %8.3f %8.3f %8.3f"%(f[i],fE1[i],fE2[i],fE3[i]))

plot(f,fE1,f,fE2,f,fE3)
show()
