#One computer will have to handle acting as a client and the other
#will handle all the server operations.

import threading
import socket

class Client(threading.Thread):
        def main(self, name, host):
                self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.sock.connect((host, 1551))
                print("Connected to " + host + ".")
                while True:
                        message = str(input())
                        message = str(name) + ": " + str(message)
                        self.sock.send(message.encode())
                        self.sock.close()


print("Welcome.")
print("Enter a username:")
name = str(input())
print("Enter an address to chat with.")
host = str(input())
send = Client()
send.start()
send.main(name, host)
