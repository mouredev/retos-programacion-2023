# Reto #1: EL "LENGUAJE HACKER"

leet_letters = {
    "a" : "4", "b" : "I3", "c" : "[",  "d" : ")",
    "e" : "3", "f" : "|:", "g" : "6",  "h" : "#",
    "i" : "1", "j" : ",_|", "k" : ">|",  "l" : "1",
    "m" : "[V]", "n" : "^/", "o" : "0",  "p" : "|*",
    "q" : "(_,)", "r" : "I2", "s" : "5",  "t" : "7",
    "u" : "(_)", "v" : "|/", "w" : "(n)",  "x" : "><",
    "y" : "j", "z" : "2"
    }

leet_numbers = {
    "1" : "L", "2" : "R", "3" : "E", "4" : "A", "5" : "S",
    "6" : "b", "7" : "T", "8" : "B", "9" : "g", "0" : "o"
    }

leet_alphabet = leet_letters | leet_numbers

input_text = input("Ingrese un texto: ").lower()
leet_text = ""

for count in range(0, len(input_text)):
    if input_text[count] in leet_alphabet.keys():
        leet_text = leet_text + leet_alphabet.get(input_text[count])
    else:
        leet_text = leet_text + input_text[count]

print(leet_text) 
    