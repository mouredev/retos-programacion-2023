const dibujarTrifuerza = (n) => {
    let arriba = ' * ';
    let abajo = '***'
    let triangulo = "";

    for (let f = 0; f < n; f++) {
        triangulo += '  '.repeat(n-f-1) + arriba + (' ' + arriba).repeat(f) + '\n';
      if (f === 0) triangulo = triangulo.slice(1);
        triangulo += '  '.repeat(n-f-1) + abajo + (' ' + abajo).repeat(f) + '\n';
    }

    return triangulo;
};

console.log(dibujarTrifuerza(10));

