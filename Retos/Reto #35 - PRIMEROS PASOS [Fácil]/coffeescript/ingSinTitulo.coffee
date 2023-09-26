# Punto 1: Hola, mundo!
console.log "Hola, mundo!"

# Punto 2: Crea una variable de texto o string
miTexto = "¡Hola desde CoffeeScript!"

# Punto 3: Crea una variable de número entero
miEntero = 42

# Punto 4: Crea una variable de número con decimales
miDecimal = 3.14

# Punto 5: Crea una variable de tipo booleano
miBooleano = true

# Punto 6: Crea una constante (no hay constantes en CoffeeScript)

# Punto 7: Usa un if, else if y else
if miEntero > 50
  console.log "El número es mayor que 50"
else if miEntero < 50
  console.log "El número es menor que 50"
else
  console.log "El número es igual a 50"

# Punto 8: Crea un Array (arreglo en CoffeeScript)
miArray = [1, 2, 3, 4, 5]

# Punto 9: Crea una lista (arreglo en CoffeeScript)
miLista = ["Manzana", "Banana", "Naranja"]

# Punto 10: Crea una tupla (no aplicable en CoffeeScript)

# Punto 11: Crea un set (no aplicable en CoffeeScript)

# Punto 12: Crea un diccionario (objeto en CoffeeScript)
miDiccionario =
  clave1: "valor1"
  clave2: "valor2"

# Punto 13: Usa un ciclo for
for elemento in miArray
  console.log elemento

# Punto 14: Usa un ciclo foreach (no aplicable en CoffeeScript)

# Punto 15: Usa un ciclo while
contador = 0
while contador < 3
  console.log "Contador: #{contador}"
  contador++

# Punto 16: Crea una función sin parámetros que no retorne nada
funcionSinParametros = ->
  console.log "Función sin parámetros"
funcionSinParametros()

# Punto 17: Crea una función con parámetros que no retorne nada
funcionConParametros = (param1, param2) ->
  console.log "Parámetro 1: #{param1}"
  console.log "Parámetro 2: #{param2}"
funcionConParametros 1, "dos"

# Punto 18: Crea una función con parámetros que retorne valor
funcionConRetorno = (a, b) ->
  a + b
resultado = funcionConRetorno 3, 4
console.log "Resultado: #{resultado}"

# Punto 19: Crea una clase (no hay clases en CoffeeScript)

# Punto 20: Muestra control de excepciones (try-catch en CoffeeScript)
try
  division = miEntero / 0
  console.log "Resultado de la división: #{division}"
catch error
  console.log "Error: #{error}"
