'''
La última semana de 2021 comenzamos la actividad de retos de programación,
con la intención de resolver un ejercicio cada semana para mejorar
nuestra lógica... ¡Hemos llegado al EJERCICIO 100! Gracias 🙌
Crea un programa que calcule los puntos de una palabra.
- Cada letra tiene un valor asignado. Por ejemplo, en el abecedario
  español de 27 letras, la A vale 1 y la Z 27.
- El programa muestra el valor de los puntos de cada palabra introducida.
- El programa finaliza si logras introducir una palabra de 100 puntos.
- Puedes usar la terminal para interactuar con el usuario y solicitarle
  cada palabra.
'''

abecedario = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 
              'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 
              'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def calcular_puntuacion(palabra):
    puntuacion = 0
    for s in palabra:
        puntuacion += (abecedario.index(s.upper()) + 1)
    return puntuacion

puntuacion = 0
while puntuacion != 100:
    palabra = input('Introduce una palabra: ')
    puntuacion = calcular_puntuacion(palabra)
    print(f'Puntuación: {puntuacion}')

print('Lo lograste, 100 puntos!! Juego terminado.')