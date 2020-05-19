import numpy as np
import matplotlib.pyplot as plt
import time

def add(n):
    m=len(n)
    t=0
    for i in range(m):
        t=t+n[i]
    return t
def DFT_f(num):
    n=len(num)
    f = np.zeros(n, dtype = complex)
    for q in range(n):
        S = np.zeros(n, dtype = complex)
        for p in range(n):
            S[p] = num[p]*np.exp(-1j*(2*np.pi*q/n)*p)/np.sqrt(n)
        f[q]=add(S)
    return f
Time_DFT_f = np.zeros(100)
for i in range(4,100):
    num = np.arange(i)
    start = time.time()

    U = DFT_f(num)
    Time_DFT_f[i] = time.time() - start
#print(Time_DFT_f)

        
Time_numpy = np.zeros(100)
for i in range(4,100):
    num = np.arange(i)
    start = time.time()

    U = np.fft.fft(num)
    Time_numpy[i] = time.time() - start
#print(Time_numpy)
x = np.arange(0,100,1)

plt.plot(x,Time_DFT_f,'red' , label = "From DFT_f")
plt.plot(x,Time_numpy,'g--', label = "From Numpy")
plt.xlabel("num points")
plt.ylabel("Time taken in sec")
plt.legend()
plt.show()

  




        
            
        



        
    

