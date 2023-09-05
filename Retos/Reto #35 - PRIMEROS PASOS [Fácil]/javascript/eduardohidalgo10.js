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
 * - Haz un "Hola, mundo!"*
 * - Crea variables de tipo String, numéricas (enteras y decimales)*
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


/* Hola mundo! */ 

console.log('Hola Mundo!')

/*Crea variables de tipo String, numéricas (enteras y decimales)*
   y Booleanas (o cualquier tipo de dato primitivo). */ 

let string = 'Eduardo';
let num = 2;
let dec = 1.0;
let lloviendo = true;


//- Crea una constante.

const apellido = 'Hidalgo';


// Usa un if, else if y else.

if(lloviendo) {
    console.log('Sal con una sombrilla');
    
}else if(!lloviendo) {
    console.log('Sal sin sombrilla');
}else {
    console.log('Mojate!');
}


//Crea estructuras como un array, lista, tupla, set y diccionario.

/*array*/

let numeros = [1,2,3,4,5];

/*lista*/

let equipos = ['televisor','celular','tablet'];

/*set*/

let mySet = new Set(['Small','Medium','Large']);

/*Diccionario es un objecto en JS*/

let User = {
    name:"Eduardo",
    lastname:"Hidalgo",
    age:28
}

/*Usa un for, foreach y un while*/

for(let i = 0; i < equipos.length;i++) {
    console.log(equipos[i]);
}

//foreach
let frutas = ['manzana','pera','uva'];

frutas.forEach(element => {
    console.log(element)
});

//while

let limit = 10;
let counter =0;

while(limit >= counter){
    console.log(counter++)
}

//Crea diferentes funciones (con/sin parámetros y con/sin retorno).

//con y sin parametros
const sum = (a,b) => {
    return console.log(a + b);
};

const Greeting = () => {
    return console.log('Saludos!!!!')
};

//sin retorno

const Despedir = () => {
    console.log('Adios');
}

//Crea una clase

class Perro {
    constructor(nombre) {
        this.nombre = nombre;
    }
}

//Muestra el control de excepciones.

try {
    let sum = 1 + 0.50 + sum;
    console.log(sum)


} catch (error) {
    console.log('Hubo un Error: ' + error)
}
