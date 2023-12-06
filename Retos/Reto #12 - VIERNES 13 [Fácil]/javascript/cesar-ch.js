/*
 * Crea una función que sea capaz de detectar si existe un viernes 13 en el mes y el año indicados.
 * - La función recibirá el mes y el año y retornará verdadero o falso.
 */

function itsFridayThirteenth(month, year) {
    return new Date(`${month} 13, ${year}`).getDay() === 5
}

console.log(itsFridayThirteenth('January', 2023))
console.log(itsFridayThirteenth('April', 2023))