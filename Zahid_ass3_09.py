import numpy as np
import matplotlib.pyplot as plt

def f(t):
    if -1.0 < t < 1.0:
        return 1
    else:
        return 0

xmin = -5
xmax = 5
n = 2**8
dx = (xmax  - xmin)/(n - 1)
x  = np.zeros(n)
y = np.zeros(n)
#analytic_f = np.zeros(n)
for i in range(n):
    y[i] = f(xmin + i*dx)
    x[i] = xmin + i*dx
k = np.fft.fftfreq(n, dx) 
I = np.argsort(k)
k = k[I]
#print("k=", k)
k = 2*np.pi*k
#print("k_new=", k)
#y = f(x)
nft = (np.fft.fft(y, norm = 'ortho'))
Nft=nft*nft

f_c = abs(dx*np.sqrt(n)*np.fft.ifft(Nft, norm = "ortho"))

f_c = f_c[I]
plt.plot(x,f_c , '.-' ,label = "convolution plot")
plt.plot(x, y,'g--' ,label = "box function")
plt.grid(True)
plt.legend()    
plt.show()
  
