'''
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
 *   con el alfabeto y los números en "leet".
    (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 '''
 
datos = input('Escribe el texto que quieras traducir: \n')
resultado = ''
for i in range(len(datos)):
    match (datos[i].lower()):
        case 'a':
            resultado += '4'
        case 'b':
            resultado += '8'
            
        case 'c':
            resultado += '['
            
        case 'd':
            resultado += '|)'
            
        case 'e':
            resultado += '3'
            
        case 'f':
            resultado += '|='
            
        case 'g':
            resultado += '&'
            
        case 'h':
            resultado += '#'
            
        case 'i':
            resultado += '1'
            
        case 'j':
            resultado += ']'
            
        case 'k':
            resultado += '>|'
            
        case 'l':
            resultado += '1'
            
        case 'm':
            resultado += '/\\/\\'
            
        case 'n':
            resultado += '|\\|'
            
        case 'o':
            resultado += '0'
            
        case 'p':
            resultado += '|*'
            
        case 'q':
            resultado += '9'
            
        case 'r':
            resultado += '|2'
            
        case 's':
            resultado += '5'
            
        case 't':
            resultado += '7'
            
        case 'u':
            resultado += '|_|'
            
        case 'v':
            resultado += '\\/'
            
        case 'w':
            resultado += '\\/\\/'
            
        case 'x':
            resultado += '><'
            
        case 'y':
            resultado += 'j'
            
        case 'z':
            resultado += '2'
            
        case '1':
            resultado += 'L'
            
        case '2':
            resultado += 'R'
            
        case '3':
            resultado += 'E'
            
        case '4':
            resultado += 'A'
            
        case '5':
            resultado += 'S'
            
        case '6':
            resultado += 'G'
            
        case '7':
            resultado += 'T'
            
        case '8':
            resultado += 'B'
            
        case '9':
            resultado += 'q'
            
        case '0':
            resultado += 'o'
            
        case _:
            resultado += datos[i]  
print(resultado)
    
        