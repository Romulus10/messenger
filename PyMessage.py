import threading
import socket

class Listener(threading.Thread):
	def run(self):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.bind((socket.gethostname(),1551))
		sock.listen(10)
		conn, addr = sock.accept()
		
		print("Received a connection.")
		print("Say hi!")
		
		while true:
			message = conn.recv(1024)
			print(str(message.decode()))
			if str(message.decode()) == "bye":
				break
			
		conn.close()
		sock.close()
		
class Sender:
	def main(self):
		print("Welcome.")
		print("Enter a username:")
		name = str(raw_input())
		print("Enter an IP address to chat with.")
		host = str(raw_input())
		connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		connection.connect((host, 1551))
		print("Connected to " + host + ".")
		
		while true:
			message = str(raw_input())
			sock.send(message.encode())
		sock.close()

send = Sender()
listen = Listener()

listen.start()

send.main()
