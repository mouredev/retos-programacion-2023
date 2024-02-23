import os


# 
# Crea un programa que calcule quien gana más partidas al piedra,
# papel, tijera, lagarto, spock.
# - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
# - La función recibe un listado que contiene pares, representando cada jugada.
# - El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
#   "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
# - Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
# - Debes buscar información sobre cómo se juega con estas 5 posibilidades.
# 

GANA_CONTRA = {
    '🗿': '✂️🦎',
    '📄': '🗿🖖',
    '✂️': '📄🦎',
    '🦎': '📄🖖',
    '🖖': '✂️🗿'
    }

NUMEROS_A_EMOJIS = {'1': '🗿',
                    '2': '📄', 
                    '3': '✂️',
                    '4': '🦎',
                    '5': '🖖'}

def limpiar_pantalla ():
    if os.name == 'nt':  # Sistema Windows
        os.system('cls')
    else:  # Sistemas basados en UNIX (Linux, macOS, etc.)
        os.system('clear')



def hacer_movimiento ():
    print("Qué movimiento desea hacer?")
    print("-"*40)
    for n in NUMEROS_A_EMOJIS:
        print(f"Número {n} para el movimiento {NUMEROS_A_EMOJIS[n]}")
    print("-"*40)
    while True:
        respuesta = input("Seleccione el número deseado: \n")
        if respuesta not in NUMEROS_A_EMOJIS:
            print ("Seleccione un número correcto")
            continue
        else:
            print(f"Genial, tu movimiento seleccionado es el {NUMEROS_A_EMOJIS[respuesta]}")
            break
    return NUMEROS_A_EMOJIS[respuesta]

def juego ():
    print("Es el turno del Jugador 1")
    movimiento_jugador_1 = hacer_movimiento()
    print("="*40)
    print("Ahora es el turno del Jugador 2")
    movimiento_jugador_2 = hacer_movimiento()
    print("="*40)
    print(f"El jugador 1 ha hecho {movimiento_jugador_1}, gana contra {GANA_CONTRA[movimiento_jugador_1]} y el jugador 2 {movimiento_jugador_2} , gana contra {GANA_CONTRA[movimiento_jugador_2]}")
    if movimiento_jugador_2 in GANA_CONTRA[movimiento_jugador_1]:
        print("Gana el jugador 1!")
        resultado = 1
    elif movimiento_jugador_1 in GANA_CONTRA[movimiento_jugador_2]:
        print("Gana el jugador 2!")
        resultado = 2
    else:
        print("Es un empate")
        resultado = 0
    return resultado

def preguntar_si_seguir():
        while True:
            print("Desean jugar otra partida? (s/n)")
            respuesta_seguir = input("")
            if respuesta_seguir.upper() == "S":
                break
            elif respuesta_seguir.upper() == "N":
                exit()
            else:
                print("Seleccione una respuesta correctra")



    
def main():
    limpiar_pantalla()
    print("="*40)
    print("Bienvenidos al juego piedra, papel o tijera, lagarto spock!")
    print("="*40)
    resultados = {'Jugador 1': 0, 'Jugador 2': 0, 'Empates': 0}
    juego_numero = 1
    while True:
        if juego_numero != 1:
            print(f"Los resultados hasta ahora son:")
            print(f"Jugador 1: {resultados['Jugador 1']} - Jugador 2: {resultados['Jugador 2']} - Empates: {resultados['Empates']}")
            preguntar_si_seguir()
            limpiar_pantalla()
        print("*"*40)
        print(f"Este es el juego número {juego_numero}")
        print(f"Jugador 1: {resultados['Jugador 1']} - Jugador 2: {resultados['Jugador 2']} - Empates: {resultados['Empates']}")
        print("*"*40)

        resultado = juego()
        if resultado == 1:
            resultados['Jugador 1'] += 1
            juego_numero += 1
        elif resultado == 2:
            resultados['Jugador 2'] += 1
            juego_numero += 1
        else:
            resultados['Empates'] += 1
            juego_numero += 1


if __name__ == "__main__":
    main()
