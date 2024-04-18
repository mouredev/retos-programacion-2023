#Reto 31

ejemplo=["O---OOOOOOOO",
 "OOO---OOOOOO",
 "---OOOOOOOOO",
 "OO---OOOOOOO",
 "OOOOOOO---OO",
 "OOOOOOOOO---",
 "---OOOOOOOOO"]
  

def lee_abaco(numero):
    solucion=''
    for elemento in numero:
        elemento=elemento.split('-')
        solucion+=str(len(elemento[0]))
    return int(solucion)

    
print(lee_abaco(ejemplo))