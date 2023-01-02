"""
Escribe un programa que muestre por consola (con un print) los
números de 1 a 100 (ambos incluidos y con un salto de línea entre
cada impresión), sustituyendo los siguientes:
- Múltiplos de 3 por la palabra "fizz".
- Múltiplos de 5 por la palabra "buzz".
- Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
"""
for num in range(1, 101):
  # Inicializamos la cadena que vamos a imprimir
  resul = ""
  # Si el número es múltiplo de 3, añadimos "fizz" a la cadena
  if num % 3 == 0:
      resul += "fizz"
  # Si el número es múltiplo de 5, añadimos "buzz" a la cadena
  if num % 5 == 0:
      resul += "buzz"
  # Si no es múltiplo de ninguno de ellos, añadimos el número a la cadena
  if resul == "":
      resul += str(num)
  # Imprimimos la cadena y un salto de línea
  print(resul)
