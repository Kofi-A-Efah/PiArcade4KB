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
my_font = pygame.font.Font(None,25)
center = (160, 220)
border_width = 0



#GUI Elements

title_rect = (70,35,180,25)
g1rect = (37,136,100,25)
g2rect = (200,136,100,25)

home_screen = {'Pi Arcade Stick 4KB':(160,50), "Game 1":(80,150), "Game 2":(240,150),"Quit":(160,220)}
g_one = {'Pac-Man':(160,50),'Quit':(160,220)}
g_two = {'Guilty Gear +R':(160,50), 
'P':(80,205), 'K':(120,205), 'S':(160,205), 'HS':(200,205), 'D':(240,205), 'Quit':(160,220)}
 


# Loop Control
global loop
loop = True 
stop = time.time() + 2

#Game Select
level = 0 # Home Screen
#level = 1  Game 1
#level = 2  Game 2


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
		
"""
Checking for so many buttons in the main while loop is a little 
annoying, so we wrapped it in a subroutine. This will set some key
variables when buttons on the piTFT are pressed.

x: x coordinate of button
y: y coordinate of button

Return: 
"""
def check_button(xcord,ycord):
	if (xcord == 80):
		game = "Game 1"
	elif (xcord == 240):
		game = "Game 2"
	elif (xcord == 160 and ycord == 220):
		game = "Quit"
		
	for event in pygame.event.get():
		if ((event.type is pygame.MOUSEBUTTONDOWN)):
			pos = pygame.mouse.get_pos()
			x,y = pos
			if (y < ycord + 30 and y > ycord - 30):
				if (x < xcord + 30 and x > xcord - 30):
					return game
					
		

start_time = time.time()
while (loop):# and stop >= time.time()):
	#Check which screen to render
	if (level == 0):
		
		init_home()
		if (check_button(160,220) == "Quit"):
			loop = False
		elif (check_button(80,150) == "Game 1"):
			level = 1
		else:
			level = 2
		
	elif (level == 1):
		init_game_one()
	else:
		init_game_two()
	
	## TO DO: Add logic for selecting games, quitting and going back
	## Deadline Tomorrow

		
							
	


		

	pygame.display.flip()

