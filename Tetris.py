from sense_emu import *
import time
from random import randint

sense = SenseHat()
sense.clear()

MATRIX_MAX = 7
MATRIX_MIN = 0
GameSpeed = 0.5

###

square = {
    0: [[0,0,0],
		[1,1,0],
		[1,1,0]],
	1: [[0,0,0],
		[1,1,0],
		[1,1,0]],
	2: [[0,0,0],
		[1,1,0],
		[1,1,0]],
	3: [[0,0,0],
		[1,1,0],
		[1,1,0]],
    
}

lBlock = {
    0: [[0,0,0],
		[1,0,0],
		[1,1,0]],
	1: [[0,0,0],
		[0,1,0],
		[1,1,0]],
	2: [[0,0,0],
		[1,1,0],
		[0,1,0]],
	3: [[0,0,0],
		[1,1,0],
		[1,0,0]],
    
}

iBlock = {
    0: [[0,1,0],
		[0,1,0],
		[0,1,0]],
	1: [[0,0,0],
		[1,1,1],
		[0,0,0]],
	2: [[0,1,0],
		[0,1,0],
		[0,1,0]],
	3: [[0,0,0],
		[1,1,1],
		[0,0,0]],
    
}

zBlock = {
    0: [[1,0,0],
		[1,1,0],
		[0,1,0]],
	1: [[0,1,1],
		[1,1,0],
		[0,0,0]],
	2: [[0,0,1],
		[0,1,1],
		[0,1,0]],
	3: [[1,1,0],
		[0,1,1],
		[0,0,0]],
    
}

blockData = [square, lBlock, iBlock, zBlock]

####

field =[[0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0]]

activeBlock_x = None
activeBlock_y = None
activeBlock = None
activeBlock_dir = None

def generateBlock():
	global activeBlock_x, activeBlock_y, activeBlock, activeBlock_dir
	temp = None
	activeBlock_x = 2
	activeBlock_y = -1
	temp = randint(0,3)
	activeBlock_dir = randint(0,3)
	hold = None
	hold = blockData[temp]
	activeBlock = hold[activeBlock_dir]

def drawActiveBlock():
	yVal = 0
	xVal = 0
	for y in activeBlock:
		xVal = 0
		yVal += 1
		for x in y:
			xVal += 1
			if x == 1:
				sense.set_pixel(xVal+activeBlock_x,yVal+activeBlock_y,(255,255,255))

def addPixel(x,y):
	field[y][x] = 1

def drawField():
	for y in range(0,8):
		for x in range(0,8):
			sense.set_pixel(x,y,(255,255,255))

generateBlock()

while True:
	
	time.sleep(1)
	
	events = sense.stick.get_events()
	if events:
		for e in events:
			if e.direction == "right":
				activeBlock_x += 1
				
			if e.direction == "left":
				activeBlock_x -= 1
		
	activeBlock_y += 1
	
	sense.clear()
	drawActiveBlock()
	
			
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
