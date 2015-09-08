#PyMessageServer script

import socket
import threading

class Main:

    def main(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((socket.gethostname(),1551))
        sock.listen(10)

        while True:
            conn, addr = sock.accept()
            print("Connected from " + addr[0] + ".")
            thread = ServerThread(run, conn)
            thread.start()


class ServerThread(threading.Thread):
    def run(self, conn):
        message = conn.recv(1024)
        print(str(message.decode))
        conn.sendall(message)
