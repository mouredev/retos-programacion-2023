#reto tenis
puntos = (15,30,40)

jugadores = {
    'P1':0,
    'P2':0,
}
resultados = ['P2', 'P2', 'P2', 'P2', 'P2', 'P2', 'P1', 'P1']

flag = False

def get_resultado(secuencia, index):
    jugadores[secuencia] = puntos[index]
    
    if not (jugadores['P1'] == 40 and jugadores['P2'] == 40):
        
        print(f"{'LOVE' if jugadores['P1'] == 0 else jugadores['P1']} - "
              f"{'LOVE' if jugadores['P2'] == 0 else jugadores['P2']} ")
        return True  
    
    else:
        
        if resultados.count('P1') > resultados.count('P2'):
            print('Ventaja P1\nHa ganado el P1')  
        elif resultados.count('P1') == resultados.count('P2'):
            print('Deuce') 
        else:
            print('Ventaja P2\nHa ganado el P2')
        return False
            
            
    
    
for secuencia in resultados:
    match jugadores.get(secuencia):
        case 0:
           flag = get_resultado(secuencia=secuencia, index=0)
        case 15:
           flag = get_resultado(secuencia=secuencia, index=1)
        case 30:
           flag = get_resultado(secuencia=secuencia, index=2)
            

if (resultados.count('P1') > resultados.count('P2')) and flag==True:
    print('Ventaja P1\nHa ganado el P1')
else:
    print('Ventaja P2\nHa ganado el P2')   
                
            