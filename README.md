# Emmanuel Torres Malena | 2021-1097
---
###  Encrypted File Transfer

#### Functionality

- **File Encryption**: The text file provided by the user is encrypted using a secret key provided by the user. 
- **File Transfer**: The encrypted file is sent from one node (client) to another (server) over a network connection using sockets.
- **Receiving and Storing**: The server receives the encrypted file and saves it in the directory where the script is executed.

#### Requirements

- Python 3.x
- No additional dependencies are required, as everything is implemented in pure Python (without external libraries).


## How It Works

### 1. **Client:**
   - The client reads a text file, encrypts it using a secret key provided by the user, and saves the encrypted file in the current directory as `encrypted_output.txt`.
   - Then, it offers the option to send the encrypted file to a server via a network connection.

### 2. **Server:**
   - The server waits to receive the encrypted file from a client.
   - Once it receives the file, it saves it in the directory where the script is running as `received_text.txt`.

## How to Run the Project

### 1. **Run the Server:**
   - In one terminal, navigate to the directory where `server.py` is located and run the following command to start the server:
   ```bash
   python network/server.py
