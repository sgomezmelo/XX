import numpy as np
import matplotlib.pyplot as plt

datos = np.loadtxt('fechas_manchas.dat')

plt.figure()
plt.plot(datos[:,0],datos[:,1])
plt.savefig('manchas.pdf')
