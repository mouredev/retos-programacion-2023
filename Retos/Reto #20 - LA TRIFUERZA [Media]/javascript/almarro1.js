function dibujaTriFuerza(filasPorTriangulo = 3) {
  // generamos el triángulo
  const triangulo = generaTriangulo(filasPorTriangulo);
  for (let fila = 0; fila < 2 * filasPorTriangulo; fila++) {
    const caracteres = triangulo[fila % filasPorTriangulo];
    if (fila < filasPorTriangulo) {
      // si estamos en la fila superior, dibujar el triángulo desplazado la mitad de '(2* (2*filas -1) +1) - filas'
      console.log(caracteres.padStart(3 * filasPorTriangulo - 1, ' '))
    } else {
      // si es la parte superior dibujamos dos triangulos uno tras otro separados por un espacio extra
      console.log(`${caracteres} ${caracteres}`);
    }
  }
}

function generaTriangulo(filas) {
  return Array(filas) //generamos un vector de 'filas' filas
    .fill(Array(2 * filas - 1).fill(' ')) // cada fila tiene '2*filas -1' caracteres en blanco
    .map((fila, indice) => {
      // sustituimos los caracteres centrales por un '*'
      return [...fila].fill('*', filas - 1 - indice, filas + indice).join('');
    });
}

dibujaTriFuerza(7);
