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
			print(y)
			print(x)
			if x == 1:
				sense.set_pixel(xVal+activeBlock_x,yVal+activeBlock_y,(255,255,255))
		
sense.clear()
generateBlock()
drawActiveBlock()

