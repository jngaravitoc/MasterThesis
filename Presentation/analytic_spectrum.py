import numpy as np 
import matplotlib.pyplot as plt

tau = 1E6
T = 1E4
Delta_v = 128.5 * T**(1/2.) / 3E4
a = 1 / (8.0*np.pi * Delta_v) 
x = np.linspace(-100, 100, 100)

def slab(tau, x):
	J_slab = 1E3*( np.sqrt(6)/(24.*np.sqrt(np.pi)*a*tau)) * x**2 / (1 + np.cosh(np.sqrt(np.pi**3/54.)*abs(x**3)/(a*tau)))
	return J_slab
def sphere(tau, x):
	J_sphere = 1E3*np.sqrt(np.pi)/(np.sqrt(24.0)*a*tau) * x**2 / (1 + np.cosh(np.sqrt(2*np.pi**3 / 27.)*abs(x**3)/(a*tau)))	
	return J_sphere

J_slab = slab(1E6, x)
J_sphere = sphere(1E6, x)
plt.plot(x, J_slab, lw=5, label="Slab")
plt.plot(x, J_sphere, lw=5, label="Sphere")
plt.xlabel(r"$\rm{x}$",fontsize=25)
plt.ylabel(r"$10^3\rm{J(x)}$", fontsize=25)
plt.legend(fontsize=18)
plt.show()

J_slab5 = slab(1E5, x)
J_slab6 = slab(1E6, x)
J_slab7 = slab(1E7, x)

plt.plot(x, J_slab5, lw = 4, label = r"$\tau = 10^5$")
plt.plot(x, J_slab6, lw = 4, label = r"$\tau = 10^6$")
plt.plot(x, J_slab7, lw = 4, label = r"$\tau = 10^7$")
plt.legend(fontsize = 18)
plt.xlabel(r"$\rm{x}$",fontsize=25)
plt.ylabel(r"$10^3\rm{J(x)}$", fontsize=25)
plt.show()


