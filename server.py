# Import required modules
import socket
import threading

# Define constants
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 1234
LISTENER_LIMIT = 5
ACTIVE_CLIENTS = []  # List of all currently connected users

# Function to receive messages from a specific client
def receive_messages_from_client(client, username):
    while True:
        # Receive and decode messages from the client
        message = client.recv(2048).decode('utf-8')
        if message != '':
            # Format the message with the sender's username and broadcast it to all clients
            formatted_msg = f'{username}~{message}'
            broadcast_message(formatted_msg)
        else:
            print(f"The message sent from client {username} is empty")

# Function to send a message to a specific client
def send_message_to_client(client, message):
    client.sendall(message.encode())

# Function to broadcast a message to all connected clients
def broadcast_message(message):
    for user in ACTIVE_CLIENTS:
        send_message_to_client(user[1], message)

# Function to handle a new client connection
def handle_client(client):
    while True:
        # Receive and decode the username from the client
        username = client.recv(2048).decode('utf-8')
        if username != '':
            # Add the client to the active clients list and broadcast the joining message
            ACTIVE_CLIENTS.append((username, client))
            prompt_message = f"SERVER~{username} joined the chat"
            broadcast_message(prompt_message)
            break
        else:
            print("Client username is empty")

    # Start a new thread to listen for messages from the client
    threading.Thread(target=receive_messages_from_client, args=(client, username,)).start()

# Main function
def main():
    # Create a socket object
    # AF_INET: Use IPv4 addresses
    # SOCK_STREAM: Use TCP packets for communication
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Bind the socket to the server address
        server_socket.bind((SERVER_HOST, SERVER_PORT))
        print(f"Running the server on {SERVER_HOST} {SERVER_PORT}")
    except:
        print(f"Unable to bind to host {SERVER_HOST} and port {SERVER_PORT}")

    # Set the maximum number of queued connections
    server_socket.listen(LISTENER_LIMIT)

    # Continuously accept incoming client connections
    while True:
        client_socket, address = server_socket.accept()
        print(f"Successfully connected to client {address[0]} {address[1]}")

        # Start a new thread to handle the connected client
        threading.Thread(target=handle_client, args=(client_socket,)).start()

# Execute the main function when the script is run
if __name__ == '__main__':
    main()
