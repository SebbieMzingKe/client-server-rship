import socket

host = '127.0.0.1'
port = 12345


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


server_socket.bind((host, port))

server_socket.listen()

print(f"Server listening on {host}:{port}")

client_socket, client_address = server_socket.accept()
print(f"Connection from {client_address}")

while True:

    data = client_socket.recv(1024)
    if not data:
        break
    
    print(f"Received from client: {data.decode()}")

  
    client_socket.sendall(data)

client_socket.close()
