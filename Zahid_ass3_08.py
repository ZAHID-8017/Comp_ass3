from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
def f(x, y):
    return np.exp(-(x ** 2 + y ** 2)/2)


xmin = -20.0
xmax = 20.0
ymin = -20.0
ymax = 20.0


n = 2**(5)

dx = (xmax - xmin)/(n - 1)
dy = (ymax - ymin)/(n-1)

x=np.zeros(n)
y=np.zeros(n)
sampled_data = np.zeros((n,n))     
for i in range(n):
          y[i] = ymin + i*dy
          x[i] = xmin + i*dx

X,Y = np.meshgrid(x,y)
sampled_data = f(X,Y)

nft2 = (np.fft.fft2(sampled_data, norm = 'ortho'))
#print(nft)

kx = np.fft.fftfreq(n, dx)
ky = np.fft.fftfreq(n, dy)

#print('k=',k)


kx = 2*np.pi*kx
ky = 2*np.pi*ky                
#print("k_new=", k)

Kx,Ky = np.meshgrid(kx,ky)
factor = np.exp(-1j*(Kx*xmin+Ky*ymin))
#print("factor=", factor)


ft = (abs((dx*dy*(n/(2*np.pi))*factor*nft2)))







fig = plt.figure()
ax = plt.axes(projection='3d')
ax = plt.axes(projection='3d')
ax.plot_surface(Kx, Ky, ft, rstride=1, cstride=1,
                cmap='viridis', edgecolor='none')
ax.set_title('surface')
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_wireframe(Kx, Ky, ft, color='blue')
ax.set_title('wireframe')
plt.show()
  
