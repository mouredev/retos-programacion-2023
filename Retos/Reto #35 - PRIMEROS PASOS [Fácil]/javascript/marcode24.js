/*
 * Como cada año, el día 256 se celebra el "Día de la Programación".
 * En nuestra comunidad siempre hacemos una gran fiesta donde repartirmos 
 * 256 regalos para seguir aprendiendo programación:
 * https://diadelaprogramacion.com
 *
 * Para seguir ayudando, te propongo este reto:
 * Mostrar la sintaxis de los principales elementos de un lenguaje
 * en TODOS los lenguajes de programación que podamos. ¿Llegaremos a 50?
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
 * Así, cualquier persona podrá consultar rápidamente diferentes ejemplos
 * de sintaxis básica de muchos lenguajes.
 *
 * ¡Muchas gracias!
 */

// Hola, mundo!
console.log('Hola, mundo!');

// Creación de variables de diferentes tipos
// eslint-disable-next-line prefer-const, no-unused-vars
let stringVariable = 'Esto es una cadena de texto';
// eslint-disable-next-line prefer-const, no-unused-vars
let numericIntegerVariable = 10;
// eslint-disable-next-line prefer-const, no-unused-vars
let numericDecimalVariable = 3.14;
// eslint-disable-next-line prefer-const, no-unused-vars
let booleanVariable = true;

// Creación de una constante
// eslint-disable-next-line no-unused-vars
const PI = 3.14159;

// Uso de if, else if y else
// eslint-disable-next-line prefer-const
let number = 15;
if (number > 10) {
  console.log('El número es mayor que 10');
} else if (number === 10) {
  console.log('El número es igual a 10');
} else {
  console.log('El número es menor que 10');
}

// Creación de estructuras de datos
// eslint-disable-next-line prefer-const
let array = [1, 2, 3, 4, 5]; // Array
// eslint-disable-next-line prefer-const
let list = [10, 20, 30]; // Lista (representada como un array en JavaScript)
// eslint-disable-next-line prefer-const, no-unused-vars
let tuple = [1, 'hola', true]; // Tupla (representada como un array en JavaScript)
// eslint-disable-next-line prefer-const, no-unused-vars
let set = new Set([1, 2, 3]); // Set
// eslint-disable-next-line prefer-const, no-unused-vars
let dictionary = { clave1: 'valor1', clave2: 'valor2' }; // Diccionario

// Uso de bucles: for, forEach y while
for (let i = 0; i < array.length; i++) {
  console.log(array[i]);
}

list.forEach((item) => {
  console.log(item);
});

let count = 0;
while (count < 5) {
  console.log(`Contador: ${count}`);
  count++;
}

// Creación de funciones
// eslint-disable-next-line no-unused-vars
function sum(a, b) {
  return a + b;
}

// eslint-disable-next-line no-unused-vars
function greet(name) {
  console.log(`Hola, ${name}!`);
}

// Creación de una función sin retorno
// eslint-disable-next-line no-unused-vars
function printMessage(message) {
  console.log(message);
}

// Creación de una función sin parámetros
// eslint-disable-next-line no-unused-vars
function sayHello() {
  console.log('¡Hola!');
}

// Creación de una clase
// eslint-disable-next-line no-unused-vars
class Persona {
  constructor(nombre, edad) {
    this.nombre = nombre;
    this.edad = edad;
  }

  presentarse() {
    console.log(`Hola, soy ${this.nombre} y tengo ${this.edad} años.`);
  }
}

// Control de excepciones
try {
  // Intentamos ejecutar un bloque de código que puede generar un error
  const resultado = 10 / 0;
  console.log(`El resultado es: ${resultado}`);
} catch (error) {
  // Capturamos y manejamos el error
  console.error(`Se produjo un error: ${error.message}`);
}

// Visita mi repo en GitHub para ver y correr los tests de este código --> https://github.com/marcode24/weekly-challenges
