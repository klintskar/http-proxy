import socket
import threading

# Global variable to signal termination
terminate_flag = False

def handle_connection(connection, client_address):
    print("Connection from:", client_address)
    try:
        while True:
            data = connection.recv(1024)
            if data:
                if data.decode() == "end":
                    break
                print("Received:", data.decode())
                connection.sendall(data)
    finally:
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
        while not terminate_flag:
            # Accept incoming connections
            connection, client_address = server_socket.accept()
            
            # Create a new thread to handle the connection
            thread = threading.Thread(target=handle_connection, args=(connection, client_address))
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
