"""
Crea un programa que calcule quien gana mΓ‘s partidas al piedra, papel, tijera, lagarto, spock.
- El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
- La funciΓ³n recibe un listado que contiene pares, representando cada jugada.
- El par puede contener combinaciones de "πΏ" (piedra), "π" (papel), "βοΈ" (tijera), "π¦" (lagarto) o "π" (spock).
- Ejemplo. Entrada: [("πΏ","βοΈ"), ("βοΈ","πΏ"), ("π","βοΈ")]. Resultado: "Player 2".
POSIBILIDADES DOCUMENTADAS:
 Tijera cortan papel; Papel tapa piedra; Piedra aplasta lagarto; Lagarto envenena Spock; Spock rompe tijera,
 Tijeras decapita lagarto; Lagarto deboda papel; Papel desatoriza Spock; Spock vaporiza piedra y Piedra aplasta tijera
"""
def pptls(lista_pares): #RECIBE una lista de pares.
    combinaciones = {"βοΈ":"π,π¦",
                     "π":"πΏ,π",
                     "πΏ":"βοΈ,π¦",
                     "π¦":"π,π",
                     "π":"βοΈ,πΏ"} #diccionario con combinaciones: para cada clave su vencible
    vulcano=0           #esto no pinta nada, pero inicia easter egg
    partida = [0,0]     #INICIAR partida 0-0
    for i in lista_pares: #recorrenos pares
        if i[0]=="π" or i[1]=="π": vulcano+=1
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
    if vulcano==3:      #si hubiere una partida donde salen 3 o mΓ‘s Spock, se saluda en vulcanianonino.
        print("Larga vida y prosperidad") 
#piedra vs papel, tijera vs lagarto, lagarto vs spock
pptls([("πΏ","π"), ("βοΈ","π¦"), ("π","π¦")])
#papel vs piedra, tijera vs papel, tijera vs piedra (clΓ‘sico)
pptls([("π","πΏ"), ("βοΈ","π"), ("βοΈ","πΏ")])
#pappers, please
pptls([("π","π"), ("π","π"), ("π","π")])
#piedra vs spock, tijera vs spock, spock vs spock => proboca easteregg
pptls([("πΏ","π"), ("βοΈ","π"), ("π","π")])
