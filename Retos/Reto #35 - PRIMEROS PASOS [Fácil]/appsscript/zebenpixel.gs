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
// Haz un "Hola, mundo!"
function helloWorld() {
  console.log("Hola mundo!")
}
// Crea variables de tipo String, numéricas (enteras y decimales)
var mombre = "Juan Pedro"
var num = 2
var decimales = 2.34
var Booleanas = true

// Crea una constante.
const valor_pi = 3.1416
console.log(valor_pi)

// Usa un if, else if y else.
var edad = 18
if (edad >= 18) {
  console.log("Eres mayor de edad")
} else {
  console.log("Eres menor de edad")
} 

// estructura array
var array = Array(1, 2, 3, 4, 5)
  console.log(array[2]); // imprime por consola la posición 2

// estructura lista
lista = ["Hola", "mundo", 10, true, {"nombre": "Juan", "edad": 20}];// {"nombre": "Juan", "edad": 20} es un objeto dentro de una lista
console.log(lista[2]); // imprime por consola la posición 2

// estructura tupla 
tupla = ("Juan", 18, true);
  console.log = ("nombre: " + tupla[0], "edad: " + tupla[1], "eres mayor de edad: "+ tupla[2])
  //En resumen, aunque Google Apps Script no tiene un tipo de dato 
  //específico llamado "tupla," se puede utilizar arrays o objetos para lograr funcionalidades similares. 

// bucle While
function bucleWhile() {
  var contador = 0;

  while (contador < 5) {
    Logger.log("El valor del contador es: " + contador);
    contador++;
  }
}
bucleWhile();

// diccionario y función sin parametros
function crearDiccionario() {
  // Crear un diccionario vacío
  var diccionario = {};

  // Agregar elementos al diccionario
  diccionario["clave1"] = "valor1";
  diccionario["clave2"] = "valor2";
  diccionario["clave3"] = "valor3";

  // Acceder a elementos del diccionario
  var valor = diccionario["clave1"];
  Logger.log("El valor de clave1 es: " + valor);

  // Verificar si una clave existe en el diccionario
  if ("clave4" in diccionario) {
    Logger.log("La clave4 existe en el diccionario.");
  } else {
    Logger.log("La clave4 no existe en el diccionario.");
  }

  // Recorrer todas las claves y valores en el diccionario con bucle for
  for (var clave in diccionario) {
    var valor = diccionario[clave];
    Logger.log("Clave: " + clave + ", Valor: " + valor);
  }
}

// función con parámetros
function saludar(nombre) {
  Logger.log("Hola, " + nombre + "!");
}

// Llamar a la función con un argumento
saludar("Juan"); // Salida: Hola, Juan!
saludar("María"); // Salida: Hola, María!

// funcion con retorno
var a = 2
var b = 1
function suma(a, b) {
  var resultado = a + b;
  return resultado;
}
suma(a,b)

// una clase llamada "Persona"
class Persona {
  constructor(nombre, edad) {
    this.nombre = nombre;
    this.edad = edad;
  }

  saludar() {
    Logger.log(`Hola, mi nombre es ${this.nombre} y tengo ${this.edad} años.`);
  }
}
// Uso de la clase Persona
function usarClasePersona() {
  // Crear una instancia de Persona
  const persona1 = new Persona("Juan", 30);

  // Llamar al método saludar
  persona1.saludar();
}

// Ejecutar la función usarClasePersona
usarClasePersona();


// Manejo de excepciones
function miFuncion() {
  try {
    // código que puede generar una excepción
    var resultado = funcionQuePuedeFallar();
    Logger.log("Resultado: " + resultado);
  } catch (excepcion) {
    // Manejo de la excepción
    Logger.log("Se ha producido una excepción: " + excepcion.message);
  } finally {
    // Este bloque se ejecuta siempre, independientemente de si hubo una excepción o no.
    Logger.log("Finalizando la ejecución de miFuncion");
  }
}

function funcionQuePuedeFallar() {
  // Simula un error aquí
  throw new Error("Este es un error simulado");
}

// Llama a miFuncion para ver cómo maneja la excepción
miFuncion();
