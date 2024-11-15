def encrypt(text, key):
    encrypted_text = ""
    key_length = len(key)

    # Desplazar cada carácter con el valor de la clave correspondiente
    for i, char in enumerate(text):
        # Obtener valor ASCII de la clave
        byte = ord(key[i % key_length])  
        # Desplazamiento del carácter
        encrypted = chr(ord(char) + byte) 
        encrypted_text += encrypted

    return encrypted_text


def decrypt(encrypted_text, key):
    decrypted_text = ""
    length = len(key)

    #Desplazar en sentido contrario
    for i, char in enumerate(encrypted_text):
        #Obtener valor ASCII de la clave
        byte = ord(key[i % length])  
        #Desplazamiento inverso
        decrypted = chr(ord(char) - byte) 
        decrypted_text += decrypted

    return decrypted_text
