
/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */
/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */




function generatePassword(max) {
    let abecedario="abcdefghijklmnopqrstuvwxyzABCDEFGHIJOKLMNOPQRSTUVWYXZ123456789!#$%&/()=?¡¿*¨[]_:;><"

    let result=""
    for (let i = 0; i < max; i++) {
        result+=abecedario.charAt(Math.floor(Math.random()*abecedario.length))

        
    }
    console.log(result);

}
generatePassword(8)