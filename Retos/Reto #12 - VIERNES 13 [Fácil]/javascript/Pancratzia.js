/*
 * Crea una función que sea capaz de detectar si existe un viernes 13 en el mes y el año indicados.
 * - La función recibirá el mes y el año y retornará verdadero o falso.
 * 
 * 
 * 
 * Realizado por Laura Ortega el 28/08/2023
 */

const meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"];

const hasFriday13 = (month, year) => {

    month--;
    const date = new Date(year, month, 13);
    if (date.getDay() === 5) {
        return true;
    }

    return false;
}

const validate = (month, year) => {
    if (isNaN(month) || isNaN(year) || month < 1 || month > 12 || year < 0) {
        return false;
    }
    return true;
}


const friday13 = (month, year) => {
    if (!validate(month, year)) {
        return `No ha ingresado una fecha válida`;
    }
    return `El mes de ${meses[month - 1]} del año ${year} ${hasFriday13(month, year) ? '': 'no '}tiene un viernes 13`;
}



//Los meses irán del 1 al 12 para no confundir al usuario y en la función se hará mes--

console.log(friday13(11, 2020));
console.log(friday13(9, 1999));
console.log(friday13(9, 2023));
console.log(friday13(1, 1954));
console.log(friday13(10, 2023));

