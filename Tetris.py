from sense_emu import *
import time
from random import randint

sense = SenseHat()
sense.clear()

MATRIX_MAX = 7
MATRIX_MIN = 0

gameSpeed = 1.0
timeCounter = 0.0
lft = 0.0
interval = gameSpeed

gameOver = False
###

square = {
    0: [[1,1],
		[1,1]],
	1: [[1,1],
		[1,1]],
	2: [[1,1],
		[1,1]],
	3: [[1,1],
		[1,1]],
    
}

lBlock = {
    0: [[1,0],
		[1,1]],
	1: [[0,1],
		[1,1]],
	2: [[1,1],
		[0,1]],
	3: [[1,1],
		[1,0]],
    
}

iBlock = {
    0: [[1],
		[1],
		[1]],
	1: [1,1,1],
	2: [[1],
		[1],
		[1]],
	3: [1,1,1],

    
}

zBlock = {
    0: [[1,0],
		[1,1],
		[0,1]],
	1: [[0,1,1],
		[1,1,0]],
	2: [[0,1],
		[1,1],
		[1,0]],
	3: [[1,1,0],
		[0,1,1]],
		
    
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

activeBlock_x = 2
activeBlock_y = -1
activeBlock = 2
activeBlock_dir = 1

def generateBlock():
	global activeBlock_x, activeBlock_y, activeBlock, activeBlock_dir
	temp = None
	activeBlock_x = 2
	activeBlock_y = -1
	activeBlock = randint(0,3)
	activeBlock_dir = randint(0,3)


def drawActiveBlock():
	yVal = -1
	xVal = 0
	
	if len(blockData[activeBlock][activeBlock_dir]) == 1:
		for x in blockData[activeBlock][activeBlock_dir]:
			xVal += 1
			sense.set_pixel(xVal + activeBlock_x, activeBlock_y,(255,255,255))
	else:
		for y in blockData[activeBlock][activeBlock_dir]:
			xVal = 0
			yVal += 1
			if y:
					for x in y:
						xVal += 1
						if x == 1:
							sense.set_pixel(xVal+activeBlock_x,yVal+activeBlock_y,(255,255,255))	
			else:
				sense.set_pixel(activeBlock_x,yVal+activeBlock_y,(255,255,255))


def addPixel(x,y):
	field[y][x] = 1

def drawField():
	for y in range(0,8):
		for x in range(0,8):
			if field[y][x] == 1:
				sense.set_pixel(x,y,(255,0,0))
				
def checkCollision(x,y):
	print("testing")
	
def rotateBlock():
	activeBlock_dir += 1

#generateBlock()
print(blockData[activeBlock][activeBlock_dir])

while True:
	
	ct = time.time()
	dt = ct - lft
	lft = ct
	timeCounter += dt
	
	events = sense.stick.get_events()
	if events:
		for e in events:
			if e.direction == "right" and activeBlock_x>0: # add check coll
				activeBlock_x += 1
				
			if e.direction == "left" and activeBlock_x<7: # Add check Coll
				activeBlock_x -= 1
			
	if timeCounter > interval:
		timeCounter = 0
		if not gameOver:
			activeBlock_y += 1
		
		sense.clear()
		drawField()
		drawActiveBlock()
		
			
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
