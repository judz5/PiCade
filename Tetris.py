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
		[1,1,1,1,1,1,1,1]]


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
				
def checkCollisionY(dx,dy):
	for y in range(0,len(blockData[activeBlock][activeBlock_dir])):
		for x in range(0,len(blockData[activeBlock][activeBlock_dir][0])):
			if blockData[activeBlock][activeBlock_dir][y][x] != 0:
				if y+dy > len(field)-1:
					# below field
					return True
				elif field[y+dy][x+dx] != 0:
					# space is taken
					return True
				
def checkCollisionX(dx,dy):
	for y in range(0,len(blockData[activeBlock][activeBlock_dir])):
		for x in range(0,len(blockData[activeBlock][activeBlock_dir][0])):
			if blockData[activeBlock][activeBlock_dir][y][x] != 0:
				if x + dx < 0:
					# to the left
					return True
				if x + dx > len(field[0])-1:
					# to the right
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
	print(activeBlock_dir)
	if activeBlock_dir < 3:
		activeBlock_dir += 1
	elif activeBlock_dir >= 3:
		activeBlock == 0


generateBlock()
print(blockData[activeBlock][activeBlock_dir])

while True:
	
	ct = time.time()
	dt = ct - lft
	lft = ct
	timeCounter += dt
	
	events = sense.stick.get_events()
	if events:
		for e in events:
			if e.direction == "right" and e.action == "pressed": # add check coll
				if not checkCollisionX(activeBlock+2, activeBlock_y):
					activeBlock_x += 1
				
			if e.direction == "left" and e.action == "pressed": # Add check Coll
				if not checkCollisionX(activeBlock_x, activeBlock_y):
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
		bottom = activeBlock_y + len(blockData[activeBlock][activeBlock_dir])
		
		if not checkCollisionY(activeBlock_x+1,activeBlock_y+1):
			activeBlock_y+=1
		else:
			lockBlock(blockData[activeBlock][activeBlock_dir])
			generateBlock()
		
		sense.clear()
		drawField()
		drawActiveBlock()
		
			
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
