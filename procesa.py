import numpy as np
import matplotlib.pyplot as plt


datos=np.loadtxt("monthrg.dat")

manchas = datos[:,3]

annos= datos[:,0] + (datos [:,1]-1)/12.0

ii= annos>1900

los_datos = np.array([annos[ii], manchas[ii]])

np.savetxt("fecha_manchas.dat", los_datos.T )
