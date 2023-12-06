/*
 *
 * En un fichero, haz lo siguiente (si el lenguaje lo soporta),
 * y comenta cada bloque para identificar con qué se corresponde:
 * - Haz un "Hola, mundo!"
 * - Crea variables de tipo String, numéricas (enteras y decimales)
 *   y Booleanas (o cualquier tipo de dato primitivo).
 * - Crea una constante.
 * - Usa un if, else if y else.
 * - Crea estructuras como un array, lista, tupla, set y diccionario.
 * - Usa un for, foreach y un while.
 * - Crea diferentes funciones (con/sin parámetros y con/sin retorno).
 * - Crea una clase.
 * - Muestra el control de excepciones.
 *
 */


// Hola, mundo!
console.log('Hola, mundo!')

// Variable de tipo String
const string = 'Hola, mundo!'
// Variables numéricas (enteras y decimales) 
const number = 123
const decimal = 1.23
// Variable Booleanas
const boleana = true
const boleana2 = false

// Constante 
const constante = 'Hola, mundo!'  // --> No se puede reasignar
let variable = 'Puedo cambiar' // --> Se puede reasignar

// if, else if y else
if (number < 0) {
    console.log('number es negativo')
} else if (number > 0) {
    console.log('number es positivo')
} else {
    console.log('number es 0')
}

// Array
const array = [1, 2, 3, 4, 5]

// Set
const set = new Set([1, 2, 3,'Hola', 'Mundo', true])

// Diccionario
const diccionario = {
    llave: 'valor',
    llave2: 'valor2',
    llave3: 'valor3'
}

// for
for (let i = 0; i < array.length; i++) {
    console.log('En el bucle for: '+array[i])
}
// foreach
array.forEach(element => {
    console.log('En el bucle foreach: '+element)
})
// while
let num = 0
while (num < 5) {
    num++
    console.log('En el bucle while: '+num)
}

// Funciones
// Sin parámetros y sin retorno
function saludar() {
    console.log('Hola, mundo!')
}

// con parámetros y con retorno
function suma(a, b) {
    return a + b
}
// llamar a funciones
saludar() // --> Hola, mundo!
const valorResultante = suma(3, 4)
console.log('Resultado de la suma: '+valorResultante) // --> Resultado de la suma: 7

// Control de excepciones
// Sin error, entra en el try:
try {
    variable = 'Cambiando el valor de la variable let'
    console.log('Nuevo valor de la variable: ' +variable) // --> Nuevo valor de la variable: Cambiando el valor de la variable let
} catch (error) {
    console.log('Error:', error.message)
}

// Error, entra en el catch:
try {
    constante = 'Intentando cambiar una constante.'
    console.log(constante)
} catch (error) {
    console.log('Error:', error.message) // --> Error: Assignment to constant variable
}



