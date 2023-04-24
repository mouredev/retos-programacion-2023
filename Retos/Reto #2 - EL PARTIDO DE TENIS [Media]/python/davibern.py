'''
  Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
  El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
  gane cada punto del juego.
  
  - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
  - Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
    15 - Love
    30 - Love
    30 - 15
    30 - 30
    40 - 30
    Deuce
    Ventaja P1
    Ha ganado el P1
  - Si quieres, puedes controlar errores en la entrada de datos.   
  - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.   
 '''
 
def comprobar_jugadas(List):
    if all(map(lambda x: x.upper() in ['P1', 'P2'], List)):
        return True
    else:
        return False
 
def tenis(List):
    
    if comprobar_jugadas(List):
        partido = [elem.upper() for elem in List] # Convierte cada elemento a mayúscula
        puntuaciones = ['Love', '15', '30', '40']
        player_1 = 0
        player_2 = 0
        
        for i in partido:
            if i == 'P1': player_1 += 1
            elif i == 'P2': player_2 += 1
            
            if player_1 == 3 and player_2 == 3: print('Deuce')
            
            elif player_1 >= 4 or player_2 >= 4:
                diff = player_1 - player_2
                
                if diff == 0: print('Deuce')
                elif diff == 1: print('Ventaja P1')
                elif diff == -1: print('Ventaja P2')
                elif diff >= 2: print('Ha ganado P1')
                else: print('Ha ganado P2')
                
            else: print(f'{puntuaciones[player_1]} - {puntuaciones[player_2]}')
    else:
        print('Error -> La lista de jugadas debe contener valores tipo P1 o P2')
 
if __name__ == '__main__':
    
    print('Que empiece el partido')
    partido = ['p1', 'P1', 'P2', 'P2', 'p1', 'P2', 'P1', 'p1']
    tenis(partido)    
    