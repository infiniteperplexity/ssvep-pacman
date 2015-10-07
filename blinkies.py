if __name__ == "__main__":
	import pygame, sys
	from pygame.locals import *
	pygame.init()
	HEIGHT = 750
	WIDTH = 1000
	UNIT = 25
	screen = pygame.display.set_mode((WIDTH,HEIGHT))
	BLACK = (  0,   0,   0)
	WHITE = (255, 255, 255)
	BLUE =  (  0,   0, 255)
	GREEN = (  0, 255,   0)
	RED =   (255,   0,   0)

	class Arrow():
		def __init__(self, x, y):
			self.state = 0
			self.x = x
			self.y = y
			pygame.draw.rect(screen,RED,[self.x,self.y,UNIT,UNIT])
			pygame.draw.rect(screen,WHITE,[self.x+UNIT,self.y,UNIT,UNIT])
			pygame.draw.rect(screen,WHITE,[self.x,self.y+UNIT,UNIT,UNIT])
			pygame.draw.rect(screen,RED,[self.x+UNIT,self.y+UNIT,UNIT,UNIT])
			
		def toggle(self):
			if self.state == 0:
				pygame.draw.rect(screen,WHITE,[self.x,self.y,UNIT,UNIT])
				pygame.draw.rect(screen,RED,[self.x+UNIT,self.y,UNIT,UNIT])
				pygame.draw.rect(screen,RED,[self.x,self.y+UNIT,UNIT,UNIT])
				pygame.draw.rect(screen,WHITE,[self.x+UNIT,self.y+UNIT,UNIT,UNIT])
				self.state = 1
			else:
				pygame.draw.rect(screen,RED,[self.x,self.y,UNIT,UNIT])
				pygame.draw.rect(screen,WHITE,[self.x+UNIT,self.y,UNIT,UNIT])
				pygame.draw.rect(screen,WHITE,[self.x,self.y+UNIT,UNIT,UNIT])
				pygame.draw.rect(screen,RED,[self.x+UNIT,self.y+UNIT,UNIT,UNIT])
				self.state = 0
		
		
	def go():
		counter = 0
		clock = pygame.time.Clock()
		while True:
			for event in pygame.event.get():
				if event.type == QUIT:
					pygame.quit()
					sys.exit()
					
			counter = counter + 1
			
			if counter%7==0: #8 fps
				left.toggle()
			if counter%5==0: #12 fps
				up.toggle()
			if counter%4==0: #15 fps
				right.toggle()
			if counter%3==0: #20 fps
				down.toggle()
			
			clock.tick(60)
			pygame.display.flip()
		 
	left = Arrow(UNIT,HEIGHT/2 - UNIT)
	up = Arrow(WIDTH/2 - UNIT, UNIT)
	right = Arrow(WIDTH - 3*UNIT, HEIGHT/2 - UNIT)
	down = Arrow(WIDTH/2 - UNIT, HEIGHT - 3*UNIT)
	go()