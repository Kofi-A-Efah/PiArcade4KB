from calendar import day_abbr
import socket
import sys
from wsgiref.simple_server import WSGIRequestHandler
import keyboard
import pyautogui
import pydirectinput

"""
This script receives a constant stream of inputs and simulates them on
the computer running the script

Default Arcade Stick Button Mappings:


For Game 1 (Pacman): 
up -> up
down -> down
left -> left
right -> right
Will use default controls 

For Game 2 (Guilty Gear):
For Simplicity, will set menu controls to be equal to in battle controls
use remap function to map arrow keys to wasd
maybe have punch be a confirm button?


"""

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Bind the socket to the port
server_address = ('10.48.56.59', 10000)
print( "Starting up on " + server_address[0] + " port " + str(server_address[1]))
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

# Wait for a connection
connection, client_address = sock.accept()
# Input Buffer which keyboard library processes
buffer = []
loop = True

try:
    print("Connection!")
    #Forever loop that will not stop. It will Always check for inputs
    while loop:

        buffer = connection.recv(4096)
        buffer = buffer.decode('utf-8')

        try:
            buffer = eval(buffer)
        except:
            # On exception, try to reacquire new input from buffer
            print("bad input is " + buffer)
            break

        # Loop through buffer, pressing the keys
        for i in range(len(buffer)):

            print("Received " + buffer[i] + " Button")

            if (buffer[i] == 'quit'):
                loop = False

            if (buffer[i].find('press',1) != -1):
                buffer[i] = buffer[i].replace("press","")
                keyboard.press(buffer[i])

            elif (buffer[i].find('release',1) != -1):
                buffer[i] = buffer[i].replace('release',"")
                keyboard.release(buffer[i])    

        else:
            print("No more data from client address, waiting for more...")
            
finally:
    # Clean up the connection
    print("Closing the Connection")
    connection.close()
  