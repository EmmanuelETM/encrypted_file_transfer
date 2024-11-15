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

#### Project Structure

/your-project-directory ├── encrypt/ │ ├── encrypt.py # Functions for encrypting and decrypting files │ ├── manage_file.py # Functions for reading and writing files │ └── validate.py # Functions for validating file paragraphs ├── network/ │ ├── client.py # Client code for sending the encrypted file │ └── server.py # Server code for receiving the file ├── main.py # Main script to run the client and server └── README.md # This file
