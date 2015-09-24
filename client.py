#client test
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()

sock.connect((host, 1551))

print("Connected to " + host + " at port 1551")

message = "Test"

sock.send(message.encode())
the = sock.recv(1024)
print(str(the.decode()))
sock.close()
