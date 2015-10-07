if __name__ == "__main__":
	import numpy as np
	N = 250 #length of rolling window
	T = 1.0/250.0 #time between samples
	window = []
	chans = 8
	
	name = 'alpha'
		
	hann = np.hanning(N)
	f = open('C:/Users/Glenn/Documents/GitHub/NGHack-Pacman/glenn/' + name + '.txt')
	op = open('C:/Users/Glenn/Documents/GitHub/NGHack-Pacman/glenn/' + name + '_fft.txt','wb')
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
			op.write('[')
			for channel in range(chans):
				signal = np.array([row[channel] for row in window], dtype=float)
				fft = np.absolute(np.fft.fft(signal*np.hanning(N)))[:(N/2)].tolist()	
				#fft = abs(np.fft.fft(signal*np.hanning(N)))[:(N/2)].tolist()		
				op.write(str(fft))
				if channel < chans-1:
					op.write(',')
			op.write(']\n')
			
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
		
	with open('C:/Users/Glenn/Documents/GitHub/NGHack-Pacman/glenn/'+name+'_fft.txt') as f:
		print "reading lines from file..."
		lines = f.readlines()
		n = -1
			
		for line in lines:
			n+=1
			if n < 2500:
				continue
			if n > 17500:
				break
				
			channels = line.split('[')[2:]
			for i, channel in enumerate(channels):
				freqs = channel.replace(']','')
				freqs = freqs.replace("'",'')
				freqs = freqs.split(', ')
				for j, freq in enumerate(freqs):
					if j >= N/2:
						break
					freq = freq.replace(',','')
					readings[i][j].append(float(freq))
		
			
	print "calculating averages..."		
	sums = []
	for i in range(8):
		s = []
		for j in range(N/2):
			average = sum(readings[i][j])/float(len(readings[i][j]))
			s.append(average)
		sums.append(s)	
		
	print "exporting data..."
	with open('C:/Users/Glenn/Documents/GitHub/NGHack-Pacman/glenn/'+name+'_freqs.csv','wb') as f:
		import csv
		writer = csv.writer(f)
		writer.writerow(bands)
		for channel in sums:
			writer.writerow(channel)
			
	print "done."
	

