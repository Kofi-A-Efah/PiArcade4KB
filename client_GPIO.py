import socket
import sys
import RPi.GPIO as GPIO
import time
import os
from callbacks import *

GPIO.setmode(GPIO.BCM)
# Set for broadcom numbering not board numbers...
# setup piTFT buttons

loop = True

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('10.48.47.103', 10000)
print("Connecting to " + server_address[0] + " port " + str(server_address[1]) )
sock.connect(server_address)

#Choosing game 1 or 2 for button configuration purposes
print("1 for game 1, 2 for game 2: ")
game = input()

assert (game == '1' or game == '2') 
sock.sendall(game.encode())

#removing file
if os.path.exists("Log.txt"):
    os.remove("Log.txt")

#Creating new log file
file1 = open("/home/pi/PiArcade4KB/Log.txt","w")

while(loop):
    try:
      time.sleep(0.025)

      #Quit
      if ( not GPIO.input(23)):
          loop = False
          message.append('quit')

      #Sending multiple inputs at once (simultaneous in real life), the message buffer must contain multiple inputs
      if len(message) >= 2:
          button = str(message)
          message.clear()
          file1.write(button + " " + "\n")
          sock.sendall(button.encode())
          print("Sent " + str(button) + " " +" to the computer")
      #Sending single inputs
      elif len(message) > 0:
          button = str(message)
          message.clear()
          file1.write(button + " " + "\n")
          sock.sendall(button.encode())
          print("Sent " + str(button) + " " +" to the computer")
          
    except:
        file1.close()

file1.close()
sock.close()
