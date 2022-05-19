import RPi.GPIO as GPIO
import time
import subprocess
import os
import pygame

GPIO.setmode(GPIO.BCM)   # Set for broadcom numbering not board numbers...

#GPIO stuff
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP)

## Pygame Setup
os.putenv('SDL_VIDEODRIVER', 'fbcon')
os.putenv('SDL_FBDEV', '/dev/fb0')
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
g_one = {'Pac-Man':(160,20),'Quit':(260,220),'Back':(60,220)}
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

#Circle Attributes	
red = (255,0,0)
green = (0,255,0)
circle_radius = 10
border_width = 0
circle_center = [79, 168]


#GUI OBJECTS
up = pygame.image.load("up.png")
up = pygame.transform.scale(up,(50,40))

uppress = pygame.image.load("uppress.png")
uppress = pygame.transform.scale(uppress,(50,40))

right = pygame.image.load("right.png")
right = pygame.transform.scale(right,(50,40))

rightpress = pygame.image.load("rightpress.png")
rightpress = pygame.transform.scale(rightpress,(50,40))

left = pygame.image.load("left.png")
left = pygame.transform.scale(left,(50,40))

leftpress = pygame.image.load("leftpress.png")
leftpress = pygame.transform.scale(leftpress,(50,40))

down = pygame.image.load("down.png")
down = pygame.transform.scale(down,(50,40))

downpress = pygame.image.load("downpress.png")
downpress = pygame.transform.scale(downpress,(50,40))

#RECTS
uprect = up.get_rect(center = (160,60))
uppressrect = uppress.get_rect(center=(160,60))

rightrect = right.get_rect(center=(200,90))
rightpressrect = rightpress.get_rect(center=(200,90))

leftrect = left.get_rect(center=(120,90))
leftpressrect = leftpress.get_rect(center=(120,90))

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
	screen.blit(up,uprect)
	screen.blit(right,rightrect)
	screen.blit(left,leftrect)
	screen.blit(down,downrect)
	for my_text, text_pos in g_one.items():
		text_surface = my_font.render(my_text,True,WHITE)
		rect = text_surface.get_rect(center=text_pos)
		screen.blit(text_surface,rect)
		
def init_game_two():
	screen.fill(black)
	screen.blit(up,uprect)
	screen.blit(right,rightrect)
	screen.blit(left,leftrect)
	screen.blit(down,downrect)
	pygame.draw.circle(screen,red,circle_center,circle_radius,border_width)
	pygame.draw.circle(screen,red,(circle_center[0]+40,circle_center[1]),circle_radius,border_width)
	pygame.draw.circle(screen,red,(circle_center[0]+80,circle_center[1]),circle_radius,border_width)
	pygame.draw.circle(screen,red,(circle_center[0]+120,circle_center[1]),circle_radius+5,border_width)
	pygame.draw.circle(screen,red,(circle_center[0]+160,circle_center[1]),circle_radius,border_width)
	if (not GPIO.input(17)):
		pygame.draw.circle(screen,green,circle_center,circle_radius,border_width)

	if (not GPIO.input(27)):
		pygame.draw.circle(screen,green,(circle_center[0]+40,circle_center[1]),circle_radius,border_width)


	if (not GPIO.input(26)):
		pygame.draw.circle(screen,green,(circle_center[0]+80,circle_center[1]),circle_radius,border_width)


	if (not GPIO.input(22)):
		pygame.draw.circle(screen,green,(circle_center[0]+120,circle_center[1]),circle_radius+5,border_width)


	if (not GPIO.input(13)):
		pygame.draw.circle(screen,green,(circle_center[0]+160,circle_center[1]),circle_radius,border_width)

	#if (not GPIO.input(19)):
	#	pygame.draw.circle(screen,green,(circle_center[0]+40,circle_center[1]),circle_radius,border_width)


	for my_text, text_pos in g_two.items():
		text_surface = my_font.render(my_text,True,WHITE)
		rect = text_surface.get_rect(center=text_pos)
		screen.blit(text_surface,rect)

def image_update():
	if (not GPIO.input(12)):
		screen.blit(leftpress,leftpressrect)
	else:
		screen.blit(left,leftrect)

	if (not GPIO.input(16)):
		screen.blit(rightpress,rightpressrect)
	else:
		screen.blit(right,rightrect)

	if (not GPIO.input(20)):
		screen.blit(uppress,uppressrect)
	else:
		screen.blit(up,uprect)

	if (not GPIO.input(21)):
		screen.blit(downpress,downpressrect)
	else:
		screen.blit(down,downrect)
		
while (loop):# and stop >= time.time()):
	
	#Quit Logic
	for event in pygame.event.get():
		if ((event.type is pygame.MOUSEBUTTONDOWN)):
			pos = pygame.mouse.get_pos()
			x,y = pos
			if (y < 30):
				if (x < 80):
					loop = False

	#Check which screen to render
	if (level == 0):
		init_home()
		# Game Selection Logic
		for event in pygame.event.get():
			if ((event.type is pygame.MOUSEBUTTONDOWN)):
				pos = pygame.mouse.get_pos()
				x,y = pos
				if (y > 40 and y < 100):
					if (x > 170 and x < 300):
						level = 1
					elif (x < 120):
						level = 2
						
	elif (level == 1):
		init_game_one()
		image_update()
		for event in pygame.event.get():
			if ((event.type is pygame.MOUSEBUTTONDOWN)):pos = pygame.mouse.get_pos()
			x,y = pos
			if (y < 30):
				if (x > 230):
					level = 0
				elif (x < 80):
					loop = False
					# Render Buttons and Swap between images depending on GPIO			
					
	elif (level == 2):
		init_game_two()
		image_update()
		for event in pygame.event.get():
			if ((event.type is pygame.MOUSEBUTTONDOWN)):pos = pygame.mouse.get_pos()
			x,y = pos
			if (y < 30):
				if (x > 170):
					level = 0
				elif (x < 80):
					loop = False
					
					#Render Buttons and and Swap between images depending on GPIO
	
	screen.blit(pygame.transform.rotate(screen,-180), (0,0))
	pygame.display.flip()

