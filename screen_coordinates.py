import pygame
from pygame.locals import *
import os
import RPi.GPIO as GPIO
import time

os.putenv('SDL_VIDEODRIVER', 'fbcon')
os.putenv('SDL_FBDEV', '/dev/fb0')
os.putenv('SDL_MOUSEDRV', 'TSLIB')
os.putenv('SDL_MOUSEDEV', '/dev/input/touchscreen')

GPIO.setmode(GPIO.BCM)   # Set for broadcom numbering not board numbers...

GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)

pygame.init() 

pygame.mouse.set_visible(False)
WHITE = 255, 255, 255
black = 0,0,0

size = width, height = 320, 240 
speed1 = [2,2]
speed2 = [1,1] 


my_font = pygame.font.Font(None,25)
mybuttons = {'quit':(160,180)}
screen = pygame.display.set_mode(size)  
screen.fill(black)  # Erase the Work space 



pygame.display.flip()  # display workspace on screen

loop = True
stop_time = time.time() + 30
while(loop and (time.time() <= stop_time)):
    screen.fill(black)
    time.sleep(0.2)
    
    if ( not GPIO.input(17) ):
        print (" ") 
        print ("Button 17 has been pressed...")
        loop = False
        
    for my_text, text_pos in mybuttons.items():
      text_surface = my_font.render(my_text,True,WHITE)
      rect = text_surface.get_rect(center=text_pos)
      screen.blit(text_surface,rect)
   
   
    if(pygame.event.get() is MOUSEBUTTONDOWN or MOUSEBUTTONUP):
          pos = pygame.mouse.get_pos()
          x,y = pos
          coordinates = 'Touch at ' + str(x) + ',' + str(y)
          text_surface = my_font.render(coordinates,True,WHITE)
          rect = text_surface.get_rect(center=(150,80))
          print(pos)
          if y > 40 and y < 60:
              if x < 60 and x > 20:
                  loop = False
                    
    screen.blit(text_surface,rect)
    screen.blit(pygame.transform.rotate(screen,-180), (0,0))
    pygame.display.flip()  # display workspace on screen

                    
            
