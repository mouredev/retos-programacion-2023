/*
 * Como cada año, el día 256 se celebra el "Día de la Programación".
 * En nuestra comunidad siempre hacemos una gran fiesta donde repartiremos 
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
 * - Crea estructuras como un array, lista, tuple, set y diccionario.
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


// Variables de tipo String, numéricas (enteras y decimales) y Booleanas

let myString = 'Hola, mundo!';
let myInteger = 23;
let myDecimal = 3.14;
let myBoolean = true;


// Constante

const myName = 'nlarrea';


// if, else if y else

if (2 > 4) {
    console.log('2 es mayor que 4');
} else if (2 < 4) {
    console.log('2 es menor que 4');
} else {
    console.log('2 y 4 son iguales');
}


// Estructuras tipo Array, lista, tuple, set y diccionario

const array = [1, 2, 3, 4, 5];      // Equivalente a lista
const set = new Set(array);
// En JS no hay tuples
const diccionario = {
    nombre: 'Naia',
    edad: 25
};


// Bucles for, foreach y while

for (let i = 0; i < 10; i++) {
    console.log(`Iteración ${i} del bucle for`);
}

array.forEach(number => {
    console.log(number);
});

let i = 0;
while (i < 10) {
    console.log(`Iteración ${i} del bucle while`);
    i++;
}


// Funciones (con/sin parámetros y con/sin retorno)

function sinParamsNiRetorno() {
    console.log('Saludos!');
}

function conParamsSinRetorno(name) {
    console.log(`Saludos ${name}`);
}

function sinParamsConRetorno() {
    return 5 + 7;
}

function conParamsConRetorno(numOne, numTwo) {
    const numThree = numOne + numTwo
    return numOne + numTwo + numThree;
}

// llamadas a las funciones:
sinParamsNiRetorno();           // se imprime: Saludos!
conParamsSinRetorno('Naia');    // se imprime: Saludos Naia
sinParamsConRetorno();          // obtiene un: 12
conParamsConRetorno(2, 10);     // obtiene un: 24


// Crea una clase

class Person {
    constructor(name, age) {
        this.name = name;
        this.age = age;
    }

    introduce() {
        console.log(`Hi! My name is ${this.name}`);
    }

    compareAges(age) {
        const difference = Math.abs(age - this.age);

        if (age > this.age) {
            console.log(`You are ${difference} year(s) older than me!`);
        } else if (age < this.age) {
            console.log(`I am ${difference} year(s) older than you!`);
        } else {
            console.log('We are the same age!');
        }

        return difference;
    }
}

// crear instancias de la clase
const me = new Person('Naia', 25);
const anotherPerson = new Person('Cristina', 29);

console.log(me.name);   // Naia
console.log(me.age);    // 25
me.introduce();         // imprime: Hi! My name is Naia
me.compareAges(8);
// imprime: I am 17 year(s) older than you!
// se obtiene: 17

console.log(anotherPerson.name);    // Cristina
// ...


// Muestra el control de excepciones

try {
    const constante = 'Sentencia try-catch';
    constante = 4;
} catch (error) {
    console.log(`${error.name}: ${error.message}`);
    // TypeError: Assignment to constant variable.
}

try {
    throw Error('Se ha lanzado un error!');
} catch (error) {
    console.log(`${error}`);
    // Error: Se ha lanzado un error!
}

// Personalizar tipos de errores

class MyPersonalError extends Error {
    constructor(message, ...params) {
        super(message, ...params);

        this.name = 'MyPersonalError';
    }
}

try {
    throw new MyPersonalError('An error occurred!');
} catch (error) {
    console.log(`${error.name}: ${error.message}`);
    // MyPersonalError: An error occurred!
}