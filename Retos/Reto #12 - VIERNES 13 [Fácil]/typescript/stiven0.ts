// /*
//  * Crea una función que sea capaz de detectar si existe un viernes 13 en el mes y el año indicados.
//  * - La función recibirá el mes y el año y retornará verdadero o falso.
//  */

type monthType = 'january' | 'february' | 'march' | 'april' | 'may' | 'june' | 
                 'july' | 'august' | 'september' | 'october' | 'november' | 'december';

const detectFridayTheThirteenth = ( month: monthType, year: number ): boolean => {

    const date = new Date( `${ month }, 13 ${ year }` ).getDay();
    return date === 5;

};

console.log( detectFridayTheThirteenth( 'october', 2023 ) ); // true
console.log( detectFridayTheThirteenth( 'august', 2021 ) );  // true
console.log( detectFridayTheThirteenth( 'june', 1924 ) );    // true
console.log( detectFridayTheThirteenth( 'august', 1700 ) );  // true
console.log( detectFridayTheThirteenth( 'march', 2023 ) );   // false