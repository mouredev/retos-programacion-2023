"""
Reto #13: ADIVINA LA PALABRA
FÁCIL | Publicación: 27/03/23 | Resolución: 03/04/23
/*
 * Crea un pequeño juego que consista en adivinar palabras en un número máximo de intentos:
 * - El juego comienza proponiendo una palabra aleatoria incompleta
 *   - Por ejemplo "m_ur_d_v", y el número de intentos que le quedan
 * - El usuario puede introducir únicamente una letra o una palabra (de la misma longitud que
 *   la palabra a adivinar)
 *   - Si escribe una letra y acierta, se muestra esa letra en la palabra. Si falla, se resta
 *     uno al número de intentos
 *   - Si escribe una resolución y acierta, finaliza el juego, en caso contrario, se resta uno
 *     al número de intentos
 *   - Si el contador de intentos llega a 0, el jugador pierde
 * - La palabra debe ocultar de forma aleatoria letras, y nunca puede comenzar
 *   ocultando más del 60%
 * - Puedes utilizar las palabras que quieras y el número de intentos que consideres
 */
 """
import math
import random

class Word():

    def __init__(self, word, attemps):
        self.word = word
        self.attemps = attemps


    def initial_sample(self):
        max_zeros = 0.6
        hidden_word = ""
        word_list = self.word.split() 

        for word in word_list:
            for i, letter in enumerate(word):
                if random.random() < max_zeros:
                    hidden_word += word[i]
                else:
                    hidden_word += '_'
            
            hidden_word = hidden_word + " "

        return hidden_word[:-1]

    def guess_word(self):

        
        dict_hidden = {index: character for index, character in enumerate(self.initial_sample())}
        dict_word = {index: character for index, character in enumerate(self.word)}
       
        att = self.attemps

        a = ''.join(dict_hidden.values())
        b = ''.join(dict_word.values())

        while att > 0:

            if list(dict_hidden.values()).count("_") == 0:
                out = "WiNNer!!!"
                break

            else:
                print(f"la palabra a adivinar es: {''.join(dict_hidden.values())}")
                letter = input("Ingrese una letra: ")

                if letter not in dict_word.values():
                    att = att - 1
                    print(f"la letra: {letter} no se encuentra en la frase. Le quedan {att} intentos")
                              
                    """
                    elif dict_hidden == dict_word:
                        out = "WiNNer!!!"
                        break
                    """                                        
                else:
                    indexs = [key for key, value in dict_word.items() if value == letter]
                
                    for index in indexs:
                        dict_hidden[index] = letter

            if att == 0:
                out = "GaMe OvEr!!!"
        
        return print(out)
    
word = Word("hola manola campeon", 5)
#print(word.initial_sample())
word.guess_word()