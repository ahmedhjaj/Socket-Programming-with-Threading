import socket


# define a function to start the client
def start_client():
    HOST = "192.168.43.166"  # set the IP address of the server
    PORT = 8000  # set the port number of the server

    with socket.socket(
        socket.AF_INET, socket.SOCK_STREAM
    ) as s:  # create a socket object
        s.connect(
            (HOST, PORT)
        )  # connect to the server using the IP address and port number

        while True:
            # Receive integer from user
            client_number = int(
                input("Enter an integer between 1 and 100: ")
            )  # prompt user to enter an integer

            # Define client name
            client_name = "Client of Hagag"

            # Send client name and integer to server
            message = (
                f"{client_name},{client_number}"  # create message to send to server
            )
            s.send(message.encode())  # send the message to the server
            data = s.recv(1024).decode()  # receive data from server
            server_name, server_number = data.split(
                ","
            )  # extract server name and number from data
            print(f"{client_name} connected to {server_name}")
            sum = (
                int(server_number) + client_number
            )  # calculate the sum of the client and server numbers
            print(
                f"Client number: {client_number}\nServer number: {server_number}\nSum: {sum}"
            )  # print the client and server numbers and their sum

            # Close client connection
            s.close()  # close the client socket connection
            break  # break out of the loop


if __name__ == "__main__":
    start_client()  # if the script is run directly, start the client
