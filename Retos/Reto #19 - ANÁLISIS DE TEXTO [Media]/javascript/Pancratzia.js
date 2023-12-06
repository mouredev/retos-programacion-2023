/*
 * Crea un programa que analice texto y obtenga:
 * - Número total de palabras.
 * - Longitud media de las palabras.
 * - Número de oraciones del texto (cada vez que aparecen un punto).
 * - Encuentre la palabra más larga.
 *
 * Todo esto utilizando un único bucle.
 * 
 * 
 * Realizado por Laura Ortega el 15/09/2023
 */


const TEXTO = "Suspendisse in laoreet libero. Vivamus ultricies purus sapien, nec varius nisl sodales dictum. Aenean non diam scelerisque, dapibus velit eget, imperdiet urna. Donec a lacus in massa luctus vulputate in eu eros. Suspendisse potenti. Ut nec luctus odio. Etiam at dolor nulla. Nullam eget lobortis dui. Vestibulum ut ex ut augue condimentum aliquam ac convallis ex. Proin rhoncus ex dui, in dignissim justo hendrerit in. Morbi nec augue ac turpis faucibus volutpat ut eu elit. Aenean dapibus laoreet vulputate. Phasellus a lectus ullamcorper, mollis felis in, maximus massas.";

const TEXTO2 = "Suspendisse potenti. Nullam varius, ligula vitae auctor convallis, quam nisi laoreet leo, finibus elementum mauris nulla vel mauris. Morbi consectetur, libero sit amet ornare ullamcorper, ante ipsum venenatis mauris, vitae tristique lacus mauris at nunc. Proin commodo volutpat nibh sed laoreet. Integer sapien tellus, mattis sit amet accumsan sed, sagittis at urna. Cras eu venenatis orci. Praesent interdum sit amet lacus eget sodales. Etiam eleifend odio a dolor elementum, in congue libero mollis. Phasellus nec sollicitudin sapien. Quisque sodales libero eu lacus aliquet mollis. Nulla id auctor purus, vitae maximus orci. Donec ut accumsan ex. Quisque tempus tortor nisi, ac varius massa euismod et. Cras condimentum quam sed magna mollis, vel laoreet ipsum egestas. Praesent ac purus a leo venenatis.";

const TEXTO3 = "a b c d e f ge h i jota kaelemeneñe o p q erre ese te u v w equis ye z";

const analizarTexto = (texto) => {
    //Variables a Buscar
    let totalPalabras = 0, longitudMediaPalabras = 0, oraciones = 0, palabraMasLarga = '';

    //Auxiliares
    let palabraActual = '', longitudPalabraActual = 0;

    //Ciclo Único
    for (let i = 0; i < texto.length; i++) {
        const char = texto[i];

        if (/[a-zA-ZáéíóúÁÉÍÓÚñÑ]/.test(char)) {
            palabraActual += char;
            longitudPalabraActual++;
        } else if (palabraActual) {
            totalPalabras++;
            longitudMediaPalabras += longitudPalabraActual;
            palabraMasLarga = palabraActual.length > palabraMasLarga.length ? palabraActual : palabraMasLarga;

            palabraActual = '';
            longitudPalabraActual = 0;
        }

        if (char === '.') oraciones++;
        if(texto.length > 0 && i === texto.length - 1 && oraciones===0) oraciones=1;
    }

    palabraMasLarga = palabraMasLarga.length > palabraActual.length ? palabraMasLarga : palabraActual;
    longitudMediaPalabras = (longitudMediaPalabras / totalPalabras).toFixed(1);

    console.log(`El texto contiene:
          - ${totalPalabras} palabras.
          - Las palabras tienen una longitud media de ${longitudMediaPalabras} caracteres.
          - ${oraciones} oraciones.
          - La palabra más larga es: ${palabraMasLarga}`);
}



analizarTexto(TEXTO);
analizarTexto(TEXTO2);
analizarTexto(TEXTO3);
