import threading
import socket

class listener(threading.thread):
	def run(self):
		listen = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		listen.bind((messenger.host, messenger.port))
		while true:
			message = listen.recv(1024)
			print(message)
			if message == "bye":
				break
		listen.shutdown()
		listen.close()
		
		
class sender:
	def send(self):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.connect((messenger.host, messenger.port))
		while true:
			text = raw_input()
			text = str(text)
			if text == "bye":
				sock.send(text)
				break
			sock.send(text)
		
	
class main:
	def main(self):
		print("Connect to:")
		self.host = raw_input()
		self.host = str(self.host)
		self.port = 1551
		listen = listener()
		listen.start()
		send = sender()
		send.send()
		
messenger = main()
main.main()
