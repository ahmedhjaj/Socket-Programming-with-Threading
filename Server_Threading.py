import socket
import threading

count = 1  # initialize a variable to keep track of the number of connections


# define a function to handle incoming client requests
def handle_client(conn, addr, server_name, server_number):
    print(f"New connection from {addr}")
    with conn:
        while True:
            global count  # use the global count variable
            data = conn.recv(2048).decode()  # receive client request data
            if not data:  # if there is no data, break out of the loop
                break
            client_name, client_number = data.split(
                ","
            )  # extract client name and number from data
            if (
                int(client_number) > 100 or int(client_number) < 0
            ):  # check if client number is within the range
                break
            client_name, client_number = data.split(
                ","
            )  # extract client name and number from data
            print(
                f"# {count}  {client_name} connected to {server_name}"
            )  # print connection message
            print(f"Client's Number: {client_number}")  # print client number
            sum = (
                int(client_number) + server_number
            )  # calculate the sum of the client and server numbers
            print(f"{client_number} + {server_number} = {sum}")  # print the sum
            modifiedMessage = f"{server_name},{server_number}"  # create modified message to send back to client
            conn.sendall(
                modifiedMessage.encode()
            )  # send the modified message to the client
            count += 1  # increment the count variable


# define a function to start the server
def start_server():
    HOST = "192.168.43.166"  # set the IP address of the server
    PORT = 8000  # set the port number of the server
    server_name = "Server of the Best Harty Ever"  # set the name of the server
    server_number = 42  # set a number associated with the server
    with socket.socket(
        socket.AF_INET, socket.SOCK_STREAM
    ) as s:  # create a socket object
        s.bind(
            (HOST, PORT)
        )  # bind the socket to the specified IP address and port number
        s.listen()  # set the socket to listen for incoming connections
        print(f"Server listening on {HOST}:{PORT}")
        while True:  # continuously accept incoming client connections
            conn, addr = s.accept()  # accept the client connection
            thread = threading.Thread(
                target=handle_client, args=(conn, addr, server_name, server_number)
            )  # create a new thread to handle the connection
            thread.start()  # start the thread to handle the connection


if __name__ == "__main__":
    start_server()  # if the script is run directly, start the server
