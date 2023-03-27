/*
 * Crea una función que sea capaz de detectar si existe un viernes 13 en el mes y el año indicados.
 * - La función recibirá el mes y el año y retornará verdadero o falso.
 */

function isFriday (month, year) {
    const d = new Date();
    d.setFullYear(year, month, 13);
    // week Day
    wd = d.getDay();
    // Check if is Friday
    if (wd === 5) {
        // It is Friday
        return true;
    } else {
        return false;
    }
}

// Month between 0-11
console.log(isFriday(9, 2023));
