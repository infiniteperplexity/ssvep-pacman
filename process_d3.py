if __name__ == "__main__":
	import numpy as np
	N = 250 #length of rolling window
	T = 1.0/250.0 #time between samples
	window = []
	chans = 8
	
	name = 'alpha'
		
	hann = np.hanning(N)
	f = open('C:/Users/Glenn/Documents/GitHub/ssvep/master/' + name + '.txt')
	op = open('C:/Users/Glenn/Documents/GitHub/ssvep/master/' + name + '_fft.csv','wb')
	import csv
	w = csv.writer(op)
	header = f.readline()
	line = f.readline()
	while line:
		sample = line.replace('[','')
		sample = sample.replace(']','')
		sample = sample.replace("'",'')
		sample = sample.replace('/n','')
		sample = sample.split(', ')
		
		sample = [float(item) for item in sample]
		if len(window) < N:
			window.append(sample)
		else:
			for i in range(N-1):
				window[i] = window[i+1]
			window[N-1] = sample
			op.write('[')
			for channel in range(chans):
				signal = np.array([row[channel] for row in window], dtype=float)
				fft = np.absolute((np.fft.fft(signal*np.hanning(N)))[:(N/2)]/float(N)).tolist()	
				#fft = abs(np.fft.fft(signal*np.hanning(N)))[:(N/2)].tolist()		
				#op.write(str(fft))
				w.writerow(fft);
				#if channel < chans-1:
					#op.write(',')
			#op.write(']/n')
			
		line = f.readline()
	f.close()
	op.close()
	print "Done!"

	bands = np.fft.fftfreq(N, d=T)[:(N/2)]
	readings = []
	for i in range(8):
		channel = []
		for j in range(N/2):
			channel.append([])
		readings.append(channel)
	

