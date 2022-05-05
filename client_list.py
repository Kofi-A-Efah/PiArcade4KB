import socket
import sys
import pickle
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('10.48.116.89', 10000)
#print >>sys.stderr, 'connecting to %s port %s' % server_address
print("Connecting to " + server_address[0] + " port " + str(server_address[1]) )
sock.connect(server_address)

try:
    
    # Send data
    #message = 'Arcade Pi 4000B Will Live!'
    message = [0,2,4,6]
    message_str = str(message)
   # print >>sys.stderr, 'sending "%s"' % message
    print( "Sending the message!")
    sock.sendall(message_str.encode())

    # Look for the response
    amount_received = 0
    amount_expected = len(message)
    
    while amount_received < amount_expected:
        data = sock.recv(4096)
        amount_received += len(data)
        #print >>sys.stderr, 'received "%s"' % data
        print("received " + data.decode())

finally:
    #print >>sys.stderr, 'closing socket'
    print("Closing Socket")
    sock.close()
