import numpy as np
import matplotlib.pyplot as plt

def f(x):
    if (x!=0):
        return np.sin(x)/x
    else:
        return 1
def analytical(k):
    if((k>-1)and(k<1)):
        return np.sqrt(np.pi/2.0)
    else:
        return 0

xmin = -5.0
xmax = 5.0

n = 2**(5)

dx = (xmax - xmin)/(n - 1)
print(dx)

sampled_data = np.zeros(n)
x = np.zeros(n)

for i in range(n):
          sampled_data[i] = f(xmin+i*dx)
          x[i] = xmin + i*dx
#print(sampled_data)
print("x=",x)
#nft = (np.fft.fft(sampled_data, norm = 'ortho'))
#print(nft)

k = np.fft.fftfreq(n, dx)

#print('k=',k)
I = np.argsort(k)
k = k[I]
print("k=", k)
k = 2*np.pi*k
#print("k_new=", k)

nft = (np.fft.fft(sampled_data, norm = 'ortho'))
nft = nft[I]

factor = np.exp(-1j*k*xmin)
#print("factor=", factor)


ft = (abs((dx*np.sqrt(n/(2*np.pi))*factor*nft)))







plt.plot(k,ft , '.-', label = "numerical")

analytic_ft=np.zeros(len(k))
for i in range(len(k)):
    analytic_ft[i]=analytical(k[i])
plt.plot(k,analytic_ft, 'r--', label='Analytic' )
plt.xlabel("Frequency")
plt.ylabel("Fourier transform")
plt.grid()
plt.legend()
plt.show()
  



















