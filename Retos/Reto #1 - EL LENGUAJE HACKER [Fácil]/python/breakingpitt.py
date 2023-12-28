LEET_DICTIONARY = {
    "A": "4", "B": "I3", "C": "[", "D": ")", "E": "3", "F": "|=", "G": "&", "H": "#", "I": "1",
    "J": ",_|", "K": ">|", "L": "1", "M": "/\\/\\", "N": " ^/", "O": "0", "P": " |*", "Q": "(_,)",
    "R": "I2", "S": "5", "T": "7", "U": "(_)", "V": "\\/", "W": "\\/\\/", "X": "><", "Y": "j", "Z": "2",
    "1": "L", "2": "R", "3": "E", "4": "A", "5": "S", "6": "b", "7": "T", "8": "B", "9": "g", "0": "o"
}

def leet_translator(text):
    leet_text = ""

    for char in text:
        leet_char = LEET_DICTIONARY.get(char.upper(), char)
        leet_text += leet_char

    return leet_text

if __name__ == "__main__":
    user_input = input("Texto a traducir: ")
    print(leet_translator(user_input))
