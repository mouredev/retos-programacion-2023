/*
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
 */

// 1.- Muestra en la consola el mensaje Hola, mundo!
console.log("Hola, mundo!");

// 2.- Declara variables de tipo primitivo
let nombre = "Flavio"; // string
let edad = 50; // number
let precio = 9.99; // number
let activo = true; // boolean
let suma; // undefined

// 3.- Declara una constante. Según convención, va en mayúsculas
const URL = "www.google.com";

// 4.- Uso de condicional if
if (precio < 10) {
  console.log("producto en oferta");
} else if (precio < 20) {
  console.log("precio normal");
} else {
  console.log("alta demanda");
}

// 5.- Crea estructuras de datos
const notas = [16, 20, 11, 14]; // array
const nombres = new Set(["Juan", "Ana", "Andrea"]); // colección
const persona = { nombre: "Juan", edad: 20, activo: true }; // objeto

// 6.- Usa un for, foreach y un while.
for (let i = 0; i < notas.length; i++) {
  console.log(notas[i]);
}
notas.forEach((nota) => {
  console.log(nota);
});
for (nombre of nombres) {
  console.log(nombre);
}
let i = 0;
while (true) {
  console.log(i++);
  if (i > 5) {
    break;
  }
}

// 7.- Crea diferentes funciones (con/sin parámetros y con/sin retorno).
function sumar(num1, num2) {
  return num1 + num2;
}
console.log(sumar(1, 2));

const mostrarFecha = () => {
  console.log(new Date());
};
mostrarFecha();

// 8.- Crea una clase.
class Persona {
  constructor(nombre) {
    this.nombre = nombre;
  }
}
const juan = new Persona("Juan");
console.log(juan);

// 9.- Uso de control de excepciones
try {
  throw new Error('Sucedió un error')
} catch (error) {
  console.log(error.message);
}
