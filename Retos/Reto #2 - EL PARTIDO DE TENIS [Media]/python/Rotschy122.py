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

from typing import List

def calcular_resultado_juego(lista_puntos: List[str]):
    if any(valor not in ['P1', 'P2'] for valor in lista_puntos):
        return print("Hay valores en la lista que no se pueden procesar")
    indice_valor_p1 = 0
    indice_valor_p2 = 0 
    for ganador_punto in lista_puntos:
        indice_valor_p1, indice_valor_p2 = retornar_valor_punto(indice_valor_p1, indice_valor_p2, ganador_punto)
        if indice_valor_p1 == 5 or indice_valor_p2 == 5: break
    return print('Juego terminado')

def retornar_valor_punto(indice_valor_p1: int, indice_valor_p2: int, valor_punto_jugado: str):    
    if valor_punto_jugado == 'P1': indice_valor_p1 +=1  
    if valor_punto_jugado == 'P2': indice_valor_p2 +=1
    #Control
    if indice_valor_p1 != 4 and indice_valor_p2 != 4:
        if indice_valor_p1 == 4 and indice_valor_p2 < 4: indice_valor_p1 = 5
        if indice_valor_p2 == 4 and indice_valor_p1 < 4: indice_valor_p2 = 5
    if indice_valor_p1 == 5 and indice_valor_p2 == 4 and valor_punto_jugado == 'P2': indice_valor_p1 = 4
    if indice_valor_p2 == 5 and indice_valor_p1 == 4 and valor_punto_jugado == 'P1': indice_valor_p2 = 4
    #Si alguno ya gano y el otro no, pongo en 
    if (indice_valor_p1 == 4 and indice_valor_p2 < 3): indice_valor_p1 = 5
    if (indice_valor_p2 == 4 and indice_valor_p1 < 3): indice_valor_p2 = 5
    #Si alguno estaba en ventaja y gana el contrario, pongo en deuce ambos
    if indice_valor_p1 == 4 and indice_valor_p2 == 4:
        indice_valor_p1 = 3
        indice_valor_p2 = 3

    imprimir_valores(indice_valor_p1, indice_valor_p2, valor_punto_jugado)
    return indice_valor_p1, indice_valor_p2

def imprimir_valores(indice_valor_p1: int, indice_valor_p2: int, valor_punto_jugado:int):
    lista_posibles_valores = ['Love', '15', '30', '40', 'Deuce', 'Ventaja ', 'Ha ganado el ']
    #print(str(indice_valor_p1) + ' - ' + str(indice_valor_p2))
    if indice_valor_p1 == 3 and indice_valor_p2 == 3: print(lista_posibles_valores[4])
    elif indice_valor_p1 == 4 or indice_valor_p2 == 4: print(lista_posibles_valores[5] + valor_punto_jugado)
    elif indice_valor_p1 == 5 or indice_valor_p2 == 5: print(lista_posibles_valores[6] + valor_punto_jugado)
    else: print(lista_posibles_valores[indice_valor_p1] + ' - ' + lista_posibles_valores[indice_valor_p2])


listas_a_procesar = [
 ['P1', 'P1', 'P2', 'P1', 'P1'],
 ['P1', 'P1', 'P2', 'P2', 'P1', 'P2', 'P1', 'P1'],
 ['P1', 'P1', 'P1', 'P1', 'P1', 'P1', 'P1', 'P1'],
 ['P2', 'P2', 'P2', 'P2', 'P2', 'P2', 'P2'],
 ['P1', 'P1', 'P1', 'P2', 'P1', 'P1', 'P1', 'P1'],
 ['P1', 'P1', 'P1', 'P2', 'P2', 'P2', 'P2', 'P2'],
 ['P1', 'P1', 'P1', 'P2', 'P2', 'P2', 'P2', 'P1', 'P2', 'P2'],
 ['P1', 'P1', 'P1', 'P2', 'P2', 'P2', 'P2', 'P1', 'P2', 'P1', 'P1', 'P1']]
for lista_a_procesar in listas_a_procesar:
    calcular_resultado_juego(lista_a_procesar)
    print ('--------------------------------------------')