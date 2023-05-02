/*
 * Crea una función que dibuje una escalera según su número de escalones.
 * - Si el número es positivo, será ascendente de izquiera a derecha.
 * - Si el número es negativo, será descendente de izquiera a derecha.
 * - Si el número es cero, se dibujarán dos guiones bajos (__).
 * 
 * Ejemplo: 4
 *         _
 *       _|       
 *     _|
 *   _|
 * _|
 * 
 */

const main = ( stairs: number ) => {
    if ( stairs === 0 ) {
        console.log('__');
        return;
    }

    const stairsIsGreaterZero = stairs > 0;

    for ( let i = stairsIsGreaterZero ? stairs : 0; stairsIsGreaterZero ? i >= 0 : i <= Math.abs( stairs ); stairsIsGreaterZero ? i-- : i++ ) {
        i === stairs || ( stairs < 0 && i === 0 )
        ? console.log( ' _'.replace(/\s/g, ' '.repeat( stairsIsGreaterZero ? stairs * 2 : 1 ) ) ) 
        : console.log( `${ stairsIsGreaterZero ? ' _|' : ' |_'  }`.replace(/\s/g, ' '.repeat( i * 2 ) ));   
    }
}

main(4);
main(-4);
main(0);
