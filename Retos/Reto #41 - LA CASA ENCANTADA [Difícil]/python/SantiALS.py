"""
/*
 * Este es un reto especial por Halloween.
 * Te encuentras explorando una mansión abandonada llena de habitaciones.
 * En cada habitación tendrás que resolver un acertijo para poder avanzar a la siguiente.
 * Tu misión es encontrar la habitación de los dulces.
 *
 * Se trata de implementar un juego interactivo de preguntas y respuestas por terminal.
 * (Tienes total libertad para ser creativo con los textos)
 *
 * - 🏰 Casa: La mansión se corresponde con una estructura cuadrada 4 x 4
 *   que deberás modelar. Las habitaciones de puerta y dulces no tienen enigma.
 *   (16 habitaciones, siendo una de entrada y otra donde están los dulces)
 *   Esta podría ser una representación:
 *   🚪⬜️⬜️⬜️
 *   ⬜️👻⬜️⬜️
 *   ⬜️⬜️⬜️👻
 *   ⬜️⬜️🍭⬜️
 * - ❓ Enigmas: Cada habitación propone un enigma aleatorio que deberás responder con texto.
 *   Si no lo aciertas no podrás desplazarte.
 * - 🧭 Movimiento: Si resuelves el enigma se te preguntará a donde quieres desplazarte.
 *   (Ejemplo: norte/sur/este/oeste. Sólo deben proporcionarse las opciones posibles)
 * - 🍭 Salida: Sales de la casa si encuentras la habitación de los dulces.
 * - 👻 (Bonus) Fantasmas: Existe un 10% de que en una habitación aparezca un fantasma y
 *   tengas que responder dos preguntas para salir de ella.
 */

"""

import random, os

def board():

    window = [['⬜️'] * 4 for _ in range(4)]
    window[0][0] = '🚪'

    return window

def print_screen(screen: list):

    for i in range(len(screen)):
        print(''.join(screen[i]))

def riddles():
     
    questions_list =[ 
                 'Tengo cabeza redonda, sin nariz, ojos, ni frente, y mi cuerpo se compone tan solo de blancos dientes.',
                 'Salgo de la habitación y entro en la cocina meneando la cola como una gallina.',
                 'Ya se fue el verano y otra estación llega: como lluvia de oro caen hojas secas.',
                 '¿Qué cosa es, que cuanto más intensa se hace menos se ve?',
                 'Una dama muy delgada y de palidez mortal, que se alegra y se reanima cuando la van a quemar.',
                 '¿Cuál es la cosa que cruda no existe, ni puede ser, pero que si está abrasada no se la puede comer?',
                 'Duros como las piedras, para el perro un buen manjar, y sin ellos no podrías ni saltar ni caminar.',
                 'Luna plateada muy bien afilada: de día trabajas y de noche descansas.',
                 'Casa con dos cuartos, nueva cada mes y otras veces llena: adivina quién es.',
                 'Tengo alas negras como la noche, y mi graznido es tan espeluznante como mi aspecto. Me encanta acechar en los tejados y los árboles. ¿Qué soy?',
                 'Vestido de blanco, con una vieja sábana, aparecerá de noche. ¡Cuidado con el …! ',
                 '¿Qué cosa es que cuanto más le quitas más grande es?',
                 'No muerde ni ladra, pero tiene dientes y la casa guarda. ¿Qué es?',
                 'Uno larguito, dos más bajitos, otro chico y flaco, y otro gordonazo.',
                 'Grande, muy grande, mayor que la Tierra. Arde y no se quema, quema y no es candela.',
                 'Entre pared y pared hay una sonora mujer, que con el diente llama a la gente.',
                 '¿Quién será la desvelada, lo puedes tú discurbrir, de día y noche acostada, sin poder nunca dormir?',
                 'Si lo tengo, no lo comparto. Si lo comparto, no lo tengo. ¿Qué es?',
                 '¿En qué lugar encuentras el jueves antes que el miércoles?',
                 'Es tan delicado que se rompe con mencionarlo.',
                 'Estoy entre cielo y tierra. ¿Qué soy?'
                ]

    answers_list =[
                'AJO',
                'ESCOBA',
                'OTOÑO',
                'OSCURIDAD',
                'VELA',
                'CENIZAS',
                'HUESOS',
                'HOZ',
                'LUNA',
                'CUERVO',
                'FANTASMA',
                'AGUJERO',
                'LLAVE',
                'DEDOS',
                'SOL',
                'CAMPANA',
                'CAMA',
                'SECRETO',
                'DICCIONARIO',
                'SILENCIO',
                'Y'
                ]

    question = random.randint(0,20)
    print(f'\nPREGUNTA:\n {questions_list[question]}')
    answer = input('\nRespuesta: ').upper()
    
    if  answer == answers_list[question]:

        print('CORRECTO!\n')
        return False
    
    elif answer == 'ESC':

        return 'break'
    
    else:

        print('INCORRECTO!')
        return True

def message():
    print('''BIENVENIDO AL DESAFÍO DE HALLOWEEN!\n 
Te encuentras explorando una mansión abandonada llena de habitaciones. En cada habitación tendrás que resolver un acertijo para 
poder avanzar a la siguiente.\n
Tu misión es encontrar la habitación de los dulces. Para poder moverte deberás responder correctamente los enigmas con "UNA SOLA
PALABRA". Partirás de la habitación en la posición [0,0] (Puerta).\n
CUIDADO! Si te encuentras con un fantasma en la habitación deberás responder correctamente 2 acertijos para poder avanzar.\n
Debes recordar en qué casillero te encuentras, en caso de olvidarte digita "Room" para conocer tu habitación. Comienzas en la puerta.\n
Para salir del juego digite "Esc".
          ''')

def movement(last_position: list):
    
    while True:

        position = last_position.copy()

        if last_position[0] == 0 and last_position[1] == 0 :
            print('Elija una de las direcciones posibles: SUR[🡣] | ESTE [🡢]')
        elif last_position[0] == 3 and last_position[1] == 3:
            print('Elija una de las direcciones posibles: NORTE[🡡] | OESTE [🡠]')
        elif last_position[0] == 3 and last_position[1] == 0:
            print('Elija una de las direcciones posibles: NORTE[🡡] | ESTE [🡢]')
        elif last_position[0] == 0 and last_position[1] == 3:
            print('Elija una de las direcciones posibles: SUR[🡣] | OESTE [🡠]')
        elif 0< last_position[0] <3 and last_position[1] == 0:
            print('Elija una de las direcciones posibles: NORTE[🡡] | SUR[🡣] | ESTE [🡢]')
        elif 0< last_position[0] <3 and last_position[1] == 3:
            print('Elija una de las direcciones posibles: NORTE[🡡] | SUR[🡣] | OESTE [🡠]')
        elif 0< last_position[1] <3 and last_position[0] == 0:
            print('Elija una de las direcciones posibles: SUR[🡣] | ESTE [🡢] | OESTE [🡠]')
        elif 0< last_position[1] <3 and last_position[0] == 3:
            print('Elija una de las direcciones posibles: NORTE[🡡] | ESTE [🡢] | OESTE [🡠]')
        else:
            print('Elija una de las direcciones posibles: NORTE[🡡] | SUR[🡣] | ESTE [🡢] | OESTE [🡠]')    
        
        event = input().upper()

        if event == 'ESC':
            position = 'esc'
            break
        elif event == 'ROOM':
            print(f'\nTe encuentras en la habitación: {position}\n')
        else :

            if event == 'SUR':
                position[0] += 1            
            
            elif event == 'ESTE':
                position[1] += 1            
            
            elif event == 'OESTE':
                position[1] -= 1             
            
            elif event == 'NORTE':
                position[0] -= 1         
            
        if position[0] < 0 or position[0] >3 or position[1] < 0 or position[1] >3:
            print('\nMovimiento inválido. Por favor ingrese un nuevo movimiento.')
        elif event == 'ROOM':
            pass
        else:
            break            

    return position

def probability() -> bool:
    
    roll_dice = random.randint(1,10)

    if roll_dice == 1:
        doble_answer = True
        print('CUIDADO CON EL FANTASMA!Debes responder 2 preguntas correctas.')
    else:
        doble_answer = False

    return doble_answer


def main():

    os.system('cls')
    message()
    print_screen(board())

    last_position = [0,0]
    new_position = movement(last_position)

    while True:

        if new_position == [2,1]:
            print('FELICIDADES! Encontraste la habitación con los dulces')
            break
    
        elif new_position == 'esc':
            print('Saliste del juego.')
            break

        doble_answer = probability()
        blok_movement = riddles()

        while blok_movement == True or doble_answer == True:

            if blok_movement == False and doble_answer == True:
                while doble_answer == True:
                    print('CUIDADO CON EL FANTASMA!Debes responder 1 pregunta correcta más.')
                    blok_movement = riddles()
                    if blok_movement == False:
                        doble_answer = False

                break
            
            if blok_movement == 'break':
                break

            blok_movement = riddles()
        
        print_screen(board())
        new_position = movement(new_position)




if __name__ == '__main__':
    main()