# Import required modules
import socket
import threading
import tkinter as tk
from tkinter import scrolledtext, messagebox

# Define constants
CLIENT_HOST = '127.0.0.1'
CLIENT_PORT = 1234

# Define constants for UI colors and fonts
LIGHT_GREY = '#F2F2F2'
DARK_BLUE = '#001F3F'
BLACK = 'black'
OCEAN_BLUE = '#0074E4'
FONT = ("Arial", 15)
BUTTON_FONT = ("Arial", 12)
SMALL_FONT = ("Arial", 12)

# Create a socket object
# AF_INET: Use IPv4 addresses
# SOCK_STREAM: Use TCP packets for communication
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Function to display a message in the GUI message box
def display_message(message):
    message_box.config(state=tk.NORMAL)
    message_box.insert(tk.END, message + '\n')
    message_box.config(state=tk.DISABLED)

# Function to connect to the server
def connect():
    try:
        client_socket.connect((CLIENT_HOST, CLIENT_PORT))
        print("Successfully connected to server")
        display_message("[SERVER] Successfully connected to the server")
    except:
        messagebox.showerror("Connection Error", f"Unable to connect to server {CLIENT_HOST} {CLIENT_PORT}")

    # Get the username from the entry field
    username = username_entry.get()
    if username != '':
        client_socket.sendall(username.encode())
    else:
        messagebox.showerror("Invalid username", "Username cannot be empty")

    # Start a thread to listen for messages from the server
    threading.Thread(target=listen_for_messages_from_server, args=(client_socket,)).start()

    # Disable username entry and join button after successful connection
    username_entry.config(state=tk.DISABLED)
    join_button.config(state=tk.DISABLED)

# Function to send a message to the server
def send_message():
    # Get the message from the entry field
    message = message_entry.get()
    if message != '':
        # Send the message to the server
        client_socket.sendall(message.encode())
        # Clear the message entry field
        message_entry.delete(0, len(message))
    else:
        messagebox.showerror("Empty message", "Message cannot be empty")

# Create the main GUI window
root = tk.Tk()
root.geometry("600x600")
root.title("Messenger Client")
root.resizable(False, False)

# Configure grid rows for layout
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=4)
root.grid_rowconfigure(2, weight=1)

# Create top, middle, and bottom frames for the UI
top_frame = tk.Frame(root, width=600, height=100, bg=LIGHT_GREY)
top_frame.grid(row=0, column=0, sticky=tk.NSEW)

middle_frame = tk.Frame(root, width=600, height=400, bg=DARK_BLUE)
middle_frame.grid(row=1, column=0, sticky=tk.NSEW)

bottom_frame = tk.Frame(root, width=600, height=100, bg=LIGHT_GREY)
bottom_frame.grid(row=2, column=0, sticky=tk.NSEW)

# Create UI elements in the top frame: username label, entry, and join button
username_label = tk.Label(top_frame, text="Enter username:", font=FONT, bg=LIGHT_GREY, fg=DARK_BLUE)
username_label.pack(side=tk.LEFT, padx=10)

username_entry = tk.Entry(top_frame, font=FONT, bg=DARK_BLUE, fg=LIGHT_GREY, width=40)
username_entry.pack(side=tk.LEFT)

join_button = tk.Button(top_frame, text="Join", font=BUTTON_FONT, bg=OCEAN_BLUE, fg=BLACK, command=connect)
join_button.pack(side=tk.LEFT, padx=15)

# Create UI elements in the bottom frame: message entry, send button
message_entry = tk.Entry(bottom_frame, font=FONT, bg=DARK_BLUE, fg=LIGHT_GREY, width=53)
message_entry.pack(side=tk.LEFT, padx=10)

send_button = tk.Button(bottom_frame, text="Send", font=BUTTON_FONT, bg=OCEAN_BLUE, fg=BLACK, command=send_message)
send_button.pack(side=tk.LEFT, padx=10)

# Create a scrolled text box in the middle frame for displaying messages
message_box = scrolledtext.ScrolledText(middle_frame, font=SMALL_FONT, bg=DARK_BLUE, fg=LIGHT_GREY, width=93, height=38)
message_box.config(state=tk.DISABLED)
message_box.pack(side=tk.TOP)


# Function to listen for messages from the server
def listen_for_messages_from_server(client):
    while True:
        # Receive and decode messages from the server
        message = client.recv(2048).decode('utf-8')
        if message != '':
            # Extract sender's username and message content
            sender_username, content = message.split("~")
            # Display the message in the GUI
            display_message(f"[{sender_username}] {content}")
        else:
            # Show an error if the received message is empty
            messagebox.showerror("Error", "Message received from the client is empty")

# Start the GUI main loop
def main():
    root.mainloop()

if __name__ == '__main__':
    main()
