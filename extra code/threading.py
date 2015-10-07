if __name__ == "__main__":
	import numpy as np
	import threading
	import time
	window = []
	fft = [None]
	freqs = np.fft.fftfreq(500, d=0.004)
	sample_ready = threading.Event()
	fft_ready = threading.Event()
	file_done = threading.Event()
	
	
def reader(w):
	with open('/path/openBCI_2013-12-24_relaxation.txt') as f:
		header = f.readline()
		line = f.readline()
		while line:
			sample = line.replace('\n','')
			sample = sample.split(', ')
			sample = sample[1:]
			sample = [float(item) for item in sample]
			if len(w) < 500:
				w.append(sample)
			else:
				for i in range(499):
					w[i] = w[i+1]
				w[499] = sample
				sample_ready.set()
				
			time.sleep(0.004)
			sample_ready.clear()
			line = f.readline()
			
		f.close()
		file_done.set()
		
def reader(w):
	
		
		
def transformer(w,f):
	while not file_done.is_set():
		sample_ready.wait()
		fft_ready.clear()
		#for channel in range(8):
		for channel in range(1):
			signal = np.array([row[channel] for row in w], dtype=float)
			fourier = np.fft.fft(signal)
			f[0] = fourier
			fft_ready.set()
		
			
def displayer(f):
	if file_done.is_set():
		print "Done reading file"
		return
		
	threading.Timer(1,displayer,args=(f,)).start()
	fft_ready.wait()
	#print only the first ten bands
	print f[0][:10]
	
		
if __name__ == "__main__":
	r = threading.Thread(target=reader, args=(window,))
	t = threading.Thread(target=transformer, args=(window,fft))
	r.start()
	t.start()
	displayer(fft)