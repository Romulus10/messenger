#PyMessageClient

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()

sock.connect((host, 1551))

print("Connected to " + host + ".")

while true:
    message = str(input())
    sock.sendall(message.encode())
    
