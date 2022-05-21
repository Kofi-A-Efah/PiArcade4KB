from calendar import day_abbr
from encodings import utf_8
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
W -> up
S -> down
A -> left
D -> right

"""

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Bind the socket to the port
server_address = ('10.48.47.103', 10000)
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
        if (buffer == '1'): # Choosing control mapping
            game = 1
        elif (buffer == '2'):
            game = 2
        else:
            buffer = buffer.replace("][",",") # Edit the input buffer to be "Valid"
            buffer = buffer.strip("][")
            buffer = buffer.split(',')

        # Loop through buffer, pressing the keys
        for i in range(len(buffer)):
            if (buffer[i] == '1'):
                continue
            elif (buffer[i] == '2'): # Change controls
                continue

            print("Received " + buffer[i] + " Button")

            if (eval(buffer[i]) == 'quit'): # To quit the script
                loop = False

            if (game == 2): # Remapping "up down left right" to "wasd"
                buffer[i] = buffer[i].replace("upp","wp")
                buffer[i] = buffer[i].replace("uprel","wrel")
                buffer[i] = buffer[i].replace("down","s")
                buffer[i] = buffer[i].replace("left","a")
                buffer[i] = buffer[i].replace("right","d")

            if (buffer[i].find('press',1) != -1): # Search for button press and use keyboard.press to simulate it
                buffer[i] = buffer[i].replace("press","")
                keyboard.press(eval(buffer[i]))

            elif (buffer[i].find('release',1) != -1): # Same thing as above, but for release
                buffer[i] = buffer[i].replace('release',"")
                keyboard.release(eval(buffer[i]))


        else:
            print("No more data from client address, waiting for more...")

except:
    # Clean up the connection
    print("Closing the Connection")
    connection.close()
  