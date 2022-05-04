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
server_address = ('10.48.41.129', 10000)
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

        buffer.append(connection.recv(4096))
        
        for i in range(len(buffer)):
            #Every input taken is removed from the buffer  
            #until the next time an input is streamed
            data_dec = buffer.pop(0).decode()
            print("Received " + data_dec + " Button")

            if (data_dec == 'quit'):
                loop = False

            if (data_dec.find('press',1) != -1):
                data_dec = data_dec.replace("press","")
                keyboard.press(data_dec)

            if (data_dec.find('release',1) != -1):
                data_dec = data_dec.replace('release',"")
                keyboard.release(data_dec)    





        else:
            print("No more data from client address, waiting for more...")
            
finally:
    # Clean up the connection
    print("Closing the Connection")
    connection.close()
  