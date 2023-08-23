# Trifuerza Zelda
def dibujar_trifuerza(n):
  # Calculamos el numero de asteriscos en la fila superior de cada triangulo
  fila_mayor = 2 * n - 1
  
  # Dibujamos la parte superior de la Trifuerza
  for i in range(n):
    espacios = " " * (n - i - 1)
    asteriscos = "*" * (2 * i + 1)
    print(espacios + asteriscos)
    
  # Dibujamos la parte inferior de la trifuerza 
  for i in range(n):
    espacios = " " * i
    asteriscos = "*" * (fila_mayor - 2 * i)
    print(espacios + asteriscos)
    
# Pedimos al usuario el numero de filas de los triangulos
num_filas = int(input("Ingrese el numero de filas de los triangulos: "))

# Mostramos la trifuerza con el numero de filas ingresado
dibujar_trifuerza(num_filas)