import re


def parse(text: str):

    words_count = 0
    letter_count = 0
    sentences_count = 0
    longest_word = []

    words = text.replace("\n", " ").split(" ")

    for word in words:

        if len(word) != 0:

            if "." in word:
                sentences_count += 1

            current_word = re.sub(r"[^\w]", "", word)

            print(current_word)

            words_count += 1
            letter_count += len(current_word)

            if len(longest_word) == 0 or len(longest_word[0]) == len(current_word):
                longest_word.append(current_word)
            elif len(current_word) > len(longest_word[0]):
                longest_word.clear()
                longest_word.append(current_word)

    print(f"El número total de palabras es: {words_count}")
    print(f"La longitud media es: {letter_count / words_count}")
    print(f"Número de oraciones: {sentences_count}")
    print(f"La palabra o palabras más largas son: {longest_word}")


parse("""
Nos encontramos en un
periodo de guerra civil. Las
naves espaciales rebeldes,
atacando desde una base
oculta, han logrado su 
primera victoria contra
el malvado Imperio
Galáctico.

Durante la batalla, los 
espías rebeldes han
conseguido apoderarse de 
los planos secretos del
arma total y definitiva del
Imperio, la ESTRELLA
DE LA MUERTE,
una estación espacial
acorazada, llevando en sí
potencia suficiente para
destruir a un planeta
entero.

Perseguida por los 
siniestros agentes del 
Imperio, la Princesa Leia 
vuela hacia su patria, a
bordo de su nave espacial,
llevando consigo los
planos robados, que
pueden salvar a su pueblo
y devolver la libertad a la
galaxia....
""")
