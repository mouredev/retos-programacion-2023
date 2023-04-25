# /*
#  * Escribe un programa que reciba un texto y transforme lenguaje natural a
#  * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
#  *  se caracteriza por sustituir caracteres alfanuméricos.
#  * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
#  *   con el alfabeto y los números en "leet".
#  *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
#  */

# Función traductor
def leet_traductor(abecedario):

    dict_leet = {
            "A": "4", "B": "I3", "C": "[", "D": ")", "E": "3",                  # A,B,C,D,E
            "F": "|=", "G": "&", "H": "#", "I": "1", "J": ",_|",                # F,G,H,I,J
            "K": ">|", "L": "1", "M": "/\/\\", "N": " ^/", "Ñ":" error ",       # K,L,M,N,Ñ
            "O": "0", "P": " |*", "Q": "(_,)", "R": "I2", "S": "5", "T": "7",   # P,Q,R,S,T
            "U": "(_)", "V": "\/", "W": "\/\/", "X": "><", "Y": "j", "Z": "2",  # U,V,W,X,Y                                                       
            "1": "L", "2": "R", "3": "E", "4": "A", "5": "S",                   # 1,2,3,4,5
            "6": "b", "7": "T", "8": "B", "9": "g", "0": "o"                    # 6,7,8,9,0
          }                   

    leet_textNuevo = ""

    for letra in abecedario:
        if letra.upper() in dict_leet.keys():               # Transforma en mayus las letras en dict_leet
            leet_textNuevo += dict_leet[letra.upper()]      # Se agrega la equivalencia de letra en mayus
        else:
            leet_textNuevo += letra                         # Si no encuentra, inserta la letra sin traducir

    return leet_textNuevo                                   # Regresa resultado


# print("Leet:",leet_traductor("Leet"))           # 1337
# print(leet_traductor("Niño"))                   # ^/1 error 0
resultado=(leet_traductor(input("Inserta texto a traducir: ")))
print("--------------------------------")
print(resultado)