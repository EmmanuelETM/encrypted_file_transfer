from encrypt.encrypt import encrypt, decrypt
from encrypt.manage_file import read_text, write_text
from encrypt.validate import valid_paragraphs
from network.client import send_file
import os

def main():
    print("Encrypt program!!!\n\n")
    
    # Elimina la creación de un directorio 'output' y guarda en el directorio actual
    # Define el nombre del archivo de salida
    output_file = "encrypted_file.txt"
    
    # Lee el archivo de entrada
    file_path = input("Enter the path of the file (Default: text.txt (hit Enter)): ")

    if file_path == '':
        text = read_text('encrypt/text.txt')
    else:
        text = read_text(file_path)

    if not valid_paragraphs(text):
        print("\n\nThat text is not valid!!")
        return
    
    print("\nText read correctly!\n")
    
    # Solicita la clave de encriptación
    encryption_key = input("Enter the encrypt key (8 characters): ")
    while len(encryption_key) < 8:
        print("\nThe key must have 8 characters")
        encryption_key = input("\nPlease, enter a valid key (8 characters): ")

    # Encripta el texto
    encrypted = encrypt(text, encryption_key)

    # Guarda el archivo encriptado en el directorio actual
    write_text(output_file, encrypted)

    print(f"Encrypted file saved as '{output_file}'")

    # Opción para enviar el archivo a otro nodo
    send = input("Do you want to send the encrypted file to another node? (y/n): ").strip().lower()
    if send == 'y':
        send_file(output_file)

if __name__ == "__main__":
    main()
