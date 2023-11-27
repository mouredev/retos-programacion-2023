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


function escalera(num){
    let space=" "
    if(num>0)
    {
      for (let index = 0; index < num; index++) 
            {
              console.log(space.repeat(num-index) + '_|');
            }
    }    
    
    if(num<0)
    {
      let newnum=Math.abs(num)
        for (let index = 0; index < newnum; index++) 
          {
            console.log(space.repeat(index) + '_|');
          }
        console.log("menos 0")
    }
      
      if(num==0){
        return '__';
      }
  

  
}
escalera(-2)
escalera(4)

escalera(0)