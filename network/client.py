import socket
import os

def send_file(file_path, host="localhost", port=65432):
    try:
        # Crear el socket y conectarse al servidor
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((host, port))

            # Enviar el nombre del archivo
            file_name = os.path.basename(file_path)
            client_socket.sendall(file_name.encode('utf-8'))

            # Enviar el contenido del archivo
            with open(file_path, 'rb') as file:
                while (chunk := file.read(1024)):
                    client_socket.sendall(chunk)
                
            print(f"Archivo '{file_name}' enviado correctamente.")
    except Exception as e:
        print(f"Error al enviar el archivo: {e}")
