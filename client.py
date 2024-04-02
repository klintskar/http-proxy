import socket

def main():
    # Create a TCP/IP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the server on localhost
    server_address = ('localhost', 8080)
    client_socket.connect(server_address)

    try:
        print("Connected to server.")

        while True:
            # Get user input
            message = input("Enter message to send: ")

            # Send the message to the server
            client_socket.sendall(message.encode())

            # Check for termination condition
            if message == "end":
                break

            # Receive the server's response
            data = client_socket.recv(1024)
            if not data:
                print("Server closed the connection.")
                break
            print("Received from server:", data.decode())

    finally:
        # Close the connection
        client_socket.close()

if __name__ == "__main__":
    main()
