'''
Reto #6: PIEDRA, PAPEL, TIJERA, LAGARTO, SPOCK

Dificultad: MEDIA

Crea un programa que calcule quien gana mΓ‘s partidas al piedra,
papel, tijera, lagarto, spock.
- El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
- La funciΓ³n recibe un listado que contiene pares, representando cada jugada.
- El par puede contener combinaciones de "πΏ" (piedra), "π" (papel),
  "βοΈ" (tijera), "π¦" (lagarto) o "π" (spock).
- Ejemplo. Entrada: [("πΏ","βοΈ"), ("βοΈ","πΏ"), ("π","βοΈ")]. Resultado: "Player 2".
- Debes buscar informaciΓ³n sobre cΓ³mo se juega con estas 5 posibilidades.
'''

def calcular_ganador(player1, player2):
    if player1 == "πΏ":
        if player2 == "πΏ":
            return "Tie"
        elif player2 == "π":
            return "Player 2"
        elif player2 == "βοΈ":
            return "Player 1"
        elif player2 == "π¦":
            return "Player 1"
        elif player2 == "π":
            return "Player 2"
    elif player1 == "π":
        if player2 == "πΏ":
            return "Player 1"
        elif player2 == "π":
            return "Tie"
        elif player2 == "βοΈ":
            return "Player 2"
        elif player2 == "π¦":
            return "Player 2"
        elif player2 == "π":
            return "Player 1"
    elif player1 == "βοΈ":
        if player2 == "πΏ":
            return "Player 2"
        elif player2 == "π":
            return "Player 1"
        elif player2 == "βοΈ":
            return "Tie"
        elif player2 == "π¦":
            return "Player 1"
        elif player2 == "π":
            return "Player 2"
    elif player1 == "π¦":
        if player2 == "πΏ":
            return "Player 2"
        elif player2 == "π":
            return "Player 1"
        elif player2 == "βοΈ":
            return "Player 2"
        elif player2 == "π¦":
            return "Tie"
        elif player2 == "π":
            return "Player 1"
    elif player1 == "π":
        if player2 == "πΏ":
            return "Player 1"
        elif player2 == "π":
            return "Player 2"
        elif player2 == "βοΈ":
            return "Player 1"
        elif player2 == "π¦":
            return "Player 2"
        elif player2 == "π":
            return "Tie"


# Test
print(calcular_ganador("πΏ","βοΈ"))
print(calcular_ganador("βοΈ","πΏ"))
print(calcular_ganador("π","βοΈ"))
print(calcular_ganador("π","π¦"))
print(calcular_ganador("π¦","πΏ"))
