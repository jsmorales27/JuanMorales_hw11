import numpy as np 
import matplotlib.pylab as plt

data=np.loadtxt("tray.txt", dtype=float, delimiter=",")

plt.plot(data[:,2], data[:,0], label="Masa m (m<<M)", color="red")
plt.legend()
plt.grid()
plt.title("Movimiento de una masa en presencia de un campo \n que depende de (r)")
plt.xlabel("Tiempo (t)")
plt.ylabel("Posicion r (m)")
plt.savefig("pos.png")
plt.clf()

plt.plot(data[:,2], data[:,1], label="Masa m (m<<M)", color="red")
plt.legend()
plt.grid()
plt.title("Velocidad de una masa en presencia de un campo \n que depende de (r)")
plt.xlabel("Tiempo (t)")
plt.ylabel("Velocidad v (m)")
plt.savefig("vel.png")
plt.clf()

plt.plot(data[:,0], data[:,1], label="Masa m (m<<M)", color="red")
plt.legend()
plt.grid()
plt.title("Velocidad de una masa en funcion de \n su posicion (r)")
plt.xlabel("Posicion (r)")
plt.ylabel("Velocidad v (m)")
plt.savefig("phase.png")
plt.clf()
