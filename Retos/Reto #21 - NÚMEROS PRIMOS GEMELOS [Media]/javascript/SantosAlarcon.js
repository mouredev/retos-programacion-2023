/**
 * Comprueba si el número es primo.
 * @param numero - El número que se va a comprobar si es primo o no.
 **/

const es_primo = (numero) => {
    if (numero <= 1) return false;

    for (let indice = 2; indice < numero; indice++) {
        if (numero % indice === 0) {
            return false; 
        }
    }

    return true;
}

/**
 *  Función que imprime los números gemelos.
 *  @param rango - El rango máximo que se va a iterar.
 **/
const buscarPrimosGemelos = (rango) => {
    for (let n = 2; n <= rango; n++) {
        if (n + 2 < rango && es_primo(n) && es_primo(n + 2)) {
            console.log(`(${n}, ${n+2})`);
        }
    }
}

buscarPrimosGemelos(44);
