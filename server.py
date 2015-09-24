#server test
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.bind((socket.gethostname(),1551))
sock.listen(10)

conn, addr = sock.accept()

print("Connected with " + str(addr[0]) + ":" + str(addr[1]) + ".")

message = conn.recv(1024)
print(str(message.decode()))
conn.sendall(message)

conn.close()
sock.close()

