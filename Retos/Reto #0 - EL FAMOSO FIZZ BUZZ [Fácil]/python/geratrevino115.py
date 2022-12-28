# /*
#  * Escribe un programa que muestre por consola (con un print) los
#  * números de 1 a 100 (ambos incluidos y con un salto de línea entre
#  * cada impresión), sustituyendo los siguientes:
#  * - Múltiplos de 3 por la palabra "fizz".
#  * - Múltiplos de 5 por la palabra "buzz".
#  * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
#  */

# #Variables a utilizar 
# num_max = 100
# num_min = 1

# #Ciclo de busqueda
# for i in range(num_min,num_max + 1):

#     #Condicionales si el numero es multiplo de 3 y 5
#     if (i % 3 == 0 and i % 5 == 0):
#         print("fizzbuzz \n")

#     elif (i % 3 == 0):
#         print("fizz \n")

#     elif (i % 5 == 0):
#         print("buzz \n")

#     else:
#         print(i, '\n')

for num in range(1, 101):
  # Inicializamos la cadena que vamos a imprimir
  output = ""
  # Si el número es múltiplo de 3, añadimos "fizz" a la cadena
  if num % 3 == 0:
      output += "fizz"
  # Si el número es múltiplo de 5, añadimos "buzz" a la cadena
  if num % 5 == 0:
      output += "buzz"
  # Si no es múltiplo de ninguno de ellos, añadimos el número a la cadena
  if output == "":
      output += str(num)
  # Imprimimos la cadena y un salto de línea
  print(output)
