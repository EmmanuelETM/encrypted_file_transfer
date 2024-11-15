def valid_paragraphs(text):
    paragraphs = text.split("\n\n")  
    
    #Verificar que haya al menos 2 párrafos
    valid_paragraphs = 0
    for paragraph in paragraphs:
        #Contar las palabras del párrafo
        word_count = len(paragraph.split())  
        #Verificar si el párrafo tiene al menos 95 palabras
        if word_count >= 95:  
            valid_paragraphs += 1
    
    return valid_paragraphs >= 2