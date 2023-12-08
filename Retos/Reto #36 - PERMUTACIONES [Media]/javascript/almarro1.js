function permutar(palabra) {
  const letras = palabra.split('');
  function permutaArray(array) {
    const permutaciones = [];
    for (let indice = 0; indice < array.length; indice++) {
      if (array.length > 1) {
        const primero = array.shift();
        permutaArray(array).forEach(x => {
          const y = [primero, ...x];
          permutaciones.push([...y]);
        });
        array.push(primero);
      } else {
        permutaciones.push([...array]);
      }
    }
    return permutaciones;
  }
  return permutaArray(letras).map(x => x.join(''));
}

console.log(permutar('abcde'));
