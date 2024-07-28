import socket
from socket import timeout

HOST = 'localhost'
PORT = 8001

socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket.settimeout(1.0)

print(f"Connected to server {HOST}:{PORT}")

while True:
    message = input("")
    socket.sendto(message.encode('utf-8'), (HOST, PORT))

    if message == "quit":
        data, server = socket.recvfrom(1024)
        print(data.decode('utf-8'))
        break
    if message == "stop":
        data, server = socket.recvfrom(1024)
        print(data.decode('utf-8'))
        break

socket.close()
