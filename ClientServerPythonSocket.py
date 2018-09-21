import socket
import sys

from _thread import *

host = ''
port = 9500

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((host, port))
except socket.error as e:
    print(str(e))
    
s.listen(5)


def threaded_client(conn):
    conn.send(str.encode('Hi'))
    
    while True:
        data = conn.recv(2048)
        reply = 'goodbye'
        if not data:
            break
        conn.sendall(str.decode(reply))
    conn.close()

while True:
    conn, addr = s.accept()
    print('Hello')
                                           
    start_new_thread(threaded_client,(conn,))

    