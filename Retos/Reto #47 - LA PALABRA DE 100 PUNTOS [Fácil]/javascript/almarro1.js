
function puntuacion(palabra) {
  return palabra
    //convertir a mayúsculas
    .toUpperCase()
    .replaceAll(/[ÁÀÄ]/g, 'A')
    .replaceAll(/[ÉÈË]/g, 'E')
    .replaceAll(/[ÍÌÏ]/g, 'I')
    .replaceAll(/[ÓÒÖ]/g, 'O')
    .replaceAll(/[ÚÙÜ]/g, 'U')
    // separar palabra en letras
    .split('')
    // eliminar todo lo que no sea A-Z
    .filter(letter => letter >= 'A' && letter <= 'Z')
    // pasar letra a valor según su código ascii
    .map(letter => letter.charCodeAt() - 64)
    .reduce((total, curr) => total + curr, 0);
}

const palabras = [
  'matrimonio', 'tarántula', 'arizónico', 'zoológico', 'zoólogo', 'pensamiento'
];
console.log('EJEMPLOS:')
palabras.forEach(palabra => console.log(`${palabra} -> ${puntuacion(palabra)}`));

const readline = require('readline').createInterface({ input: process.stdin, output: process.stdout, prompt: 'guess>' });

async function main() {
  let found = false;
  while (!found) {
    const palabra = await new Promise(resolve => readline.question('Introduce una palabra: ', resolve));
    const valor = puntuacion(palabra);
    console.log(`La palabra "${palabra}" tiene un valor de ${valor} puntos`);
    if (valor === 100) {
      console.log('¡Enhorabuena, has encontrado la palabra de 100 puntos!');
      found = true;
    }
  }
  process.exit();
}

main();
