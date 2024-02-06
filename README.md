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

---
