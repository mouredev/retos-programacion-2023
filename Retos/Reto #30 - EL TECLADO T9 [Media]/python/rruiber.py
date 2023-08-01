# Teclado T9

def T9 (i = input("Escribe tu mensaje en tu teclado T9, solo puedes usar digitos y guiones: ")): # Permite a la función leer el mensaje mediante una entrada.
    valores = {"1": ",", "11": ".", "111": "?", "1111": "!",
               "2": "a", "22": "b", "222": "c",
               "3": "d", "33": "e", "333": "f",
               "4": "g", "44": "h", "444": "i",
               "5": "j", "55": "k", "555": "l",
               "6": "m", "66": "n", "666": "o",
               "7": "p", "77": "q", "777": "r", "7777": "s",
               "8": "t", "88": "u", "888": "v",
               "9": "w", "99": "x", "999": "y", "9999": "z", "-": {}} # Diccionario de caracteres T9
    ultimo = "-"
    i = i+ultimo # Agrega un guión al final de la entrada para que la función guarde el caracter final
    mensaje_inicial = [] # Se usa para guardar el mensaje de prueba que pudiera contener errores, caracteres indeseados o códigos que no están en el diccionario
    mensaje_real = [] # Se usa para guardar el mensaje sin errores 
    read = [] # Se usa para leer el mensaje
    for j in i:
        if j not in valores:
            continue # ignora caracteres que no son dígitos y guión
        elif j != "-":
            read.append(j) # agrega a read caracteres que son dígitos
        if j == "-":
            read = "".join(read) # cuando aparece un guión nuevo convierte read a str
            mensaje_inicial.append(read) # agrega los digitos a mensaje de prueba      
            read = [] # resetea read
    # print(mensaje_inicial) 
    for i in range(len(mensaje_inicial)):
        if mensaje_inicial[i] in valores: # verifica que el mensaje de prueba contenga elementos del diccionario T9
            mensaje_real.append(mensaje_inicial[i]) # Agrega al mensaje los caracteres que no tienen errores
    # print(mensaje_real)
    for i in range(len(mensaje_real)):
        mensaje_real[i] = valores[mensaje_real[i]] # cambia los valores del en codigo T9 a caracteres del diccionario
    mensaje = "".join(mensaje_real) # escribe el mensaje traducido
    print(mensaje) # muestra el mensaje traducido

T9 ()