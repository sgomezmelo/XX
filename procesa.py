import numpy as np

datos = np.loadtxt('monthrg.dat')
t = []
manchas = []

for d in datos:
    if(d[0] > 1899):
        t.append(d[0] + (d[1]-1)/12.0)
        manchas.append(d[3])

salida = np.array([t,manchas])

np.savetxt('fechas_manchas.dat',salida.T)
