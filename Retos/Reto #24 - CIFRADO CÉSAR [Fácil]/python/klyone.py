#!/usr/bin/env python3

alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def are_arguments_valid(text, n):
    if n == 0 or abs(n) >= len(alphabet):
        return False
    else:
        return True

def prepare_text(text):
    return text.upper()

def translate_text(text, jumps):
    translate = ""

    for t in text:
        if t in alphabet:
            pos = alphabet.find(t)
            pos = (pos + jumps) % len(alphabet)
            t = alphabet[pos]

        translate += t
    return translate

def encode_cesar(text, n):
    if not are_arguments_valid(text, n):
        return text

    text = prepare_text(text)
    return translate_text(text, n)

def decode_cesar(text, n):
    return encode_cesar(text, -n)

if __name__ == "__main__":
    print(encode_cesar("HELLO WORLD", 2))
    print(decode_cesar(encode_cesar("NICE ONE", 5), 5))
    print(encode_cesar("ThiS Is A WonderFULl PLaCE", 17))
