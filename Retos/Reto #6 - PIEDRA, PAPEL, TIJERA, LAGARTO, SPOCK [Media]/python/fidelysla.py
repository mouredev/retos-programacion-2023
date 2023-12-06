import random
import os
import time

"""
   Crea un programa que calcule quien gana más partidas al piedra,
   papel, tijera, lagarto, spock.
   - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
   - La función recibe un listado que contiene pares, representando cada jugada.
   - El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
     "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
   - Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
   - Debes buscar información sobre cómo se juega con estas 5 posibilidades.
"""
# * UTILIZO RANDOM.CHOICE() PARA GENERARA ALEATORIAMENTE ENTRADAS DE EMOJIS!!


def gene():
    db = ["\U0001F596", "\U0001f98e", "\u2702\uFE0F", "\U0001F4C4", "\U0001F5FF"]
    fp = random.choice(db)
    sp = random.choice(db)
    return fp, sp


def comb():
    f = "PLAYER 1"
    s = "PLAYER 2"
    contadorfp = 0
    contadorsp = 0
    n = 5
    salir = 0
    while salir == 0:
        for i in range(n):
            time.sleep(1)
            print("*"*15)
            a, b = gene()
            print(f"{f}: {a}")
            print(f"{s}: {b}")
            if a == "\U0001F5FF" and b == "\u2702\uFE0F":
                contadorfp += 1
            if b == "\U0001F5FF" and a == "\u2702\uFE0F":
                contadorsp += 1
            if a == "\u2702\uFE0F" and b == "\U0001F4C4":
                contadorfp += 1
            if b == "\u2702\uFE0F" and a == "\U0001F4C4":
                contadorsp += 1
            if a == "\U0001F4C4" and b == "\U0001F5FF":
                contadorfp += 1
            if b == "\U0001F4C4" and a == "\U0001F5FF":
                contadorsp += 1
            if a == "\U0001F5FF" and b == "\U0001f98e":
                contadorfp += 1
            if b == "\U0001F5FF" and a == "\U0001f98e":
                contadorsp += 1
            if a == "\U0001f98e" and b == "\U0001F596":
                contadorfp += 1
            if b == "\U0001f98e" and a == "\U0001F596":
                contadorsp += 1
            if a == "\U0001F596" and b == "\u2702\uFE0F":
                contadorfp += 1
            if b == "\U0001F596" and a == "\u2702\uFE0F":
                contadorsp += 1
            if a == "\u2702\uFE0F" and b == "\U0001f98e":
                contadorfp += 1
            if b == "\u2702\uFE0F" and a == "\U0001f98e":
                contadorsp += 1
            if a == "\U0001f98e" and b == "\U0001F4C4":
                contadorfp += 1
            if b == "\U0001f98e" and a == "\U0001F4C4":
                contadorsp += 1
            if a == "\U0001F4C4" and b == "\U0001F596":
                contadorfp += 1
            if b == "\U0001F4C4" and a == "\U0001F596":
                contadorsp += 1
            if a == "\U0001F596" and b == "\U0001F5FF":
                contadorfp += 1
            if b == "\U0001F596" and a == "\U0001F5FF":
                contadorsp += 1

        if contadorfp > contadorsp:
            print("*"*15)
            print(f"""GANADOR {f}""")
            salir = 1
        elif contadorfp < contadorsp:
            print("*"*15)
            print(f"""GANADOR {s}""")
            salir = 1
        elif contadorsp == contadorsp:
            print("*"*15)
            print(f"---EMPATE!!---")
            salir = 0
            n = 1


def main():
    os.system("cls")
    print(f"""JUEGO: PIEDRA, PAPEL, TIJERA, LAGARTO Y SPOCK""")
    comb()


if __name__ == "__main__":
    main()
