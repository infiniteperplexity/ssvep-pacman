if __name__ == "__main__":
	import numpy as np
	import threading
	import time
	import matplotlib.pyplot as plt

	N = 500 #length of rolling window
	T = 1.0/250.0 #time between samples
	window = []
	low_cut = 5.0
	freqs = np.fft.fftfreq(N, d=T)[:(N/2)]
	for n,v in enumerate(freqs):
		if v >= low_cut:
			low_cut = n
			break
		
	hann = np.hanning(N)
	plt.ion()
	figure = plt.figure()
	plt.xlim(5,120)
	plt.ylim(-500,500)
	graph, = plt.plot([], [])
	f = open('C:/Users/Glenn/Documents/GitHub/NGHack-Pacman/glenn/live_raw.txt')
	header = f.readline()
	line = f.readline()
	while line:
		sample = line.replace('[','')
		sample = sample.replace(']','')
		sample = sample.replace("'",'')
		sample = sample.replace('\n','')
		sample = sample.split(', ')
		
		sample = [float(item) for item in sample]
		if len(window) < N:
			window.append(sample)
		else:
			for i in range(N-1):
				window[i] = window[i+1]
			window[N-1] = sample
			signal = np.array([row[0] for row in window], dtype=float)
			fft = abs(np.fft.fft(signal*hann))[:(N/2)]			
			graph.set_data(freqs[low_cut:],fft[low_cut:])
			time.sleep(0.004)
			plt.draw()
			
		line = f.readline()
	f.close()