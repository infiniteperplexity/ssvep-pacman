"""
if True:
	import sys
	sys.path.insert(0,'C:/Users/Glenn/Documents/GitHub/NGHack-Pacman/glenn')
	import main1
	main1.go()
	##cd C:\Python27\
	##python -m serial.tools.list_ports
"""
if True:
	import sys
	sys.path.insert(0,'C:/Users/Glenn/Documents/GitHub/NGHack-Pacman/glenn')
	import pygame, open_bci_v3 as bci
	board = bci.OpenBCIBoard()
	board.print_register_settings()
	f =  open('C:/Users/Glenn/Documents/GitHub/NGHack-Pacman/glenn/live_raw.txt','w')
	n = 0
	
	def handle_sample(sample):
		global n, f
		if n>=20000:
			return
			
		raw = []
		for channel in range(8):
			signal = sample.channel_data[channel]
			raw.append(signal)
			
		f.write(str(raw))
		f.write('\n')
		n+=1
		if n>=20000:
			f.close()
			print "finished for now"
		
	board.start_streaming(handle_sample)