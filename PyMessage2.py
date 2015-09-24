import socket

def listenerThread():
    

global sock
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((socket.gethostname(), 1551))

sock.listen(1)
conn, addr = sock.accept()

def receiver():
    while 1:
        mess = conn.recv(1024)
        print(str(mess.decode))

