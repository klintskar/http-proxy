import socket
import threading
from http_handler import HTTPHandler  # Importing your HTTPHandler class

def handle_connection(server_socket, connection, client_address):
    print("Connection from:", client_address)
    try:
        if connection is None:
            print("Error: Connection is None")
            return  # Exit the function if connection is None
        
        # Ensure the connection is not closed unexpectedly
        if connection.fileno() == -1:
            print("Error: Connection closed unexpectedly")
            return
        
        handler = HTTPHandler(request=None, client_address=client_address, server=server_socket)
        handler.parse_request()
        handler.handle(connection.makefile('rb'))
    except AttributeError as e:
        print("Error handling connection:", e)
        # Handle the AttributeError here, e.g., by logging the error or sending an appropriate response to the client
    finally:
        if connection:
            connection.close()
            print("Connection with", client_address, "closed.")


def main():
    global terminate_flag
    
    # Create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind the socket to the port
    server_address = ('', 8080)  # Empty string indicates localhost
    server_socket.bind(server_address)
    
    # Listen for incoming connections
    server_socket.listen(3)
    
    print("Server is listening on port 8080...")
    
    threads = []

    try:
        while True:
            # Accept incoming connections
            connection, client_address = server_socket.accept()
            print("Accepted connection:", connection)  # Debugging statement
            
            if connection is None:
                print("Error: Connection is None")
                continue  # Skip handling this connection
            
            # Create a new thread to handle the connection
            thread = threading.Thread(target=handle_connection, args=(server_socket, connection, client_address))
            thread.start()
            
            threads.append(thread)
    except KeyboardInterrupt:
        print("\nKeyboardInterrupt received. Exiting...")
    
    finally:
        # Close all connections and join threads
        for thread in threads:
            thread.join()
        
        # Close the server socket
        server_socket.close()

if __name__ == "__main__":
    main()
