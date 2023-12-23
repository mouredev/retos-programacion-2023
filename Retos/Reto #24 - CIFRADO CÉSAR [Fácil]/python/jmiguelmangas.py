"""/*
 * Crea un programa que realize el cifrado César de un texto y lo imprima.
 * También debe ser capaz de descifrarlo cuando así se lo indiquemos.
 *
 * Te recomiendo que busques información para conocer en profundidad cómo
 * realizar el cifrado. Esto también forma parte del reto.
 */"""

def get_sentence():
    return input("Escribe tu frase: ").strip()


def get_traduction():
    opcion = 0
    while opcion != 1 and opcion != 2:
        print("1- Español -> Cesar\n2- Cesar -> Español\n")
        try:
            opcion = int(input("Introduce tu opcion: "))
        except ValueError:
            print(opcion)
    try:
        desplazamiento = int(input("Que desplazamiento tiene el cifrado: "))
    except ValueError:
        print("Valor Cifrado incorrecto")
    return (opcion,desplazamiento)

def construir_nuevo_alphabeto(desplazamiento):
    lista_letras = ["a","b","c","d","e","f","g","h","i","j","k","l","m","ñ","o","p","q","r","s","t","u","v","x","y","z"]
    lista_new = []
    dictionary_traduction = {}
    for i in range(desplazamiento,len(lista_letras)):
        lista_new.append(lista_letras[i])
    for i in range(desplazamiento):
        lista_new.append(lista_letras[i])
    for i in range(len(lista_letras)):
        dictionary_traduction[lista_letras[i]] = lista_new[i]
    return dictionary_traduction
def traducir_alphabeto(desplazamiento):
    lista_letras = ["a","b","c","d","e","f","g","h","i","j","k","l","m","ñ","o","p","q","r","s","t","u","v","x","y","z"]
    lista_new = []
    dictionary_traduction = {}
    for i in range(desplazamiento,len(lista_letras)):
        lista_new.append(lista_letras[i])
    for i in range(desplazamiento):
        lista_new.append(lista_letras[i])
    for i in range(len(lista_letras)):
        dictionary_traduction[lista_new[i]] = lista_letras[i]
    return dictionary_traduction
def main():
    opcion,desplazamiento = get_traduction()
    frase = get_sentence()
    nueva_frase = ""
    
    if opcion == 1:
        dic = construir_nuevo_alphabeto(desplazamiento)
        for character in frase:
            if character in dic:
                nueva_frase = nueva_frase + dic[character]
            else:
                nueva_frase = nueva_frase + character
        print(nueva_frase)
    else:
        traduc = traducir_alphabeto(desplazamiento)
        for character in frase:
            if character in traduc:
                nueva_frase = nueva_frase + traduc[character]
            else:
                nueva_frase = nueva_frase + character
        print(nueva_frase)

    
if __name__  == "__main__":
    main()