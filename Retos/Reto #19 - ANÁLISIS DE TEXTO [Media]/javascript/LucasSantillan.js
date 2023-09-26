/*
Crea un programa que analice texto y obtenga:
- Número total de palabras.
- Longitud media de las palabras.
- Número de oraciones del texto (cada vez que aparecen un punto).
- Encuentre la palabra más larga.
 Todo esto utilizando un único bucle.

 Texto extraido del cuento "El jorobadito" de Roberto Arlt
*/
"use strict"

const texto = `Los diversos y exagerados rumores desparramados con motivo de la conducta que observé en compañía de Rigoletto, el jorobadito, en la casa de la señora X, apartaron en su tiempo a mucha gente de mi lado.
Sin embargo, mis singularidades no me acarrearon mayores desventuras, de no perfeccionarlas estrangulando a Rigoletto.
Retorcerle el pescuezo al jorobadito ha sido de mi parte un acto más ruinoso e imprudente para mis intereses, que atentar contra la existencia de un benefactor de la humanidad.`;

function analicisTexto(texto) {
  let numOraciones = 0;
  let acumPromedioPalabras = 0;
  let palabraMasLarga = '';
  let textoFomateando = '';
  let textoOraciones = [];
  let textoPalabras = [];

  textoOraciones = texto.split('.');
  numOraciones = textoOraciones.length - 1;

  textoFomateando = texto.replaceAll('\n', ' ');
  textoFomateando = textoFomateando.replaceAll(/[^0-zÀ-ÿ\ ]+/g, '');
  textoPalabras =  textoFomateando.split(' ');

  textoPalabras.forEach(palabra => {
    palabraMasLarga = palabra.length > palabraMasLarga.length ? palabra : palabraMasLarga;
    acumPromedioPalabras += palabra.length;
  });

  console.log(`Número total de palabras: ${textoPalabras.length}`);
  console.log(`Longitud media de las palabras: ${acumPromedioPalabras / textoPalabras.length}`);
  console.log(`Número de oraciones: ${numOraciones}`);
  console.log(`La palabra más larga es: "${palabraMasLarga}"`);

}

analicisTexto(texto);
