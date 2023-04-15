import socket

# Define server host and port
host = "192.168.43.166"
port = 8000

# Create a TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server
client_socket.connect((host, port))

# Receive integer from user
client_number = int(input("Enter an integer between 1 and 100: "))

# Define client name
client_name = "Client of Youssef Elharty"

# Send client name and integer to server
message = f"{client_name},{client_number}"
print(message.split())
client_socket.send(message.encode())

# Receive server message
data = client_socket.recv(1024).decode()
server_name, server_number = data.split(",")

# Display client name, server name, and sum of numbers
print(f"{client_name} connected to {server_name}")
sum = int(server_number) + client_number
print(f"Client number: {client_number}\nServer number: {server_number}\nSum: {sum}")

# Close client connection
client_socket.close()
