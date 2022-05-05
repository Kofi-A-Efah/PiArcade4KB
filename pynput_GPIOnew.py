import RPi.GPIO as GPIO
import time
import keyboard
import os

GPIO.setmode(GPIO.BCM)   # Set for broadcom numbering not board numbers...
# setup piTFT buttons
#                        V need this so that button doesn't 'float'!
#                        V   When button NOT pressed, this guarantees 
#                        V             signal = logical 1 = 3.3 Volts
loop = True

GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)


global time_since
time_since = time.time()+4

def GPIO27_callback(channel):
    time_since = time.time() + 4


GPIO.add_event_detect(27,GPIO.FALLING, callback=GPIO27_callback, bouncetime=300)

while loop:
    time.sleep(0.08)  # Without sleep, no screen output!

    if ( (not GPIO.input(27))):
        keyboard.press_and_release('up')
        time.sleep(0.1)

    elif ( not GPIO.input(27)):
        keyboard.press_and_release('up')




    elif ( not GPIO.input(17) ):
        print (" ") 
        print ("Button 17 has been pressed...")
        loop = False


#    elif ( not GPIO.input(23) ): # Setting GPIO 27 to act as a "command scroll" for terminal
#        if GPIO.input(23):
#            keyboard.release(Key.up)
#        elif (not GPIO.input(23)):
#            keyboard.press(Key.up)
        #keyboard.release(Key.down)


    #elif ( not GPIO.input(23) ):
     #   keyboard.press(Key.up)
      #  keyboard.release(Key.up)
