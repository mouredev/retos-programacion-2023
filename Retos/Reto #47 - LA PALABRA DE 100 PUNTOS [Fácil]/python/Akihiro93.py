while True:
    word = input("Introduce la palabra: ")

    for i in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
        if i in word:
            print("Error")
            exit()
    break

dict_values = {
    'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9,
    'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'ñ': 15, 'o': 16, 'p': 17,
    'q': 18, 'r': 19, 's': 20, 't': 21, 'u': 22, 'v': 23, 'w': 24, 'x': 25,
    'y': 26, 'z': 27
}

for i in word:
    result = 0
    for i in word.lower():
        result += dict_values[i]

print(result)