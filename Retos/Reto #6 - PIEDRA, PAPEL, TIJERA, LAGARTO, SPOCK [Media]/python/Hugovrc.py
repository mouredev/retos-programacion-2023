from enum import Enum 

class Movimiento(Enum):
    PIEDRA = "🗿"
    PAPEL = "📃"
    TIJERA = "✂️"
    LAGARTO = "🐊"
    SPOCK = "🖖"


def piedra_papel_tijera_lagarto_spock(juegos:list[tuple[str,str]]):
    jugador1 = 0
    jugador2 = 0
    
    for game in juegos:
        
        jugador_uno_mov = game[0]
        jugador_dos_mov = game[1]
        
        if jugador_uno_mov != jugador_dos_mov:

            if jugador_uno_mov == "🗿" and jugador_dos_mov == "✂️" or jugador_uno_mov == "✂️" and jugador_dos_mov == "📃" or jugador_uno_mov == "📃" and jugador_dos_mov == "🗿" or jugador_uno_mov == "🗿" and jugador_dos_mov == "🐊" or jugador_uno_mov == "🐊" and jugador_dos_mov == "🖖" or jugador_uno_mov == "🖖" and jugador_dos_mov == "✂️" or jugador_uno_mov == "✂️" and jugador_dos_mov == "🐊" or jugador_uno_mov == "📃" and jugador_dos_mov == "🖖" or jugador_uno_mov == "🐊" and jugador_dos_mov == "📃" or jugador_uno_mov == "🖖" and jugador_dos_mov == "🗿" :
                jugador1 += 1
            else:
                jugador2 += 1

    if jugador1 == jugador2:
        print("Tier")
    elif jugador1 > jugador2:
        print ("Player 1")
    else:
        print ("Player 2")

piedra_papel_tijera_lagarto_spock([("📃", "🗿"),("🐊","🖖"),("🖖","📃"),("🗿","🖖")])
piedra_papel_tijera_lagarto_spock([("🐊","🖖"),("📃","🖖"),("🗿","🖖")])