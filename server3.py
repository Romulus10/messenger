import socket
import threading

print("PyMessage Server version 0.0.1")
#Starts with an empty message queue.
messageQueue = []
#Contains the entire list of connected users.
connected = []
#A socket object for the actual server, which can handle 10 connections at once.
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((socket.gethostname(),1551))
sock.listen(10)

#Main loop for handling serving messages.
while True:
    

    
#Shuts off and closes the socket.
sock.shutdown()
sock.close()
