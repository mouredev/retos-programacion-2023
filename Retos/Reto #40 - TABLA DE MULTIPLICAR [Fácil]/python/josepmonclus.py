'''
Crea un programa que sea capaz de solicitarte un número y se
encargue de imprimir su tabla de multiplicar entre el 1 y el 10.
- Debe visualizarse qué operación se realiza y su resultado.
  Ej: 1 x 1 = 1
      1 x 2 = 2
      1 x 3 = 3
      ... 
'''

def tabla_multiplicar(n):
    for i in range(1, 11):
        print(n, 'x', i, '=', n * i)

print('Tabla de multiplicar del 5')
tabla_multiplicar(5)

print('Tabla de multiplicar del 11')
tabla_multiplicar(11)

print('Tabla de multiplicar del 439')
tabla_multiplicar(439)