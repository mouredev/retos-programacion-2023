# Heterograma --> Palabra o frase en la que cada letra aparece una única vez
# Isograma --> Palabra o frase en la que cada letra aparece el mismo número de veces
# Pangrama --> Frase que utiliza todas las letras del abecedario

# Importamos el módulo string
import string

# Con string.ascii_letters obtenemos las letras del alfabeto y las metemos en una lista.
# Tendremos en cuenta únicamente las minúsculas
my_letters_list = list(string.ascii_letters.lower())
# Vamos a incluir la ñ extendiendo la lista
new_characters = ["ñ"]
my_letters_list.extend(new_characters)


def elimina_tildes_may_esp(word): # Para no tener en cuenta las tildes, las mayúsculas ni los espacios
    word = word.replace("á","a")
    word = word.replace("é","e")
    word = word.replace("í","i")
    word = word.replace("ó","o")
    word = word.replace("ú","u")
    word = word.lower()
    word = word.replace(" ", "")
    return word


def get_heterograma(word): # Un heterograma es una palabra o frase sin letras repetidas
    heterograma = bool
    word = elimina_tildes_may_esp(word)
    # Si tiene alguna letra repetida su número será > 1 
    # Recorremos todos los caracteres de la lista con las letras de la palabra para comprobar si alguna se repite
    for char in my_letters_list:
        if word.count(char) <= 1:
            heterograma = True
        elif word.count(char) > 1:
            heterograma = False
            break
    return heterograma


def get_isograma(word):
    isograma = bool
    my_dict_char = {}
    word = elimina_tildes_may_esp(word)
    for char in word:
        if word.count(char) != 0:
            my_dict_char[char] = word.count(char)
            # Obtenemos los valores máximo y mínimo del diccionario
            valor_maximo = max(my_dict_char.values())
            valor_minimo = min(my_dict_char.values())
            # Si el max y el min son iguales es un isograma
            if valor_maximo == valor_minimo:
                isograma = True
            else:
                isograma = False
    return isograma


def get_pangrama(word): # Ejemplo de panagrama "Fabio me exige, sin tapujos, que añada cerveza al whisky"
    pangrama = bool
    my_dict_char = {}
    word = elimina_tildes_may_esp(word)
    # Contamos el número de veces que aparece cada letra recorriendo la lista de letras
    for char in my_letters_list:
        my_dict_char[char] = word.count(char)
    valor_minimo = min(my_dict_char.values())
    # Si el valor mínmo es cero es que se han usado todos los caracteres
    if valor_minimo != 0:
        pangrama = True
    else:
        pangrama = False
    return pangrama


palabra = input("Introduzca una palabra o frase para determinar si es heterograma, isograma y pangrama: " )

if get_heterograma(palabra) == False:
    print(f"\"{palabra}\" NO es un heterograma")
else:
    print(f"\"{palabra}\" SI es un heterograma")

if get_isograma(palabra) == False:
    print(f"\"{palabra}\" NO es un isograma")
else:
    print(f"\"{palabra}\" SI es un isograma")

if get_pangrama(palabra) == False:
    print(f"\"{palabra}\" NO es un pangrama")
else:
    print(f"\"{palabra}\" SI es un pangrama")