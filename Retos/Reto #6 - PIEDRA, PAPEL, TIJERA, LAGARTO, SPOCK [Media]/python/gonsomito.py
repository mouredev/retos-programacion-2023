"""
Crea un programa que calcule quien gana más partidas al piedra, papel, tijera, lagarto, spock.
- El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
- La función recibe un listado que contiene pares, representando cada jugada.
- El par puede contener combinaciones de "🗿" (piedra), "📄" (papel), "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
- Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
POSIBILIDADES DOCUMENTADAS:
 Tijera cortan papel; Papel tapa piedra; Piedra aplasta lagarto; Lagarto envenena Spock; Spock rompe tijera,
 Tijeras decapita lagarto; Lagarto deboda papel; Papel desatoriza Spock; Spock vaporiza piedra y Piedra aplasta tijera
"""
def pptls(lista_pares): #RECIBE una lista de pares.
    combinaciones = {"✂️":"📄,🦎",
                     "📄":"🗿,🖖",
                     "🗿":"✂️,🦎",
                     "🦎":"📄,🖖",
                     "🖖":"✂️,🗿"} #diccionario con combinaciones: para cada clave su vencible
    vulcano=0           #esto no pinta nada, pero inicia easter egg
    partida = [0,0]     #INICIAR partida 0-0
    for i in lista_pares: #recorrenos pares
        if i[0]=="🖖" or i[1]=="🖖": vulcano+=1
        if i[0] in combinaciones[i[1]]:
            partida[1] = partida[1] + 1
        elif i[1] in combinaciones[i[0]]:
            partida[0] = partida[0] + 1
    #print(partida)     #para ver el resultado de la partida
    if partida[0] > partida[1]:
        print("Player 1")
    elif partida[0] < partida[1]:
        print("Player 2")
    else:
        print ("Tie")
    if vulcano==3:      #si hubiere una partida donde salen 3 o más Spock, se saluda en vulcanianonino.
        print("Larga vida y prosperidad") 
#piedra vs papel, tijera vs lagarto, lagarto vs spock
pptls([("🗿","📄"), ("✂️","🦎"), ("🖖","🦎")])
#papel vs piedra, tijera vs papel, tijera vs piedra (clásico)
pptls([("📄","🗿"), ("✂️","📄"), ("✂️","🗿")])
#pappers, please
pptls([("📄","📄"), ("📄","📄"), ("📄","📄")])
#piedra vs spock, tijera vs spock, spock vs spock => proboca easteregg
pptls([("🗿","🖖"), ("✂️","🖖"), ("🖖","🖖")])
