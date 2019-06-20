import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 6*np.pi, 1000)
sbase = [np.sin(n*x) for n in range (1, 11)]
cbase = [np.cos(n*x) for n in range (1, 11)]
f1 = sum(sbase[n-1]/n for n in range (1, 11))
f2 = sum(sbase[n-1]/n for n in range(1, 11, 2))

'''
f1 and f2 are partial sums of Fourier series. 
S = trivial_term+\sum^10 1/n*(2*pi*n*x/omega), 
where omega=2*pi, n is in {1,2,...,10} or {1,3,...,9}, 1/n is Fourier coefficient.
Periodicities are 2*pi.
'''

fig, ax = plt.subplots(figsize=(6,6))
ax.plot(x, f1) # Blue wave
ax.plot(x, f2) # Orange wave
fig.savefig('fourier.png', format='png')

