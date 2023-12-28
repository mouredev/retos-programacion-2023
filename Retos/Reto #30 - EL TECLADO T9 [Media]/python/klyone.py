#!/usr/bin/env python3

t9_dict = {
    "2" : "A",
    "22" : "B",
    "222" : "C",
    "3" : "D",
    "33" : "E",
    "333" : "F",
    "4" : "G",
    "44" : "H",
    "444" : "I",
    "5" : "J",
    "55" : "K",
    "555" : "L",
    "6" : "M",
    "66" : "N",
    "666" : "O",
    "7" : "P",
    "77" : "Q",
    "777" : "R",
    "7777" : "S",
    "8" : "T",
    "88" : "U",
    "888" : "V",
    "9" : "W",
    "99" : "X",
    "999" : "Y",
    "9999" : "Z"
}

def convert_t9_to_word(code):
    word = ""
    chars = code.split("-")

    for c in chars:
        if c in t9_dict:
            word += t9_dict[c]
        else:
            raise Exception()

    return word

if __name__ == "__main__":
    print(convert_t9_to_word("6-666-88-777-33-3-33-888"))
