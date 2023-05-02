/*Crea 3 funciones, cada una encargada de detectar si una cadena de
 * texto es un heterograma, un isograma o un pangrama.
 * - Debes buscar la definición de cada uno de estos términos.
 */
//Es una palabra o frase que no contiene ninguna letra repetida.1

function heterograma(palabra) {
    var abecedario = "abcdefghijklmnñopqrstuvwxyz";
    var palabra = palabra.toLowerCase();
    var heterograma = true;
    for (var i = 0; i < abecedario.length; i++) {
        var contador = 0;
        for (var j = 0; j < palabra.length; j++) {
            if (abecedario[i] == palabra[j]) {
                contador++;
            }
        }
        if (contador > 1) {
            heterograma = false;
        }
    }
    if (heterograma) {
        console.log("La palabra " + palabra + " es un heterograma");
    } else {
        console.log("La palabra " + palabra + " no es un heterograma");
    }
}

heterograma("murcielago");

function esIsograma(cadena) {
    cadena = cadena.toLowerCase();
    let contador = {};
    for (let i = 0; i < cadena.length; i++) {
        let letra = cadena[i];

        if (contador[letra]) {
            return false;
        }
        contador[letra] = true;
    }

    return true;
}

esIsograma("acondicionar")

function esPangrama(cadena) {
    // Convertir la cadena a minúsculas para hacer la comparación de caracteres más fácil
    cadena = cadena.toLowerCase();
    // Crear un objeto para llevar la cuenta de la cantidad de veces que aparece cada letra en la cadena
    let contador = {};
    // Recorrer cada letra de la cadena
    for (let i = 0; i < cadena.length; i++) {
        let letra = cadena[i];
        // Si la letra es una letra del alfabeto, agregarla al objeto contador
        if (/[a-z]/.test(letra)) {
            contador[letra] = true;
        }
    }
    // Si el objeto contador tiene 26 propiedades (una para cada letra del alfabeto), entonces la cadena es un pangrama
    return Object.keys(contador).length === 26;
}



esPangrama(" Benjamín pidió una bebida de kiwi y fresa. Noé, sin vergüenza, la más exquisita champaña del menú.")