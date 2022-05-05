import socket
import sys
import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BCM)
# Set for broadcom numbering not board numbers...
# setup piTFT buttons
#                        V need this so that button doesn't 'float'!
#                        V   When button NOT pressed, this guarantees 
#                        V             signal = logical 1 = 3.3 Volts

#main loop bool
loop = True
message = []
global prev_press
global prev_press_w
global  prev_press_a
prev_press = False # False - Release, True - Press
prev_press_w = False
prev_press_a = False


def GPIO27_callback(channel):
    global prev_press
    if ( (not GPIO.input(27) ) and ( prev_press is False ) ):
        message.append('dpress')
        prev_press = True #
    else:
        message.append('drelease')
        prev_press = False

def GPIO23_callback(channel):
    global prev_press_w
    if (not GPIO.input(23) and ( prev_press_w is False )):
        message.append('wpress')
        prev_press_w = True
    elif ( GPIO.input(23)):
        message.append('wrelease')
        prev_press_w = False 


def GPIO22_callback(channel):
    global prev_press_a
    if (not GPIO.input(22) and ( prev_press_a is False ) ):
        message.append('apress')
        prev_press_a = True
    else:
        message.append('arelease')
        prev_press_a = False 


GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.add_event_detect(27,GPIO.BOTH, callback=GPIO27_callback, bouncetime=150)
GPIO.add_event_detect(23,GPIO.BOTH, callback=GPIO23_callback, bouncetime=35)
GPIO.add_event_detect(22,GPIO.BOTH, callback=GPIO22_callback, bouncetime=150)

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('10.48.41.129', 10000)
print("Connecting to " + server_address[0] + " port " + str(server_address[1]) )
sock.connect(server_address)

if os.path.exists("Log.txt"):
    os.remove("Log.txt")
    
file1 = open("/home/pi/ECE5725-Project/Log.txt","w")

while(loop):
    time.sleep(0.075)

    if ( not GPIO.input(17) ):
        loop = False
        message.append('quit')

    try:
        button = message.pop(0)
        file1.write(button +"\n")
        sock.sendall(button.encode())
        print("Sent " + str(button) + " to the computer")
    except:
        pass


file1.close()
sock.close()
