import pygame
import sys
import random
import json

pygame.init() 

#Screen properties
screen_width = 800
screen_height = 600
win = pygame.display.set_mode((screen_width, screen_height)) 

#Sets window title
pygame.display.set_caption("Moving rectangle") 

#Starting position of the ball
balx = screen_width/2
baly = screen_height/2

#Platform properties
width = 100
height = 20

#Gravity properties
vel = 1
gravity = 1

#Speed of the player platforms
platSpeed = 2

#Left platform starting position
plat1x = 100
plat1y = screen_height-100

#Right platform starting position
plat2x = 500
plat2y = screen_height-100

#Importing image(s)
character = pygame.image.load('balloon.png')

#Left/Right bouncing properties
bouncey = 1
bouncex = 0
xmemory = 0

#Answer basket properties
box_width = 100
box_height = 50
box_y = screen_height - box_height
left_box_x = 50 
right_box_x = screen_width - box_width - 50

#Run!
run = True

#Function to draw balloon
def add_balloon_at_location(balx,baly):
	win.blit(character, (balx,baly))

#Function to generate question
def GenerateQuestion() :
	JsonFile = open('Questions.json')
	JsonData = json.load(JsonFile)
	CurrentQuestion = JsonData['Questions'][random.randrange(0, len(JsonData['Questions']))]
	print(CurrentQuestion)
	JsonFile.close()

#Runs the code as long as the game is running
while run: 
	pygame.time.delay(10)
	
	GenerateQuestion()
	
	balloon_col = pygame.Rect(balx, baly, 37, 49)
	plat1_col = pygame.Rect(plat1x, plat1y, width, height)
	plat2_col = pygame.Rect(plat2x, plat2y, width, height)
	basketL_col = pygame.Rect(left_box_x, box_y + box_height * 0.9, box_width, box_height)
	basketR_col = pygame.Rect(right_box_x, box_y + box_height * 0.9, box_width, box_height)

	for event in pygame.event.get(): 
		if event.type == pygame.QUIT: 
			run = False

	keys = pygame.key.get_pressed() 

	#Movement for left platform
	if keys[pygame.K_a] and plat1x>0: 
		plat1x -= platSpeed
	if keys[pygame.K_d] and plat1x<screen_width-width: 
		plat1x += platSpeed
	if keys[pygame.K_w] and plat1y>0: 
		plat1y -= platSpeed 
	if keys[pygame.K_s] and plat1y<screen_height-height: 
		plat1y += platSpeed
	
	#Movement for right platform
	if keys[pygame.K_LEFT] and plat2x>0: 
		plat2x -= platSpeed
	if keys[pygame.K_RIGHT] and plat2x<screen_width-width: 
		plat2x += platSpeed 
	if keys[pygame.K_UP] and plat2y>0: 
		plat2y -= platSpeed 
	if keys[pygame.K_DOWN] and plat2y<screen_height-height: 
		plat2y += platSpeed

	#Makes balloon stay inside the screen
	if balx<0: 
		balx = 0
	if balx > screen_width-37:
		balx = screen_width-37

	if baly<screen_height-height: 
		baly += gravity

	#Clears the screen
	win.fill((0, 0, 0)) 
	
	#Draw the player platforms
	pygame.draw.rect(win, (0, 0, 255), (plat1x, plat1y, width, height))
	pygame.draw.rect(win, (0, 255, 0), (plat2x, plat2y, width, height))
	
	#Draw the Answer Boxes
	pygame.draw.rect(win, (255, 0, 0), (left_box_x, box_y, box_width, box_height))
	pygame.draw.rect(win, (255, 0, 0), (right_box_x, box_y, box_width, box_height))
	
	#Checks if the balloon hits the left platform
	if balloon_col.colliderect(plat1_col):
		bouncey = 5
		bouncex = random.uniform(0, 5)
		xmemory = bouncex
		print(bouncex)
	
	#Checks if the balloon hits the right platform
	if balloon_col.colliderect(plat2_col):
		bouncey = 5
		bouncex = random.uniform(-5, 0)
		xmemory = bouncex
		print(bouncex)
		
	#Checks if the balloon is inside the answer basket
	if balloon_col.colliderect(basketL_col):
		balx = screen_width/2
		baly = screen_height/2 
	
	#Gravity
	if bouncey > vel:
		baly -= vel * bouncey
		balx += vel * bouncex
		bouncey -= 0.05
	
	#Left/Right movement fall off
	if bouncex < 0:
		bouncex += xmemory * -0.01 
	elif bouncex > 0:
		bouncex += xmemory * -0.01

	#Draw the balloon
	balloon = add_balloon_at_location(balx, baly)
	
	#Updates the screen
	pygame.display.update()

pygame.quit() 