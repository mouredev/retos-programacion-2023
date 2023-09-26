/*
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */


// 1) Creamos una funcion que recibe un texto
function lenguajeHacker(texto) {

    // 2) Creamos el objeto 'leet' para almacenar las  conversiones de caracteres
    const objetoLeet = {
        'a' : '4',
        'b' : '8',
        'e' : '3',
        'g' : '6',
        'l' : '1',
        'o' : '0',
        's' : '5',
        't' : '7',
        'z' : '2'
    }

    // 3) Definimos una variable 'vacia' donde guardaremos nuestra conversion
    let textoAGuardar = '';

    // 4) Recorremos el largo del 'Texto pedido por parametro en la funcion'
    for (let i = 0; i < texto.length; i++) {
        
        // 5) A continuacion Creamos una variable 'char' que gracias a 'texto.charAt(i)' Extraera caracter por caracter de la cadena introducida texto y lo convertira en minuscula
        const char = texto.charAt(i).toLowerCase();
        
        // 6) Luego buscamos en 'ObjetoLeet' si existen estos '[char]' en caso de que si lo sustituimos y lo guardamos en 'textoAGuardar' de lo contrario || guardamos el 'char' en 'textoAGuardar'  
        textoAGuardar += objetoLeet[char] || char;    
    }

    // 7) Devolvemos ahora si nuestro 'textoAGuardar' con sus nuevos datos guardados
    console.log(textoAGuardar)
}



// A PROBAR
lenguajeHacker("En que anda la banda loca");
