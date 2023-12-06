-- Hola Mundo
print("Hola, Mundo!")

-- Variable tipo String
nombre = "Solobino"

-- Variable numerica entera
edad = 9

-- Variable numerica decimal
peso = 13.5

-- variable booleana
perro = true

-- Uso de if, else if, y else
if edad <= 2 then
    print("Cachorro")
elseif edad > 2 and edad < 10 then
    print("perro adulto")
else 
    print("perro viejito")
end

-- creacion de un Array, en realidad les llaman tablas en lua que parecen diccionarios
mi_array = {"lua", "python", "C#", "Java"}

-- La sentencia for
for llave, valor in ipairs(mi_array)
do 
    print(valor)
end

-- La sentencia While
a = 1
print(#mi_array)
while(a <= #mi_array)
do
    print(mi_array[a])
    a = a + 1
end

-- Funcion sin parametros
function hola_mundo()
    print("Hola, Mundo!")
end

-- Funcion con parametros
function suma(numero1, numero2)
    print(numero1 + numero2)
end

-- Funcion sin parametros y retorno
function saludo()
    return "Hola"
end

-- Funcion con parametros y retorno
function multiplicacion(num1, num2)
    return num1 * num2
end

-- implementacion de una Clase (en realidad se simula por  que no existe como tal)
-- Definicion de la Clase
Auto = {}
Auto.__index = Auto

-- Constructor de la Clase
function Auto.new(marca, anio)
    local self = setmetatable({}, Auto)
    self.marca = marca
    self.anio = anio
    return self
end

