from unidecode import unidecode

alphabet = []
for i in range(97, 123):
    alphabet.append(chr(i))

alphabet.insert(alphabet.index("n") + 1, "ñ")

while True:

    word = input("Introduce una palabra: ")

    unicode_word = unidecode(word.lower().replace(
        "ñ", "_$_")).replace("_$_", "ñ")

    value = 0

    for letter in unicode_word:
        if letter in alphabet:
            value += alphabet.index(letter) + 1

    print(f"El valor de \"{word}\" es {value}")

    if value == 100:
        print("Has introducido una palabra de 100 puntos! El programa finalizará.")
        break
