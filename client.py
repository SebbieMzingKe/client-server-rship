import socket

host = '127.0.0.1'
port = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((host, port))

while True:
   
    message = input("Enter a message (or 'exit' to quit): ")
    
    if message.lower() == 'exit':
        break

    client_socket.sendall(message.encode())
    data = client_socket.recv(1024)
    print(f"Received from server: {data.decode()}")

client_socket.close()
