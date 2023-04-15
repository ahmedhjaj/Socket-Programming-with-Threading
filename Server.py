import socket

# Define server host and port
host = ""
port = 12000

# Create a TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the host and port
server_socket.bind((host, port))

# Listen for incoming connections
server_socket.listen(1)

# Define server name and server-chosen integer value
server_name = "Server of Youssef Elharty"
server_number = 42

# Accept incoming connections
while True:
    client_socket, address = server_socket.accept()
    print(f"Connection from {address} has been established.")

    # Receive client message
    data = client_socket.recv(1024).decode()
    client_name, client_number = data.split(",")
    if client_number > 100:
        socket.close()

    # Display client name, server name, and sum of numbers
    print(f"{client_name} connected to {server_name}")
    sum = int(client_number) + server_number
    print(f"Client number: {client_number}\nServer number: {server_number}\nSum: {sum}")

    # Send server name and server-chosen integer value back to client
    message = f"{server_name},{server_number}"
    client_socket.send(message.encode())

    # Close client connection
    client_socket.close()
