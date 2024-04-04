import pygame
import random
import json

def GenerateQuestion() :
	JsonFile = open('Questions.json')
	JsonData = json.load(JsonFile)
	CurrentQuestion = JsonData['Questions'][random.randrange(0, len(JsonData['Questions']))]
	print(CurrentQuestion)
	JsonFile.close()


pygame.init() 


GenerateQuestion()


screen_width = 800
screen_height = 600
win = pygame.display.set_mode((screen_width, screen_height)) 

pygame.display.set_caption("Moving rectangle") 

balx = screen_width/2
baly = screen_height/2

width = 100
height = 20

vel = 1
gravity = 1

plat1x = 100
plat1y = screen_height-100

plat2x = 500
plat2y = screen_height-100

character = pygame.image.load('balloon.png')

bouncey = 1
bouncex = 0

run = True

def add_character_at_location(balx,baly):
	win.blit(character, (balx,baly))

while run: 
	pygame.time.delay(10)
	
	balloon_col = pygame.Rect(balx, baly, 37, 49)
	plat1_col = pygame.Rect(plat1x, plat1y, width, height)
	plat2_col = pygame.Rect(plat2x, plat2y, width, height)

	for event in pygame.event.get(): 
		if event.type == pygame.QUIT: 
			run = False

	keys = pygame.key.get_pressed() 

	if keys[pygame.K_LEFT] and plat1x>0: 
		plat1x -= vel 
	if keys[pygame.K_RIGHT] and plat1x<screen_width-width: 
		plat1x += vel 
	if keys[pygame.K_UP] and plat1y>0: 
		plat1y -= vel 
	if keys[pygame.K_DOWN] and plat1y<screen_height-height: 
		plat1y += vel
		
	if keys[pygame.K_a] and plat2x>0: 
		plat2x -= vel 
	if keys[pygame.K_d] and plat2x<screen_width-width: 
		plat2x += vel 
	if keys[pygame.K_w] and plat2y>0: 
		plat2y -= vel 
	if keys[pygame.K_s] and plat2y<screen_height-height: 
		plat2y += vel

	if balx<0: 
		balx = 0
	if balx > screen_width-37:
		balx = screen_width-37

	if baly<screen_height-height: 
		baly += gravity

	win.fill((0, 0, 0)) 
	
	pygame.draw.rect(win, (0, 0, 255), (plat1x, plat1y, width, height))
	pygame.draw.rect(win, (0, 255, 0), (plat2x, plat2y, width, height))
	#pygame.draw.rect(win, (255, 0, 0), (balx, baly, 37, 49))
	
	
	if balloon_col.colliderect(plat1_col):
		bouncey = 5
		bouncex = random.uniform(-2, 5)
		print(bouncex)
		
	if balloon_col.colliderect(plat2_col):
		bouncey = 5
		bouncex = random.uniform(-5, 2)
		print(bouncex)
	
	if bouncey > vel:
		baly -= vel * bouncey
		balx += vel * bouncex
		bouncey -= 0.05

	add_character_at_location(balx, baly)

	pygame.display.update()

pygame.quit() 