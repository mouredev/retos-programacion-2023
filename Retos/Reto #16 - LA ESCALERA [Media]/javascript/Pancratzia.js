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
 * 
 * 
 * Creado por Laura Ortega - 04/09/2023
 */

function drawStairs(n){

    let stairs = '';

    if(n===0) stairs="__";
    else if (n<0){
        stairs = "__";
        for(let i=0; i<Math.abs(n); i++) stairs = stairs + "\n"+ "  ".repeat(Math.abs(i+1))+ "|_" ; 
    }
    else{
        stairs += "  ".repeat(Math.abs(n)) + "_" + "\n";
        for(let i=0; i<n; i++) stairs += "  ".repeat(Math.abs(i-n+1)) + "_|" + "\n";
    }

    console.log(stairs);

}


drawStairs(4);
drawStairs(-6);
drawStairs(0);