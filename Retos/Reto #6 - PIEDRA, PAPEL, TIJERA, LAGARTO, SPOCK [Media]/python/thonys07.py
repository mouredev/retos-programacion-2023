"""
* Crea un programa que calcule quien gana más partidas al piedra,
 * papel, tijera, lagarto, spock.
 * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
 * - La función recibe un listado que contiene pares, representando cada jugada.
 * - El par puede contener combinaciones de "piedra" (piedra), "papel" (papel),
 *   "tijera" (tijera), "lagartija" (lagarto) o "spock" (spock).
 * - Ejemplo. Entrada: [("piedra","tijera"), ("tijera","piedra"), ("papel","tijera")]. Resultado: "Player 2".
 * - Debes buscar información sobre cómo se juega con estas 5 posibilidades.
Piedra aplasta tijeras y aplasta lagarto.
Papel cubre piedra y desautoriza Spock.
Tijeras cortan papel y decapitan lagarto.
Lagarto come papel y envenena Spock.
Spock rompe tijeras y vaporiza piedra.


"""


def rock_paper_scissors_spock_lizard(jugador1, jugador2):
   reglas = {
        ("1", "2"): "1 aplasta 2",
        ("1", "4"): "1 aplasta 4",
        ("3", "1"): "3 cubre 1",
        ("3", "5"): "3 desautoriza 5",
        ("2", "3"): "2 corta 3",
        ("2", "4"): "2 decapita 4",
        ("4", "3"): "4 come 3",
        ("4", "5"): "4 envenena 5",
        ("5", "2"): "5 vaporiza 2",
        ("5", "1"): "5 rompe 1"
    }
   
   if jugador1 == jugador2:
        return "Tie"
   elif (jugador1, jugador2) in reglas:
        return "Player 1"
   else:
        return "Player 2"

def calcular_ganador(partidas):
    puntuacion = {"Player 1": 0, "Player 2": 0, "Tie": 0}
    
    for jugador1, jugador2 in partidas:
        resultado = rock_paper_scissors_spock_lizard(jugador1, jugador2)
        puntuacion[resultado] += 1
        print(f"{jugador1} vs {jugador2}: {resultado}, {puntuacion}")
    ganador = max(puntuacion, key=puntuacion.get)
    
    return ganador

def main():
    partidas = []
    while True:
        jugador1 = input("Player 1, enter your move 1: Rock, 2: Paper, 3: Scissors, 4: Lizard, 5: Spock: ")
        if jugador1 == "":
            break
        jugador2 = input("Player 2, enter your move 1: Rock, 2: Paper, 3: Scissors, 4: Lizard, 5: Spock: ")
        if jugador2 == "":
            break
        partidas.append((jugador1, jugador2))
    
    ganador = calcular_ganador(partidas)
    print("The winner is: " + ganador)

main();1

