// En un fichero, haz lo siguiente (si el lenguaje lo soporta),
// y comenta cada bloque para identificar con qué se corresponde:
// - Haz un "Hola, mundo!"
// - Crea variables de tipo String, numéricas (enteras y decimales)
//   y Booleanas (o cualquier tipo de dato primitivo).
// - Crea una constante.
// - Usa un if, else if y else.
// - Crea estructuras como un array, lista, tupla, set y diccionario.
// - Usa un for, foreach y un while.
// - Crea diferentes funciones (con/sin parámetros y con/sin retorno).
// - Crea una clase.
// - Muestra el control de excepciones.
//
// Así, cualquier persona podrá consultar rápidamente diferentes ejemplos
// de sintaxis básica de muchos lenguajes.
//
// ¡Muchas gracias!
// /

console.log("Hola, mundo!");

let str = "María";
let int = 30;
let flt = 11.20;

const BIRTHDAY = "1992/11/20";

if (int > 25) {
  console.log("Bigger than 25");
} else if (int === 30) {
  console.log("Equal to 30");
} else {
  console.log("No matches");
};

let arr = [1, 2, 3, 4, 5];

for (num in arr) {
  console.log(arr[num] * 2);
}

const sayHi = () => {
  return "Hiiiii!";
}

console.log(sayHi());

const sayBye = () => {
  console.log("Bye...");
}

sayBye();


class Person {
  constructor(name, age, city) {
    this.name = name;
    this.age = age;
    this.city = city
  }
}

let me = new Person("Maria", 30, "Nara")
console.log(me);
