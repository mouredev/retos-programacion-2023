/*
 * Crea un programa que detecte cuando el famoso "Código Konami" se ha introducido
 * correctamente desde el teclado. 
 * Si sucede esto, debe notificarse mostrando un mensaje en la terminal.
 */

const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const konami = ['u', 'u', 'd', 'd', 'l', 'r', 'l', 'r', 'b', 'a'];

let index = 0;

rl.on('line', (input) => {
  index = input.replace(/\s+/g, '').trim() === konami[index] ? index + 1 : 0;
  if (index === konami.length) {
    console.log('Konami code!');
    rl.close();
  }
});

// Visita mi repo en GitHub para ver y correr los tests de este código --> https://github.com/marcode24/weekly-challenges
