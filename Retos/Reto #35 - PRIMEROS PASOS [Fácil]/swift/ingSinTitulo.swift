// Punto 1: Hola, mundo!
print("Hola, mundo!")

// Punto 2: Crea una variable de texto o string
let miTexto = "¡Hola desde Swift!"

// Punto 3: Crea una variable de número entero
let miEntero: Int = 42

// Punto 4: Crea una variable de número con decimales
let miDecimal: Double = 3.14

// Punto 5: Crea una variable de tipo booleano
let miBooleano: Bool = true

// Punto 6: Crea una constante
let miConstante: Int = 10

// Punto 7: Usa un if, else if y else
if miEntero > 50 {
    print("El número es mayor que 50")
} else if miEntero < 50 {
    print("El número es menor que 50")
} else {
    print("El número es igual a 50")
}

// Punto 8: Crea un Array
let miArray = [1, 2, 3, 4, 5]

// Punto 9: Crea una lista (array en Swift)
let miLista = ["Manzana", "Banana", "Naranja"]

// Punto 10: Crea una tupla
let miTupla = (1, "dos", 3.14)

// Punto 11: Crea un set
let miSet: Set<String> = ["Rojo", "Verde", "Azul"]

// Punto 12: Crea un diccionario
let miDiccionario = ["clave1": "valor1", "clave2": "valor2"]

// Punto 13: Usa un ciclo for
for elemento in miArray {
    print(elemento)
}

// Punto 14: Usa un ciclo foreach
for elemento in miLista {
    print(elemento)
}

// Punto 15: Usa un ciclo while
var contador = 0
while contador < 3 {
    print("Contador: \(contador)")
    contador += 1
}

// Punto 16: Crea una función sin parámetros que no retorne nada
func funcionSinParametros() {
    print("Función sin parámetros")
}
funcionSinParametros()

// Punto 17: Crea una función con parámetros que no retorne nada
func funcionConParametros(param1: Int, param2: String) {
    print("Parámetro 1: \(param1)")
    print("Parámetro 2: \(param2)")
}
funcionConParametros(param1: 1, param2: "dos")

// Punto 18: Crea una función con parámetros que retorne valor
func funcionConRetorno(a: Int, b: Int) -> Int {
    return a + b
}
let resultado = funcionConRetorno(a: 3, b: 4)
print("Resultado: \(resultado)")

// Punto 19: Crea una estructura (struct en Swift)
struct Persona {
    var nombre: String
    var edad: Int
}
let persona = Persona(nombre: "Juan", edad: 30)
print("Nombre: \(persona.nombre), Edad: \(persona.edad)")

// Punto 20: Muestra control de excepciones (do-catch en Swift)
do {
    let division = try dividir(dividendo: 10, divisor: 0)
    print("Resultado de la división: \(division)")
} catch {
    print("Error: \(error)")
}

// Punto 20: Muestra control de excepciones (do-catch en Swift)
func dividir(dividendo: Int, divisor: Int) throws -> Int {
    if divisor == 0 {
        throw NSError(domain: "División por cero", code: 0, userInfo: nil)
    }
    return dividendo / divisor
}
