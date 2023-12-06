/*
 * Crea 3 funciones, cada una encargada de detectar si una cadena de
 * texto es un heterograma, un isograma o un pangrama.
 * - Debes buscar la definición de cada uno de estos términos.
 * 
 * CREADO POR LAURA ORTEGA 26/08/2023
 */



const abecedario = "abcdefghijklmnñopqrstuvwxyz";

function contarLetras(texto){
    let letras = [];
    texto = texto.toLowerCase().replace(/\s/g, '');
    for (let i = 0; i < texto.length; i++) {
        const letra = texto[i];
        const letraEncontrada = letras.find(l => l.letra === letra);
        if (letraEncontrada) {
            letraEncontrada.cantidad++;
        } else {
            letras.push({ letra, cantidad: 1 });
        }
    }
    return letras;
}

function esHeterograma(letras){ //cada letra esta solo una vez
    return letras.filter(l => l.cantidad > 1).length === 0;
}

function esIsograma(letras){ //todas las letras se repiten la misma cantidad de veces
    return letras.filter(l => l.cantidad === 1).length === letras.length;
}

function esPangrama(letras){ //contiene todas las letras del abecedario
    for (let letra of abecedario) {
        if (!letras.find(l => l.letra === letra)) {
            return false;
        }
    }
    return true;
}


function ejercicio(texto){

    let letras = contarLetras(texto);
    console.log("#################################");
    console.log(`La frase ${(esHeterograma(letras) ? "es" : "no es")} un heterograma`);
    console.log(`La frase ${(esIsograma(letras) ? "es" : "no es")} un isograma`);
    console.log(`La frase ${(esPangrama(letras) ? "es" : "no es")} un pangrama`);
    console.log("#################################");
}

ejercicio("Hola Mundo");
ejercicio("Hola");
ejercicio("Alla en la fuente habia un chorrito se hacia grandote se hacia chiquito estaba de mal humor pobre chorrito tenia calor");
ejercicio("abcdefghijklmnñopqrstuvwxyz");
