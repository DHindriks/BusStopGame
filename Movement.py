from turtle import Screen
import pygame 

pygame.init() 

screen_width = 800
screen_height = 600
win = pygame.display.set_mode((screen_width, screen_height)) 

pygame.display.set_caption("Moving rectangle") 

balx = 200
baly = 200

width = 200
height = 20

vel = 1
gravity = 0.3

platx = 100
platy = 100

character = pygame.image.load('balloon.png')

balloon_col = pygame.Rect(balx, baly, 47, 53)
platform_col = pygame.Rect(platx, platy, width, height)

run = True

def add_character_at_location(balx,baly):
	win.blit(character, (balx,baly))

while run: 
	pygame.time.delay(10)
	
	for event in pygame.event.get(): 
		if event.type == pygame.QUIT: 
			run = False

	keys = pygame.key.get_pressed() 

	if keys[pygame.K_LEFT] and platx>0: 
		platx -= vel 
		
	if keys[pygame.K_RIGHT] and platx<screen_width-width: 
		platx += vel 
		
	if keys[pygame.K_UP] and platy>0: 
		platy -= vel 

	if keys[pygame.K_DOWN] and platy<screen_height-height: 
		platy += vel 
	
	if baly<screen_height-height: 
		baly += gravity

	win.fill((0, 0, 0)) 
	
	pygame.draw.rect(win, (255, 0, 0), (platx, platy, width, height))
	pygame.draw.rect(win, (255, 0, 0), (balx, baly, 47, 53))
	
	add_character_at_location(balx, baly)

	pygame.display.update()

	if balloon_col.colliderect(platform_col):
		gravity = 0
		

pygame.quit() 