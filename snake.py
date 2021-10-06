from sense_emu import *
import time
import random  
sense = SenseHat()
sense.low_light = False


gameRunning = True
MATRIX_MIN_VALUE = 0
MATRIX_MAX_VALUE = 7
MATRIX_SIZE = 8
score = 0
posX = [3]
posY = [6]


foodPosX = random.randint(0,7)
foodPosY = random.randint(0,7)

movX = 0
movY = -1

sense.show_message("3 2 1")

def growSnake():
	posX.append(0)
	posY.append(0)

while gameRunning:
		
	if posX[0] == foodPosX and posY[0] == foodPosY:
		score+=1
		growSnake()
		retry = True
		while retry:
			foodPosX = random.randint(0,7)
			foodPosY = random.randint(0,7)
			retry = False
			for x, y in zip(posX, posY):
				if x == foodPosX and y == foodPosY:
					retry = True
					break
	
	for i in range(1, len(posX)):
		if posX[i] == posX[0] and posY[i] == posY[0]:
			print("game over")
			gameRunning = False
			
	if not gameRunning:
		break
	
	events = sense.stick.get_events()
	for event in events:
		if event.direction == "left" and movX != 1:
			movX = -1
			movY = 0
		elif event.direction == "right" and movX != -1:
			movX = 1
			movY = 0
		elif event.direction == "up" and movY != 1:
			movX = 0
			movY = -1
		elif event.direction == "down" and movY != -1:
			movX = 0
			movY = 1
			
	for i in range((len(posX) - 1),0, -1):
		posX[i] = posX[i-1]
		posY[i] = posY[i-1]
	
	posX[0] += movX
	posY[0] += movY
	
	if posX[0] > MATRIX_MAX_VALUE:
		posX[0] -= MATRIX_SIZE
	elif posX[0] < MATRIX_MIN_VALUE:
		posX[0] += MATRIX_SIZE
	if posY[0] > MATRIX_MAX_VALUE:
		posY[0] -= MATRIX_SIZE
	elif posY[0] < MATRIX_MIN_VALUE:
		posY[0] += MATRIX_SIZE
			
	sense.clear()
	sense.set_pixel(foodPosX, foodPosY,(255,0,0))
	for x, y in zip(posX, posY):
		sense.set_pixel(x,y,(0,255,0))
		
	time.sleep(0.2)

if not gameRunning:
	show = "Score: "
	sense.show_message(show + str(score))
	





