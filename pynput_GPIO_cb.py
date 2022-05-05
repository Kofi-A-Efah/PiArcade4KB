import RPi.GPIO as GPIO
import time
from pynput.keyboard import Key, Controller



GPIO.setmode(GPIO.BCM)   # Set for broadcom numbering not board numbers...
# setup piTFT buttons
#                        V need this so that button doesn't 'float'!
#                        V   When button NOT pressed, this guarantees 
#                        V             signal = logical 1 = 3.3 Volts
loop = True

keyboard = Controller()

GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def GPIO22_callback(channel):
    pass

def GPIO27_callback(channel):
    keyboard.press(Key.down)
    keyboard.release(Key.down)


def GPIO23_callback(channel):
    keyboard.press(Key.up)
    keyboard.release(Key.up)


def GPIO26_callback(channel):
    pass



GPIO.add_event_detect(22,GPIO.LOW, callback=GPIO22_callback, bouncetime=50)
GPIO.add_event_detect(27,GPIO.LOW, callback=GPIO27_callback, bouncetime=50)
GPIO.add_event_detect(23,GPIO.LOW, callback=GPIO23_callback, bouncetime=50)
GPIO.add_event_detect(26,GPIO.LOW, callback=GPIO26_callback, bouncetime=50)


while loop:
    time.sleep(0.2)  # Without sleep, no screen output!
    if ( not GPIO.input(17) ):
        print (" ") 
        print ("Button 17 has been pressed...")
        loop = False


GPIO.cleanup()
