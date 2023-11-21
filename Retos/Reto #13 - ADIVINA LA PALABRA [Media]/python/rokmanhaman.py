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
        
        length = len(self.word)
        bin = ''
        for i in range(length):
            if random.random() < max_zeros:
                bin += self.word[i]
            elif self.word[i] != " ":
                bin += '_'
        return bin

    def guess_word(self):
        ini_sample = self.initial_sample()

        ini_sample_list = list(ini_sample)
        print(f"la palabra a adivinar es: {ini_sample}")
        
        att = self.attemps

        while att > 0:
            l = input("Ingrese una letra: ")

            if l in self.word:
                index = [i for i, c in enumerate(self.word) if c == l]  
                for ind in index:
                    ini_sample_list[ind] = l
                out = ''.join(ini_sample_list)    
                print(f"la palabra a adivinar es: {out}")
            else:
                att = att - 1
                print(f"la letra: {l} no se encuentra en la frase. Le quedan {att} intentos")
            
            if att == 0:
                message = "GAME OVER!!!"
            
            out = ''.join(ini_sample_list) 
                        
            if self.word == out:
                message = "WINNER!!!"
                break

        return print(message)
    

word = Word("hola manola campeon", 5)
#print(word.initial_sample())
word.guess_word()