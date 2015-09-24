#PyMessageServer

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.bind((socket.gethostname(),1551))
sock.listen(10)

conn, addr = sock.accept()

print("Enter a username.")
name = str(input())

print("Connected with " + str(addr[0]) + ":" + str(addr[1]) + ".")

while True:
    message = conn.recv(1024)
    print(str(message.decode()))
    mymessage = str(input())
    mymessage = str(name) + ": " + str(mymessage)
    conn.sendall(mymessage.encode())

conn.close()
sock.close()


