import RPi.GPIO as GPIO
import time
import subprocess
import os
import pygame

GPIO.setmode(GPIO.BCM)   # Set for broadcom numbering not board numbers...

## Pygame Stuff
os.putenv('SDL_VIDEODRIVER', 'fbcon')
os.putenv('SDL_FBDEV', '/dev/fb1')
os.putenv('SDL_MOUSEDRV', 'TSLIB')
os.putenv('SDL_MOUSEDEV', '/dev/input/touchscreen')

pygame.init() 
pygame.mouse.set_visible(False)

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

title_rect = (70,35,180,25)
g1rect = (37,136,100,25)
g2rect = (200,136,100,25)


home_screen = {'Pi Arcade Stick 4KB':(160,50), "Game 1":(80,150), "Game 2":(240,150)}
g_one = {'Pac-Man':(160,50)}
g_two = {'Guilty Gear +R':(160,50), 
'P':(80,195), 'K':(120,195), 'S':(160,195), 'HS':(200,195), 'D':(240,195),
}
 


global loop
loop = True 
stop = time.time() + 2



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

start_time = time.time()
while (loop and stop >= time.time()):
	init_game_two()

							
	
	for event in pygame.event.get():
		if ((event.type is pygame.MOUSEBUTTONDOWN)):
			pos = pygame.mouse.get_pos()
			x,y = pos
			if (y > 200 and y < 240):
				if x < 260 and x > 220:
					loop = False

		

	pygame.display.flip()

