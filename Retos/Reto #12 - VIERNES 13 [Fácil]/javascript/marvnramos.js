/*
 * Crea una función que sea capaz de detectar si existe un viernes 13 en el mes y el año indicados.
 * - La función recibirá el mes y el año y retornará verdadero o falso.
 */

function isFriday13(month, year) {
    const date = new Date(`${year}/${month}/13`);
    const dayOfWeek = date.getDay();

    return dayOfWeek === 5;
}

console.log(isFriday13(9, 2023));