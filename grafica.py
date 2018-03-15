import numpy as np
import matplotlib.pyplot as plt

datos=np.loadtxt("fecha_manchas.dat")

annos= datos[:,0]
manchas=datos[:,1]

plt.figure()
plt.plot(annos, manchas)
plt.savefig("fecha_manchas.pdf")
