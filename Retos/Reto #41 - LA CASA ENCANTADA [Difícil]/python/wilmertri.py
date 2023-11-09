"""
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
"""
import random


def painting_mansion(r: int, c: int, init: bool, candy: bool, ghost: bool):
    mansion = [
        ['🚪', '⬜️', '⬜️', '⬜️'],
        ['⬜️', '⬜️', '⬜️', '⬜️'],
        ['⬜️', '⬜️', '⬜️', '⬜️'],
        ['⬜️', '⬜️', '⬜️', '⬜️']
    ]

    if init:
        mansion[r][c] = '🙍‍♂️'
    if candy:
        mansion[r][c] = '🍭'
    if ghost:
        mansion[r][c] = '👻'


    for r in mansion:
        print(' '.join(r))

def options_move(r: int, c:int) -> list:
    option = ["arriba", "abajo", "izquierda", "derecha" ]

    if r == 0:
        option = ["abajo"]
    elif r == 3:
        option = ["arriba"]

    if r == 0 or r == 3:
        if c == 0:
            option.append("derecha")
        if 0 < c < 3:
            option += ["izquierda","derecha"]
        if c == 3:
            option.append("izquierda")

    if c == 0:
        option = ["derecha"]
    elif c == 3:
        option = ["izquierda"]

    if c == 0 or c == 3:
        if r == 0:
            option.append("abajo")
        if 0 < r < 3:
            option += ["arriba", "abajo"]
        if r == 3:
            option.append("arriba")

    return option


questions_answers = [
    ('Son doce señoras con medias, pero sin zapatos. ¿De quiénes se trata?', 'las horas'),
    ('Todos pasan preguntando por mí, pero yo ni paso ni pregunto por nadie.', 'la calle'),
    ('Aunque fui por él, no lo traje', 'El camino'),
    ('¿Qué se encuentra entre playa y mar?', 'La letra y'),
    ('Es blanco como la sal y, aunque se puede abrir, no se cierra.', 'el huevo'),
    ('Existe un ser vivo capaz de beber agua con los pies. ¿Cuál es?', 'el arbol'),
    ('Es tuyo, pero todos lo usan más', 'el nombre'),
    ('Cuando lo nombras ya no estará porque desaparece.', 'el silencio'),
    ('¿Qué es lo que se hace de noche, que no se puede hacer de día?', 'trasnochar'),
    ('Va siempre en la sopa, pero nunca se come.', 'la cuchara'),
    ('Tiene un cuadrado de envase, una base redonda y una porción triangular.', 'una pizza'),
    ('Tengo hipo al decir mi nombre, ¿quién soy?', 'el hipopotamo'),
    ('De celda en celda voy, pero presa no estoy.', 'la abeja'),
    ('Tiene cuello, pero no tiene cabeza. ¿Qué es?', 'la botella'),
    ('¿Cuántos meses tienen 28 días?', 'los doce')
]


def game():

    painting_mansion(0,0, False, False, False)
    option = input("Desea iniciar el juego. 1.Si 2.No: ")
    if option.lower() == "si":

        print("----------------\nVamos a Jugar!!!\n----------------")

        row_init, column_init = 0, 0
        row_candy, column_candy = 3, random.randint(0, 3)

        while option.lower() != "salir":

            painting_mansion(row_init, column_init, True, False, False)


            option =  input(f"Ingrese su siguiente movimiento ({'/'.join(options_move(row_init, column_init))}) o salir para terminar el juego: ")

            if option.lower() == "salir":
                print("----------------\nVuelva pronto!!!\n----------------")
                break


            if option.lower() not in options_move(row_init, column_init):
                print("El movimiento no es correcto")
            else:    
                number_questions = 1

                if not (row_init == 0 and column_init == 0):
                    # Genera un número aleatorio entre 0 y 1
                    numero_aleatorio = random.random()
                    # Define una probabilidad del 10%
                    probabilidad = 0.1

                    if numero_aleatorio <= probabilidad:
                        painting_mansion(row_init, column_init, True, False, True)
                        print("Ha aparecido un fantasma tendras que resolver dos enigmas para poder moverte de cuarto!")
                        number_questions = 2

                for i in range(0, number_questions):

                    enigma_choose = random.randint(0, len(questions_answers) - 1)
                    question = questions_answers[enigma_choose][0]
                    answer = questions_answers[enigma_choose][1]

                    win_answer = False

                    while not win_answer:
                        print(f"Tu enigma es: {question}")
                        answer_user = input("Ingresa la respuesta a tu enigma: ")
                        if answer_user.lower() == answer.lower():
                            print("Correcto, resolviste tu enigma")
                            win_answer = True
                        else:
                            print("Incorrecto, sigue intentando")


                if option.lower() == "abajo":
                    row_init += 1
                elif option.lower() == "arriba":
                    row_init -= 1
                elif option.lower() == "derecha":
                    column_init += 1
                elif option.lower() == "izquierda":
                    column_init -= 1

                if column_init == column_candy and row_init == row_candy:
                    print("Has salido de la mansión!")
                    print("----------------\nVuelva pronto!!!\n----------------")
                    painting_mansion(row_init, column_init, True, True, False)
                    break

if __name__ == "__main__":
    game()