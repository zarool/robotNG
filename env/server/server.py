import socket

HOST = '0.0.0.0'
PORT = 8000

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((HOST, PORT))

print(f"Server listening on IP: {HOST}:{PORT}")

while True:
    data, addr = server.recvfrom(1024)
    print(f"Connected by {addr}, message:\n{data.decode('utf-8')}")

    if data.decode('utf-8') == "quit":
        server.sendto("Connection closed by user, program terminated".encode('utf-8'), addr)
    if data.decode('utf-8') == "stop":
        server.sendto("Server turned off, program terminated".encode('utf-8'), addr)
        break
server.close()
