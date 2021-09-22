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
    0: [[1,0],
		[1,0],
		[1,0]],
	1: [[0,0,0],
		[1,1,1]],
	2: [[0,1],
		[0,1],
		[0,1]],
	3: [[0,0,0],
		[1,1,1]],

    
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

field =[[1,1,1,1,1,1,1,1,1,1],
		[1,0,0,0,0,0,0,0,0,1],
		[1,0,0,0,0,0,0,0,0,1],
		[1,0,0,0,0,0,0,0,0,1],
		[1,0,0,0,0,0,0,0,0,1],
		[1,0,0,0,0,0,0,0,0,1],
		[1,0,0,0,0,0,0,0,0,1],
		[1,0,0,0,0,0,0,0,0,1],
		[1,0,0,0,1,1,1,0,0,1],
		[1,1,1,1,1,1,1,1,1,1]]

activeBlock_x = None
activeBlock_y = None
activeBlock = None
activeBlock_dir = None

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
	for y in blockData[activeBlock][activeBlock_dir]:
		xVal = 0
		yVal += 1
		for x in y:
			xVal += 1
			if x != 0:
				sense.set_pixel(xVal + activeBlock_x, yVal + activeBlock_y,(255,255,255))

def addPixel(x,y):
	field[y][x] = 1

def drawField():
	for y in range(1,9):
		for x in range(1,9):
			if field[y][x] != 0:
				sense.set_pixel(x-1,y-1,(255,0,0))
				
def checkCollision(dx,dy):
	for y in range(dy, len(blockData[activeBlock][activeBlock_dir])):
		for x in range(dx, len(blockData[activeBlock][activeBlock_dir][0])):
			if field[y][x] != 0:
				print "boomshakalaka"
				return False
	
	return True
	
def rotateBlock():
	global activeBlock_dir
	print(activeBlock_dir)
	if activeBlock_dir < 3:
		activeBlock_dir += 1
	elif activeBlock_dir >= 3:
		activeBlock == 0


generateBlock()
print(blockData[activeBlock][activeBlock_dir])
print(activeBlock_dir)

while True:
	
	ct = time.time()
	dt = ct - lft
	lft = ct
	timeCounter += dt
	
	events = sense.stick.get_events()
	if events:
		for e in events:
			if e.direction == "right" and e.action == "pressed": # add check coll
				if not checkCollision(activeBlock_x+len(blockData[activeBlock][activeBlock_dir])):
					activeBlock_x += 1
				
			if e.direction == "left" and e.action == "pressed": # Add check Coll
				if not checkCollision(activeBlock_x-1, activeBlock_y):
					activeBlock_x -= 1
				
			if e.direction == "up" and e.action == "pressed":
				rotateBlock()
			
	if timeCounter > interval:
		timeCounter = 0
		if not checkCollision(activeBlock_x+1,activeBlock_y+1):
			activeBlock_y += 1
		
		sense.clear()
		drawField()
		drawActiveBlock()
		
			
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
