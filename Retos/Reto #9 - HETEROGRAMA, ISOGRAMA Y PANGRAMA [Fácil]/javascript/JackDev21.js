/*
 * Crea 3 funciones, cada una encargada de detectar si una cadena de
 * texto es un heterograma, un isograma o un pangrama.
 * - Debes buscar la definición de cada uno de estos términos.
 */



const esHeterograma = (str) => {
  let heterograma = true;
  let letrasEncontradas = new Set();
  const alfabeto = "abcdefghijklmnopqrstuvwxyzñ";

  for (let i = 0; i < str.length && heterograma; i++) {
    let letra = str[i].toLowerCase();
    if (letrasEncontradas.has(letra)) {
      heterograma = false;
    } else if (alfabeto.includes(letra)) {
      letrasEncontradas.add(letra);
    }
  }
  return heterograma;
}


const esIsograma = (str) => {
  let letrasEncontradas = new Set();

  for (let letra of str.toLowerCase()) {
    if (/[a-zñ]/.test(letra)) {
      if (letrasEncontradas.has(letra)) {
        return false;
      }
      letrasEncontradas.add(letra);
    }
  }

  return true;
}


const esPangrama = (str) => {
  const alfabeto = "abcdefghijklmnopqrstuvwxyz";

  for (let letra of alfabeto) {
    if (!str.toLowerCase().includes(letra)) {
      return false;
    }
  }

  return true;
}


const texto = "murcielago";

console.log(`¿Es un heterograma? ${esHeterograma(texto)}`);
console.log(`¿Es un isograma? ${esIsograma(texto)}`);
console.log(`¿Es un pangrama? ${esPangrama(texto)}`);