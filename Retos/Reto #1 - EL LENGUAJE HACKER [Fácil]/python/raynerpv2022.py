 ### Reto #1: EL "LENGUAJE HACKER"” ###

""" https://retosdeprogramacion.com/

 Escribe un programa que reciba un texto y transforme lenguaje natural a
 "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
  se caracteriza por sustituir caracteres alfanuméricos.
 - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
   con el alfabeto y los números en "leet".
   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
"""
leet_dict = {"a": "4", "b": "I3", "c": "[", "d": ")", "e": "3", "f": "|=", "g": "&", "h": "#", "i": "1", "j": ",_|", "k": ">|",
                "l": "1", "m": "/\/\\", "n": "^/", "o": "0", "p": "|*", "q": "(_,)", "r": "|2", "s": "5", "t": "7", "u": "(_)",
                "v": "\/", "w": "\/\/", "x": "><", "y": "j", "z": "2", "1": "L", "2": "R", "3": "E", "4": "A", "5": "S", "6": "b",
                "7": "T", "8": "B", "9": "g", "0": "o"
            }

# using for loop :)
def to_leet(text):
    leet =""
    for i in text:
        leet += leet_dict.get(i,i)
         
    return leet

#  using list comprehension :))
def to_leet_list_com(text:str)-> str:
    return  ''.join([leet_dict.get(x,x) for x in text ])



text = input("Enter text to transform to LEET: \n").lower()
print(to_leet(text))
print(to_leet_list_com(text))
 