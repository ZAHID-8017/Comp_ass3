from scipy import signal
import numpy as np
import matplotlib.pyplot as plt




text_file = np.loadtxt(fname = "noise.txt", dtype = float)


#x = np.linspace(0,512,512)
#print(x)
#print(text_file)

ft = np.fft.fft(text_file, norm = "ortho")
k = np.fft.fftfreq(512, d=1)
order = np.argsort(k)
k = k[order]
aft =  abs(ft[order])
################ "PLoting the DFT file" ###############################################
plt.figure()
plt.plot(k,aft, "red", label = "DFT_data")
plt.grid(True)
plt.xlabel('frequency')
plt.ylabel('DFT_data')
plt.legend()
################ "PLoting the text file" ###############################################
#plt.show()
fig = plt.figure()
plt.plot(text_file, "green", label = "text_file")
plt.grid(True)
plt.xlabel('index')
plt.ylabel('file_data')
plt.legend()
#plt.show()


spectra=abs(ft)*abs(ft)/(512)

################ "PLoting the power spectrum" ###############################################
fig = plt.figure()
plt.plot(k,spectra, label='Spectra')
plt.xlabel('frequency')
plt.ylabel('Power spectrum')
plt.legend()


################ "PLoting the Histogram"###############################################
bin=10
fig = plt.figure()
plt.hist(spectra,bin, facecolor='blue',label='binned power spectrum')
plt.legend()
plt.show()











