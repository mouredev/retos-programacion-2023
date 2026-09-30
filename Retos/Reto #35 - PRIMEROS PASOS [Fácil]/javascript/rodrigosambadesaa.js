'use strict';

// Variables primitivas y constante.
let text = 'Hola, mundo!';
let integer = 256;
let decimal = 3.14;
let enabled = true;
const LANGUAGE = 'JavaScript';

// Condicional.
function classify(number) {
  if (number > 0) return 'positivo';
  else if (number < 0) return 'negativo';
  return 'cero';
}

// Array, objeto, Set y Map (JavaScript no posee tuplas nativas).
const array = [1, 2, 3];
const tuple = Object.freeze(['x', 'y']);
const set = new Set(array);
const dictionary = { language: LANGUAGE };
const map = new Map([['language', LANGUAGE]]);

// Bucles for, for...of (foreach) y while.
function loopExamples(values) {
  const result = [];
  for (let index = 0; index < values.length; index++) result.push(values[index]);
  for (const value of values) result.push(value);
  let index = 0;
  while (index < values.length) result.push(values[index++]);
  return result;
}

// Funciones con y sin parámetros y retorno.
function greet(name) {
  return `Hola, ${name}`;
}
function sayHello() {
  console.log(text);
}

// Clase.
class Person {
  constructor(name) {
    this.name = name;
  }
  greet() {
    return greet(this.name);
  }
}

// Control de excepciones.
function safeJson(value) {
  try {
    return JSON.parse(value);
  } catch (error) {
    return { error: error.message };
  } finally {
    enabled = Boolean(enabled);
  }
}

module.exports = {
  classify, loopExamples, greet, sayHello, Person, safeJson,
  examples: { integer, decimal, enabled, LANGUAGE, array, tuple, set, dictionary, map }
};

if (require.main === module) {
  sayHello();
  console.log(new Person('JavaScript').greet());
}
