from sense_emu import *
import time
from random import randint

sense = SenseHat()
sense.clear()

MATRIX_MAX = 7
MATRIX_MIN = 0

gameSpeed = 0.75
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
	2: [[1,0],
		[1,1],
		[0,1]],
	3: [[0,1,1],
		[1,1,0]],
		
    
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
	print "GENERATIN' BLOCK"
	temp = None
	activeBlock_x = 2
	activeBlock_y = -1
	activeBlock = randint(0,3)
	activeBlock_dir = randint(0,3)


def drawActiveBlock():
	print "DRAWIN' BLOCK"
	yVal = -1
	xVal = 0
	for y in blockData[activeBlock][activeBlock_dir]:
		xVal = 0
		yVal += 1
		for x in y:
			xVal += 1
			if x != 0:
				if yVal == 0 and activeBlock_y == -1:
					yVal += 1
					print yVal, activeBlock_y
				sense.set_pixel(xVal + activeBlock_x, yVal + activeBlock_y,(255,255,255))


def drawField():
	for y in range(0,8):
		for x in range(0,8):
			if field[y][x] != 0:
				sense.set_pixel(x,y,(255,0,0))
				
def checkCollision(dx,dy,block):
	for y in range(0,len(block)):
		for x in range(0,len(block[0])):
			if block[y][x] != 0:
				if x + dx < 0:
					# to the left
					print "left"
					return True
				if x + dx >= len(field[0]):
					# to the right
					print "right"
					return True
				if y+ dy >= len(field):
					return True
				if field[y+dy][x+dx] != 0:
					# space is taken
					return True
	
def lockBlock(block):
	print "LOCKIN' BLOCK"
	for y in range(0, len(block)):
		for x in range(0, len(block[0])):
			if block[y][x] != 0:
				field[y + activeBlock_y][x + activeBlock_x+1] = 1
			
	
def rotateBlock():
	global activeBlock_dir
	tmpDir = (activeBlock_dir + 1) % 4
	tmpBlock = blockData[activeBlock][tmpDir]
	if not checkCollision(activeBlock_x+1,activeBlock_y, tmpBlock):
		activeBlock_dir = (activeBlock_dir + 1) % 4

generateBlock()
print(blockData[activeBlock][activeBlock_dir])
curBlock = blockData[activeBlock][activeBlock_dir]

while True:
	
	ct = time.time()
	dt = ct - lft
	lft = ct
	timeCounter += dt
	
	events = sense.stick.get_events()
	if events:
		for e in events:
			if e.direction == "right" and e.action == "pressed": # add check coll
				if not checkCollision(activeBlock_x+2, activeBlock_y, curBlock):
					activeBlock_x += 1
				
			if e.direction == "left" and e.action == "pressed": # Add check Coll
				if not checkCollision(activeBlock_x, activeBlock_y, curBlock):
					activeBlock_x -= 1
				
			if e.direction == "up" and e.action == "pressed":
				rotateBlock()
				
			if e.direction == "down" and e.action == "pressed":
				print "Pog"
				interval = gameSpeed/5
				
			if e.direction == "down" and e.action == "pressed":
				interval = gameSpeed
			
	if timeCounter > interval:
		timeCounter = 0
		
		if not checkCollision(activeBlock_x+1,activeBlock_y+1, curBlock):
			activeBlock_y+=1
		else:
			lockBlock(blockData[activeBlock][activeBlock_dir])
			generateBlock()
			curBlock = blockData[activeBlock][activeBlock_dir]
		
		sense.clear()
		drawField()
		drawActiveBlock()
		
			
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
