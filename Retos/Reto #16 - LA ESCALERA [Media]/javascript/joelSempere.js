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
const UNDERSCORE = '__';
const STAIR_ASC = '_|';
const STAIR_DES = '|_';
const INIT_STAIR = '_';
const SPACE = ' ';

function printStairs(num = 0) {
    num != 0 ? console.log(createStairs(num)) : console.log(UNDERSCORE);
}

function createStairs(num) {
    let isDes = num < 0;
    let outStair = '';
    let stairsQtty = Math.abs(num) + 1;
    for(let x = 0; x < stairsQtty; x++) {
        if(x == 0) {
            outStair +=  (isDes ? INIT_STAIR : SPACE.repeat((stairsQtty) * 2) + INIT_STAIR) + '\n'; //
        }
        else {
            outStair += (isDes ? SPACE.repeat((x * 2) - 1) +  STAIR_DES : SPACE.repeat((stairsQtty - x) * 2) + STAIR_ASC) + '\n';   
        }
    }
    return outStair;

}

printStairs(5);
printStairs();
printStairs(-5);

