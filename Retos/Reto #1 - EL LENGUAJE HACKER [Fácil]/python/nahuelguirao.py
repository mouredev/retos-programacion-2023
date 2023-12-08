def leet_text(text):
    letters = {
        "a" : "4", "b" : "I3", "c" : "[", "d" : ")", "e" : "3", "f" : "|=", "g" : "&", "h" : "&", "i" : "1", "j" : ",_|", "k" : ">|", "l" : "1", "m" : "/\/\.", "n" : "^/", "o" : "0", "p" : "|*", "q" : "(_,)", "r" : "I2", "s" : "5", "t" : "7", "u" : "(_)", "v" : "\/", "w" : "\/\/", "x" : "><", "y" : "j", "z" : "2"
    }
    new_text = text
    for letter in text:
        if letter in letters:
            new_modification = new_text.replace(letter, letters[letter])
            new_text = new_modification
    print(new_text)

leet_text("Buenas tardes, ¿Cómo estas?")