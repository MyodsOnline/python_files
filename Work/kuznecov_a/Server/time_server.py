from socket import socket, AF_INET, SOCK_STREAM
import time

SERV_SOCK = socket(AF_INET, SOCK_STREAM)
SERV_SOCK.bind(('', 8008))
SERV_SOCK.listen(1)

try:
    while True:
        CLIENT_SOCK, ADDR = SERV_SOCK.accept()
        print(f'Incoming connection from client {ADDR}')
        TIMESTR = time.ctime(time.time()) + '\n'
        data = CLIENT_SOCK.recv(2048)
        print(f'Maessage {data} accept. {TIMESTR}')
        msg = f'Your message accept. {TIMESTR}'
        CLIENT_SOCK.send(msg.encode('utf-8'))
        CLIENT_SOCK.close()
finally:
    SERV_SOCK.close()
