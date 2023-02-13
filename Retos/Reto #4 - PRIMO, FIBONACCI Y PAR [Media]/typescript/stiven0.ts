/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */

const isPrime = ( number: number ): string => {

    if ( number < 2 ) return 'debes ingresar un numero mayor a 1';

    const raizOfNumber = Math.trunc( Math.sqrt( number ) );
    const arrayNumbers = [ ...Array( raizOfNumber + 1 ).keys() ].filter( number => number > 1 )
    let isPrime = true;

    for ( let item of arrayNumbers ) {

        if ( number % item === 0 ) {
            isPrime = false;
            break;
        }

    }

    return isPrime ? 'es primo' : 'no es primo';

}

const isFibonacci = ( number: number ): string => {

    let arrFibonacci: Array<number> = [];
    let isFibonacci = false;

    for ( let i = 0; i <= number + 1; i++ ) {

        const result = arrFibonacci[arrFibonacci.length - 1] + arrFibonacci[arrFibonacci.length - 2] || 1;

        if ( result === number || number === 0 ) {
            isFibonacci = true;
            break;
        } else if ( result > number ) {
            break;
        }

        arrFibonacci.push( result );

    }

    return isFibonacci ? 'fibonacci' : 'no es fibonacci';
}

const isEven = ( number: number ) => number % 2 === 0 ? 'es par' : 'es impar';

const checkNumber = ( number: number ): string => {
    return `${ number } ${ isPrime( number ) }, ${ isFibonacci( number ) } y ${ isEven( number ) }`; 
}

console.log( checkNumber(2) );
console.log( checkNumber(7) );