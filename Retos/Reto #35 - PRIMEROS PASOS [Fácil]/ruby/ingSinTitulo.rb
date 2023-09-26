# Punto 1: Hola, mundo!
puts "Hola, mundo!"

# Punto 2: Crea una variable de texto o string
mi_texto = "¡Hola desde Ruby!"

# Punto 3: Crea una variable de número entero
mi_entero = 42

# Punto 4: Crea una variable de número con decimales
mi_decimal = 3.14

# Punto 5: Crea una variable de tipo booleano
mi_booleano = true

# Punto 6: Crea una constante
MI_CONSTANTE = 10

# Punto 7: Usa un if, else if y else
if mi_entero > 50
    puts "El número es mayor que 50"
elsif mi_entero < 50
    puts "El número es menor que 50"
else
    puts "El número es igual a 50"
end

# Punto 8: Crea un Array
mi_array = [1, 2, 3, 4, 5]

# Punto 9: Crea una lista (array en Ruby)
mi_lista = ["Manzana", "Banana", "Naranja"]

# Punto 10: Crea una tupla (no aplicable en Ruby)

# Punto 11: Crea un set (no aplicable en Ruby)

# Punto 12: Crea un diccionario (hash en Ruby)
mi_diccionario = {
    "clave1" => "valor1",
    "clave2" => "valor2"
}

# Punto 13: Usa un ciclo for
mi_array.each do |elemento|
    puts elemento
end

# Punto 14: Usa un ciclo foreach (no aplicable en Ruby)

# Punto 15: Usa un ciclo while
contador = 0
while contador < 3 do
    puts "Contador: #{contador}"
    contador += 1
end

# Punto 16: Crea una función sin parámetros que no retorne nada
def funcion_sin_parametros
    puts "Función sin parámetros"
end
funcion_sin_parametros

# Punto 17: Crea una función con parámetros que no retorne nada
def funcion_con_parametros(param1, param2)
    puts "Parámetro 1: #{param1}"
    puts "Parámetro 2: #{param2}"
end
funcion_con_parametros(1, "dos")

# Punto 18: Crea una función con parámetros que retorne valor
def funcion_con_retorno(a, b)
    return a + b
end
resultado = funcion_con_retorno(3, 4)
puts "Resultado: #{resultado}"

# Punto 19: Crea una clase
class Persona
    attr_accessor :nombre, :edad

    def initialize(nombre, edad)
        @nombre = nombre
        @edad = edad
    end
end

# Punto 20: Muestra control de excepciones (begin-rescue en Ruby)
begin
    division = mi_entero / 0
    puts division
rescue Exception => e
    puts "Error: #{e.message}"
end
