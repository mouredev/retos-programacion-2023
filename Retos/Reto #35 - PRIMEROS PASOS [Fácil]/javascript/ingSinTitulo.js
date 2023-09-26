// Punto 1: Hola, mundo!
console.log("Hola, mundo!");

// Punto 2: Crea una variable de texto o string
let miTexto = "¡Hola desde JavaScript!";

// Punto 3: Crea una variable de número entero
let miEntero = 42;

// Punto 4: Crea una variable de número con decimales
let miDecimal = 3.14;

// Punto 5: Crea una variable de tipo booleano
let miBooleano = true;

// Punto 6: Crea una constante
const MI_CONSTANTE = 10;

// Punto 7: Usa un if, else if y else
if (miEntero > 50) {
    console.log("El número es mayor que 50");
} else if (miEntero < 50) {
    console.log("El número es menor que 50");
} else {
    console.log("El número es igual a 50");
}

// Punto 8: Crea un Array
let miArray = [1, 2, 3, 4, 5];

// Punto 9: Crea una lista (Array en JavaScript)
let miLista = ["Manzana", "Banana", "Naranja"];

// Punto 10: Crea una tupla (no aplicable en JavaScript)

// Punto 11: Crea un set
let miSet = new Set(["Rojo", "Verde", "Azul"]);

// Punto 12: Crea un diccionario (objeto en JavaScript)
let miDiccionario = {
    clave1: "valor1",
    clave2: "valor2"
};

// Punto 13: Usa un ciclo for
for (let i = 0; i < miArray.length; i++) {
    console.log(miArray[i]);
}

// Punto 14: Usa un ciclo foreach
for (let elemento of miLista) {
    console.log(elemento);
}

// Punto 15: Usa un ciclo while
let contador = 0;
while (contador < 3) {
    console.log("Contador: " + contador);
    contador++;
}

// Punto 16: Crea una función sin parámetros que no retorne nada
function funcionSinParametros() {
    console.log("Función sin parámetros");
}

// Punto 17: Crea una función con parámetros que no retorne nada
function funcionConParametros(param1, param2) {
    console.log("Parámetro 1: " + param1);
    console.log("Parámetro 2: " + param2);
}

// Punto 18: Crea una función con parámetros que retorne valor
function funcionConRetorno(a, b) {
    return a + b;
}

// Punto 19: Crea una clase (sintaxis de clase en JavaScript)
class Persona {
    constructor(nombre, edad) {
        this.nombre = nombre;
        this.edad = edad;
    }
}

// Punto 20: Muestra control de excepciones
try {
    let resultado = miEntero / 0;
    console.log(resultado);
} catch (error) {
    console.log("Error: " + error.message);
}
