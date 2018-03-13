import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,(np.pi)/2)
seno=[]
for i in x:
    seno.append(np.sin(i))
    


plt.plot(x,seno)
plt.savefig("grafica.png")
