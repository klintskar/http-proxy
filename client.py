import socket

def main():
    # Create a TCP/IP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the server on localhost
    server_address = ('localhost', 8080)
    client_socket.connect(server_address)

    print("Connected to server.")

    # Prepare the GET request for a blocked site
    blocked_site_url = "example.com"  # Replace this with the URL of the blocked site
    get_request = f"GET {blocked_site_url} HTTP/1.1\r\nHost: localhost\r\n\r\n"

    # Send the GET request to the server
    client_socket.sendall(get_request.encode())

    # Receive the server's response
    #data = client_socket.recv(1024)
    #print("Received from server:", data.decode())

if __name__ == "__main__":
    main()
