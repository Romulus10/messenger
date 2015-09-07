import threading
import socket

class listener(threading.thread):
	def run(self):
		listen = socket(socket.AF_INET, socket.SOCK_STREAM)
		listen.connect((messenger.host, messenger.port))
		
		
class sender:
	def send(self):
		
	
class main:
	def main(self):
		print("Connect to:")
		self.host = raw_input()
		self.host = str(self.host)
		self.port = 1551
		
messenger = main()
