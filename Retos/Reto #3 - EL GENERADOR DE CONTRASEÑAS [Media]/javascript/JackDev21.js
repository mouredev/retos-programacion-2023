/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */


function generarPassword(conMinusculas, conMayusculas, conNumeros, conSimbolos) {

    const minusculas = 'abcdefghijklmnopqrstuvwxyz';
    const mayusculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
    const numeros = '0123456789';
    const simbolos = '!@#$%^&*()_+{}:"<>?|[];\',./`~';

    let caracteres; // Variable para almacenar los caracteres posibles

    // Añadir minusculas si el parámetro conMinusculas es true
    if (conMinusculas) {
        caracteres += minusculas;
    }

    // Añadir mayúsculas si el parámetro conMayusculas es true
    if (conMayusculas) {
        caracteres += mayusculas;
    }

    // Añadir números si el parámetro conNumeros es true
    if (conNumeros) {
        caracteres += numeros;
    }

    // Añadir símbolos si el parámetro conSimbolos es true
    if (conSimbolos) {
        caracteres += simbolos;
    }

    // Generar una longitud aleatoria para la contraseña entre 8 y 16
    const longitud = Math.floor(Math.random() * (16 - 8 + 1)) + 8;

    // Inicializar la contraseña como un string vacío
    let password = '';

    // Construir la contraseña con caracteres aleatorios hasta alcanzar la longitud deseada
    for (let i = 0; i < longitud; i++) {
        // Elegir un índice aleatorio de la cadena de caracteres posibles
        const charIndex = Math.floor(Math.random() * caracteres.length);
        // Añadir el carácter correspondiente a la contraseña
        password += caracteres[charIndex];
    }

    // Devolver la contraseña generada
    return password;
}

// Uso de la función
// Configurar las opciones de generación de contraseña
const conMinusculas = true;
const conMayusculas = true;
const conNumeros = true;
const conSimbolos = true;

// Generar la contraseña con las opciones configuradas
const nuevaPassword = generarPassword(conMinusculas, conMayusculas, conNumeros, conSimbolos);
// Mostrar la contraseña generada
console.log(nuevaPassword);
console.log(nuevaPassword.length)

