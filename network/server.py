import socket

def start_server(host="localhost", port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen(1)
        print("Esperando la conexión del cliente...")

        client_socket, client_address = server_socket.accept()
        with client_socket:
            print(f"Conexión establecida con {client_address}")
            
            # Recibir el archivo y guardarlo en el directorio actual como 'received_text.txt'
            try:
                # Recibir el nombre del archivo (aunque no es necesario, lo mostramos para referencia)
                file_name = client_socket.recv(1024).decode('utf-8')
                print(f"Recibiendo el archivo: {file_name}")

                # Guardar el archivo recibido en el directorio actual como 'received_text.txt'
                with open('../received_text.txt', 'wb') as f:
                    while True:
                        data = client_socket.recv(1024)
                        if not data:
                            break
                        f.write(data)

                print("Archivo recibido y guardado como 'received_text.txt'.")
            except Exception as e:
                print(f"Error al recibir el archivo: {e}")

if __name__ == "__main__":
    start_server()
