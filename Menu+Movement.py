from pickle import FALSE
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

#checks if the menu needs to pop-up
menuTime = True

#is the mouse inside a button?
mouseOnButton = False

#Run!
run = True

#Function to draw balloon
def add_balloon_at_location(balx,baly):
	win.blit(character, (balx,baly))
	

class menuButton(pygame.sprite.Sprite):
	
	def __init__(self, buttonX, buttonY, buttonWidth, buttonHeight, buttonText, screen):
		super().__init__()
		self.canvas = screen
		self.buttonX = buttonX
		self.buttonY = buttonY
		self.buttonWidth = buttonWidth
		self.buttonHeight = buttonHeight
		self.buttonText = buttonText
		
		self.color = (70,70,200)
		self.rect = pygame.Rect(self.buttonX, self.buttonY, self.buttonWidth, self.buttonHeight)
		
		self.textColor = (180, 240, 255)
		self.font = pygame.font.SysFont('Arial', 25)

		self.transition_duration = 30
		self.transition_timer = 0
		self.target_color = (70,70,200)
		
	def draw(self):
		pygame.draw.rect(self.canvas, self.color, self.rect)
		self.draw_centered_text()
	
	def draw_centered_text(self):
		self.text_surface = self.font.render(self.buttonText, True, self.textColor)
		self.text_rect = self.text_surface.get_rect()

		rect_center = self.rect.center

		self.text_x = rect_center[0] - self.text_rect.width / 2
		self.text_y = rect_center[1] - self.text_rect.height / 2

		self.text_rect.topleft = (self.text_x, self.text_y)

		self.canvas.blit(self.text_surface, self.text_rect)
		


class mouse(pygame.sprite.Sprite):
	def __init__(self, width, height, screen):
		super().__init__()
		self.canvas = screen
		self.hbWidth = width
		self.hbHeight = height
		
		self.rect = pygame.Rect(0, 0, self.hbWidth, self.hbHeight)
	
	def update(self):
		self.rect.topleft = pygame.mouse.get_pos()
	
startButton = menuButton(screen_width*0.1, (screen_height/2)-50, 200, 100, "Start", win)
endButton = menuButton((screen_width*0.9)-200, (screen_height/2)-50, 200, 100, "End", win)
theMouse = mouse(1, 1, win)

#Runs the code as long as the game is running
while run:
	
	for event in pygame.event.get(): 
		if event.type == pygame.QUIT: 
			run = False
	
	#All the Main Menu Stuff happens here
	if menuTime:
		win.fill((32, 32, 32))
		
		#Draw a hitbox around the mouse
		theMouse.update()
			
		# Check for collision
		if startButton.rect.colliderect(theMouse.rect):
			print ("hello")
		
		# Draw button
		startButton.draw()
		
		endButton.draw()
	
	#If the player chooses start then:
	else:
		balloon_col = pygame.Rect(balx, baly, 37, 49)
		plat1_col = pygame.Rect(plat1x, plat1y, width, height)
		plat2_col = pygame.Rect(plat2x, plat2y, width, height)
		basketL_col = pygame.Rect(left_box_x, box_y + box_height * 0.9, box_width, box_height)
		basketR_col = pygame.Rect(right_box_x, box_y + box_height * 0.9, box_width, box_height)
		
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