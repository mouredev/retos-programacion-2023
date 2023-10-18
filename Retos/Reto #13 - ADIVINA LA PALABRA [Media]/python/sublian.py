"""
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
 * - La palabra debe ocultar de forma aleatoria letras, y nunca puede comenzar ocultando más del 60%
 * - Puedes utilizar las palabras que quieras y el número de intentos que consideres
"""
import random

word =["luis", "angel", "gonzalez","pereira", "python"]
word= random.choice(word)
hidden_letters= int(len(word)*.6)
hidden_position= random.sample(range(len(word)), hidden_letters)

hidden_word=""
for index, letter in enumerate(word) :
    hidden_word += "_" if index in hidden_position else letter
    
attempts = 5
    


while attempts>0:
    print(f"Adivina la palabra: {hidden_word}\nTienes {attempts} intentos.")
    text=input("Introduce una letra o la solucion completa: ")
    
    if len(text)==1:
        new_hidden_word=""
        success=False
        for index, letter in enumerate(word):
            if text==letter and hidden_word[index] =="_":
                new_hidden_word +=text
                success=True
            else:
                new_hidden_word +=hidden_word[index]
        hidden_word=new_hidden_word
        
        if success:
            if word==hidden_word:
                print(f"Has acertado!, la palabra oculta era {word}")                   
                break
            else:
                print("Has acertado la letra") 
            
        else:
            print(f"No has acertado la letra oculta")
            attempts-=1
            
                
    elif len(text)==len(word):
        if text==word:
            print(f"Has acertado la palabra oculta")
            break
        else:
            print(f"No has acertado la palabra oculta")
            attempts-=1
    else:
        print("Texto invalido.")
        attempts-=1
    
if attempts == 0:
    print(f"Has perdido. La palabra oculta era {word}")