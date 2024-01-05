from unidecode import unidecode

alfabeto = []
for i in range(97, 123):
    alfabeto.append(chr(i))

alfabeto.insert(alfabeto.index("n") + 1, "ñ")

while True:

    word = input("Introduce una palabra: ")

    unicode_word = unidecode(word.lower().replace(
        "ñ", "_$_")).replace("_$_", "ñ")

    val = 0

    for letra in unicode_word:
        if letra in alfabeto:
            val += alfabeto.index(letra) + 1

    print(f"El valor de \"{word}\" es {val}")

    if val == 100:
        print("Has introducido una palabra de 100 puntos! El programa finalizará.")
        break
