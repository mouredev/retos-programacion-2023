// Punto 1: Hola, mundo!
printfn "Hola, mundo!"

// Punto 2: Crea una variable de texto o string
let miTexto = "¡Hola desde F#!"

// Punto 3: Crea una variable de número entero
let miEntero = 42

// Punto 4: Crea una variable de número con decimales
let miDecimal = 3.14

// Punto 5: Crea una variable de tipo booleano
let miBooleano = true

// Punto 6: Crea una constante
let miConstante = 10

// Punto 7: Usa un if, else if y else
let ejemploIf x =
    if x > 50 then
        "El número es mayor que 50"
    elif x < 50 then
        "El número es menor que 50"
    else
        "El número es igual a 50"

// Punto 8: Crea un Array (array en F#)
let miArray = [|1; 2; 3; 4; 5|]

// Punto 9: Crea una lista (list en F#)
let miLista = ["Manzana"; "Banana"; "Naranja"]

// Punto 10: Crea una tupla
// Las tuplas en F# se definen directamente en su contexto de uso, no como variables independientes

// Punto 11: Crea un set (no aplicable en F#)

// Punto 12: Crea un diccionario (dictionary en F#)
let miDiccionario =
    dict ["clave1", "valor1"; "clave2", "valor2"]

// Punto 13: Usa un ciclo for (no es común en F#, se prefieren funciones de alto orden)
// Punto 14: Usa un ciclo foreach (no es común en F#, se prefieren funciones de alto orden)

// Punto 15: Usa un ciclo while (no es común en F#, se prefieren funciones de alto orden)

// Punto 16: Crea una función sin parámetros que no retorne nada
let funcionSinParametros () =
    printfn "Función sin parámetros"

// Punto 17: Crea una función con parámetros que no retorne nada
let funcionConParametros param1 param2 =
    printfn "Parámetro 1: %d" param1
    printfn "Parámetro 2: %s" param2

// Punto 18: Crea una función con parámetros que retorne valor
let funcionConRetorno a b =
    a + b

// Punto 19: Crea una clase (no hay clases en F#, se usan tipos de registros y módulos)

// Punto 20: Muestra control de excepciones (try-with en F#)
try
    let resultado = miEntero / 0
    printfn "%d" resultado
with
    | :? System.DividedByZeroException as ex ->
        printfn "Error: %s" ex.Message
