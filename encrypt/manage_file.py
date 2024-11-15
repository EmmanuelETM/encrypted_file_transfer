def read_text(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
        return text
    except FileNotFoundError:
        print(f"Error: El archivo '{file_path}' no se encuentra.")
        return None
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        return None
    

def write_text(file_path, encrypted_text):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write("===================== TEXTO ENCRIPTADO =====================\n")
        file.write(encrypted_text + "\n")
    print(f"\nFile created. Data has been written to '{file_path}'.")

