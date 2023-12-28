"""
  Escribe un programa que reciba un texto y transforme lenguaje natural a
  "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
   se caracteriza por sustituir caracteres alfanuméricos.
  - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
    con el alfabeto y los números en "leet".
    (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
"""

# Create a leet dictionary
dic = {
        'a': '4', 'b': 'l3', 'c': '[', 'd': ')',
        'e': '3', 'f': '|=', 'g': '&', 'h': 'h',
        'i': '1', 'j': ',_|', 'k': '>|', 'l': '1',
        'm': '[V]', 'n': '|\|', 'o': '0', 'p': '|*',
        'q': '(_,)', 'r': 'I2', 's': '5', 't': '7',
        'u': '(_)', 'v': '|/', 'w': 'VV', 'x': '><',
        'y': 'j', 'z': '2', ' ': ' '
}

# Create the message
msg = input('Hi dear, write your message: ')
msg_lower = msg.lower()
# Create to list
cmsg = list(msg_lower)
# Empty list
newMsg = []

def traductor():
    # Write letter a letter
    for i in range(len(cmsg)):
        if cmsg[i] in dic:
            newMsg.append(dic[cmsg[i]])
            # print(cmsg[i] + " = " + str(dic[cmsg[i]]))
    return newMsg 


# Function convert List to String

def listToString(s):
   
    # initialize an empty string
    str1 = " "
   
    # return string 
    return (str1.join(s))


if __name__ == '__main__':
    print(listToString(traductor()))
   
