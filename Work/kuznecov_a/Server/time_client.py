from socket import socket, AF_INET, SOCK_STREAM
import time

cnt = 5

while cnt > 0:

    CLIENT_SOCK = socket(AF_INET, SOCK_STREAM)
    CLIENT_SOCK.connect(('localhost', 8008))
    client_msg = 'Hi, server'
    CLIENT_SOCK.send(client_msg.encode('utf-8'))

    RES_BYTES = CLIENT_SOCK.recv(2048)

    print(f'Message from server: {RES_BYTES.decode("utf-8")}')

    CLIENT_SOCK.close()

    cnt -= 1
    time.sleep(2)
