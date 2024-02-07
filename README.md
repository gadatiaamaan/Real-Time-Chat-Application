# Real-Time Chat Application

## Introduction

Welcome to my real-time chat application! This project aims to create a user-friendly platform for real-time communication using the Python programming language. By leveraging socket programming and the tkinter module for GUI, this application allows users to exchange messages seamlessly.

## Key Features and Descriptions

- **Starting Up the Server:** Starting the server is the first step to enabling users to join and start chatting. Without the server running, users cannot access the chatroom.

- **Joining the Chatroom as a User:** Users can join the chatroom by running the client.py script. Upon entering a username and clicking “Join,” they gain access to the chatroom and receive confirmation.

- **Sending Messages Between Users:** Once connected, users can exchange messages in real-time. Messages are broadcasted to all connected clients, facilitating smooth communication.

- **Leaving the Chatroom:** Exiting the chatroom is simple. Users can type "[EXIT]" in the chat box, triggering a logout procedure and notifying other users.

- **Group Chat Capabilities:** In addition to one-on-one conversations, the application supports group chats. Users can engage in group conversations by sending and receiving text messages.

- **Picking Back Up Where You Left Off:** Users can seamlessly resume conversations after logging out. Chat logs are saved for users to review.

## Installation and Usage

### Installation:

1. Clone the repository to your local machine by running the following command in your terminal:

    ```
    git clone https://github.com/gadatiaamaan/Real-Time-Chat-Application.git
    ```

### Usage:

1. **Start the server:** Run the server-side script by executing the following command in the terminal:

    ```
    python server.py
    ```

   This command initializes the server, enabling it to handle incoming client connections.

2. **Launch a client:** Open a new terminal window, navigate to the project's directory, and enter:

    ```
    python client.py
    ```

   This command launches the client application, connecting it to the running server.

3. **Connect multiple clients:** Repeat step 2 to create multiple client instances and enable simultaneous chatting among users.

**Note:**
- Ensure that Python is installed on your system before running the application.
- The server must be started before any clients can connect.

Feel free to reach out if you encounter any issues or have questions about the functionality!

## Technologies, Algorithms, and Concepts Used

### Technologies:

- **Python**: The primary programming language used for both server and client-side development. Python's simplicity and versatility make it an excellent choice for network programming tasks.
- **Socket Programming**: Leveraged to establish communication channels between the server and clients over a network. The `socket` module in Python provides the necessary functions and classes for implementing socket-based communication.
- **Tkinter**: Utilized for creating the graphical user interface (GUI) in the client-side application. Tkinter is Python's de-facto standard GUI toolkit, offering a simple and intuitive way to build desktop applications.
- **Threading**: Employed to handle multiple client connections concurrently on the server-side. Threading allows the server to listen for incoming connections while simultaneously processing messages from connected clients.

### Algorithms:

- **Message Broadcasting**: Implemented to deliver messages from one client to all other connected clients. When a client sends a message to the server, the server broadcasts the message to all clients in the chatroom, ensuring that everyone receives real-time updates.
- **Username Assignment**: Used to assign unique usernames to clients upon joining the chatroom. When a client connects to the server, they are prompted to enter a username. The server ensures that each username is unique and assigns it to the client for identification purposes during communication.

### Concepts:

- **Client-Server Architecture**: Adopted to facilitate communication between multiple clients and a central server. The server acts as a mediator, managing client connections and message distribution.
- **Real-Time Communication**: Enabled by establishing persistent connections between clients and the server. Clients can send and receive messages instantaneously, creating a seamless chatting experience.
- **Concurrency**: Employed to handle multiple client connections simultaneously on the server. Concurrency ensures that the server can handle a large number of clients concurrently without blocking or delaying message processing.
- **Event-Driven Programming**: Implemented in the client-side GUI application to handle user interactions and message handling. Tkinter's event-driven model allows the application to respond to user inputs and server messages in real-time, providing an interactive user experience.