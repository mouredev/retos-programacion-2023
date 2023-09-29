-- Punto 1: Hola, mundo!
print("Hola, mundo!")

-- Punto 2: Crea una variable de texto o string
miTexto = "¡Hola desde Lua!"

-- Punto 3: Crea una variable de número entero
miEntero = 42

-- Punto 4: Crea una variable de número con decimales
miDecimal = 3.14

-- Punto 5: Crea una variable de tipo booleano
miBooleano = true

-- Punto 6: Crea una constante (no es común en Lua, se usa convención)
MI_CONSTANTE = 10

-- Punto 7: Usa un if, else if y else
function ejemploIf(x)
    if x > 50 then
        print("El número es mayor que 50")
    elseif x < 50 then
        print("El número es menor que 50")
    else
        print("El número es igual a 50")
    end
end

-- Punto 8: Crea un Array (no aplicable en Lua)

-- Punto 9: Crea una lista (no aplicable en Lua)

-- Punto 10: Crea una tupla (no aplicable en Lua)

-- Punto 11: Crea un set (no aplicable en Lua)

-- Punto 12: Crea un diccionario (no aplicable en Lua)

-- Punto 13: Usa un ciclo for
for i = 1, 5 do
    print(i)
end

-- Punto 14: Usa un ciclo foreach (no aplicable en Lua)

-- Punto 15: Usa un ciclo while
contador = 0
while contador < 3 do
    print("Contador:", contador)
    contador = contador + 1
end

-- Punto 16: Crea una función sin parámetros que no retorne nada
function funcionSinParametros()
    print("Función sin parámetros")
end

-- Punto 17: Crea una función con parámetros que no retorne nada
function funcionConParametros(param1, param2)
    print("Parámetro 1:", param1)
    print("Parámetro 2:", param2)
end

-- Punto 18: Crea una función con parámetros que retorne valor
function funcionConRetorno(a, b)
    return a + b
end

-- Punto 19: Crea una clase (no hay clases en Lua, se usan tablas y metatables)

-- Punto 20: Muestra control de excepciones (no es común en Lua, se usa pcall para capturar errores)
