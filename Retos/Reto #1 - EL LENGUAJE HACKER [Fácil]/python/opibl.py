
def cambiar_texto(texto):
    i = 0
    nuevo_texto = list(texto)
    while i < len(texto):
        if nuevo_texto[i] == 'A':
            nuevo_texto[i] = '4'
        if nuevo_texto[i] == 'B':
            nuevo_texto[i] = 'I3'
        if nuevo_texto[i] == 'C':
            nuevo_texto[i] = '['
        if nuevo_texto[i] == 'D':
            nuevo_texto[i] = ')'
        if nuevo_texto[i] == 'E':
            nuevo_texto[i] = '3'
        if nuevo_texto[i] == 'F':
            nuevo_texto[i] = '|='
        if nuevo_texto[i] == 'G':
            nuevo_texto[i] = '&'
        if nuevo_texto[i] == 'H':
            nuevo_texto[i] = '#'
        if nuevo_texto[i] == 'I':
            nuevo_texto[i] = '1'
        if nuevo_texto[i] == 'J':
            nuevo_texto[i] = ',_|'
        if nuevo_texto[i] == 'K':
            nuevo_texto[i] = '>|'
        if nuevo_texto[i] == 'L':
            nuevo_texto[i] = '1' 
        if nuevo_texto[i] == 'M':
            nuevo_texto[i] = '[V]'  
        if nuevo_texto[i] == 'N':
            nuevo_texto[i] = '^/'  
        if nuevo_texto[i] == "O":
            nuevo_texto[i] = '0'  
        if nuevo_texto[i] == 'P':
            nuevo_texto[i] = '|*'  
        if nuevo_texto[i] == 'Q':
            nuevo_texto[i] = '(_,)'  
        if nuevo_texto[i] == 'R':
            nuevo_texto[i] = 'I2'  
        if nuevo_texto[i] == 'S':
            nuevo_texto[i] = '5'  
        if nuevo_texto[i] == 'T':
            nuevo_texto[i] = '7'  
        if nuevo_texto[i] == 'U':
            nuevo_texto[i] = '(_)'
        if nuevo_texto[i] == 'V':
            nuevo_texto[i] = '\/'  
        if nuevo_texto[i] == 'W':
            nuevo_texto[i] = '\/\/'  
        if nuevo_texto[i] == 'X':
            nuevo_texto[i] = '><'  
        if nuevo_texto[i] == 'Y':
            nuevo_texto[i] = 'j' 
        if nuevo_texto[i] == 'Z':
            nuevo_texto[i] = '2' 


        i = i + 1                                                                                 

    texto = "".join(nuevo_texto)
    print("TEXTO TRANSFORMADO",texto)


texto = input('Escribe un texto\n')
texto = texto.upper()
cambiar_texto(texto)