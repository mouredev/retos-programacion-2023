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


  
function escalones(numero){
    let contadorPositivos = 1;
    let contadorNegativos = -1
    let escalera = "";

    if(numero>0){
        while(contadorPositivos<=numero){
            escalera += '  '.repeat(numero - contadorPositivos) + '_|\n';
            contadorPositivos++;
        }
    }else if(numero<0){
        while(contadorNegativos>=numero){
            escalera += '  '.repeat(Math.abs(contadorNegativos) - 1) + '|_\n';
            contadorNegativos--;
        }
    }else {
        escalera = '__';
    }
    return escalera
}

console.log(escalones(6));
