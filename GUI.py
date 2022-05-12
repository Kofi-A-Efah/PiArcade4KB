import RPi.GPIO as GPIO
import time
import subprocess
import os
import pygame

GPIO.setmode(GPIO.BCM)   # Set for broadcom numbering not board numbers...

## Pygame Setup
os.putenv('SDL_VIDEODRIVER', 'fbcon')
os.putenv('SDL_FBDEV', '/dev/fb1')
os.putenv('SDL_MOUSEDRV', 'TSLIB')
os.putenv('SDL_MOUSEDEV', '/dev/input/touchscreen')

pygame.init() 
pygame.mouse.set_visible(False)

#Screen
size = width, height = 320, 240 
speed1 = [2,2]
speed2 = [1,1] 
blue = (0,0,255)
black = 0,0,0
WHITE = 255,255,255
screen = pygame.display.set_mode(size)  
screen.fill(black)  # Erase the Work space 
pygame.display.flip()
my_font = pygame.font.Font(None,25)
center = (160, 220)
border_width = 0



#GUI Elements

title_rect = (70,35,180,25)
g1rect = (37,136,100,25)
g2rect = (200,136,100,25)

global home_screen
global g_one
global g_two
home_screen = {'Pi Arcade Stick 4KB':(160,50), "Game 1":(80,150), "Game 2":(240,150),"Quit":(260,220)}
g_one = {'Pac-Man':(160,50),'Quit':(260,220),'Back':(60,220)}
g_two = {'Guilty Gear +R':(160,20), 
'P':(80,170), 'K':(120,170), 'S':(160,170), 'HS':(200,170), 'D':(240,170), 'Quit':(260,220),'Back':(60,220)}
 


# Loop Control
global loop
loop = True 
stop = time.time() + 10

#Game Select
global level
level = 0 # Home Screen
#level = 1  Game 1
#level = 2  Game 2

#GUI OBJECTS
up = pygame.image.load("up.png")
up = pygame.transform.scale(up,(50,40))

uppress = pygame.image.load("uppress.png")
uppress = pygame.transform.scale(up,(50,40))

right = pygame.image.load("right.png")
right = pygame.transform.scale(up,(50,40))

rightpress = pygame.image.load("rightpress.png")
rightpress = pygame.transform.scale(up,(50,40))

left = pygame.image.load("left.png")
left = pygame.transform.scale(up,(50,40))

leftpress = pygame.image.load("leftpress.png")
leftpress = pygame.transform.scale(up,(50,40))

down = pygame.image.load("down.png")
down = pygame.transform.scale(up,(50,40))

downpress = pygame.image.load("downpress.png")
downpress = pygame.transform.scale(up,(50,40))

#RECTS
uprect = up.get_rect(center = (160,60))
uppressrect = uppress.get_rect(center=(160,60))
rightrect = right.get_rect(center=(200,90))
rightpressrect = rightpress.get_rect(center=(200,90))
leftrect = left.get_rect(center=(160,120))
leftpressrect = leftpress.get_rect(center=(160,120))
downrect = down.get_rect(center=(160,120))
downpressrect = downpress.get_rect(center =(160,120))
#





def init_home():
	screen.fill(black)
	pygame.draw.rect(screen,blue,title_rect,1)
	pygame.draw.rect(screen,blue,g1rect,1)
	pygame.draw.rect(screen,blue,g2rect,1)
	for my_text, text_pos in home_screen.items():
		text_surface = my_font.render(my_text,True,WHITE)
		rect = text_surface.get_rect(center=text_pos)
		screen.blit(text_surface,rect)

def init_game_one():
	screen.fill(black)
	for my_text, text_pos in g_one.items():
		text_surface = my_font.render(my_text,True,WHITE)
		rect = text_surface.get_rect(center=text_pos)
		screen.blit(text_surface,rect)
		
def init_game_two():
	screen.fill(black)
	for my_text, text_pos in g_two.items():
		text_surface = my_font.render(my_text,True,WHITE)
		rect = text_surface.get_rect(center=text_pos)
		screen.blit(text_surface,rect)
		
					
		
while (loop and stop >= time.time()):
	#Quit Logic
	for event in pygame.event.get():
		if ((event.type is pygame.MOUSEBUTTONDOWN)):
			pos = pygame.mouse.get_pos()
			x,y = pos
			if (y > 185 and y < 250):
				if (x > 220 and x < 300):
					loop = False


	#Check which screen to render
	if (level == 0):
		init_home()
		# Game Selection Logic
		for event in pygame.event.get():
			if ((event.type is pygame.MOUSEBUTTONDOWN)):
				pos = pygame.mouse.get_pos()
				x,y = pos
				if (y > 120 and y < 180):
					if (x > 50 and x < 110):
						level = 1
					elif (x > 210 and x < 270):
						level = 2
						
	elif (level == 1):
		init_game_one()
		for event in pygame.event.get():
			if ((event.type is pygame.MOUSEBUTTONDOWN)):pos = pygame.mouse.get_pos()
			x,y = pos
			if (y > 185 and y < 250):
				if (x > 30 and x < 90):
					level = 0
				elif (x > 220 and x < 300):
					loop = False
					# Render Buttons and Swap between images depending on GPIO
					
					
					
					
					
	elif (level == 2):
		init_game_two()
		#screen.blit(up,uprect)
		screen.blit(right,rightrect)
		for event in pygame.event.get():
			if ((event.type is pygame.MOUSEBUTTONDOWN)):pos = pygame.mouse.get_pos()
			x,y = pos
			if (y > 185 and y < 250):
				if (x > 30 and x < 90):
					level = 0
				elif (x > 220 and x < 300):
					loop = False
					
					#Render Buttons and and Swap between images depending on GPIO

					
	
	
	
	
	
	
	
		

	pygame.display.flip()

