
/*
 *	¡El nuevo "The Legend of Zelda: Tears of the Kingdom" ya está disponible! 
 *
 * Crea un programa que dibuje una Trifuerza de "Zelda"
 * formada por asteriscos.
 * - Debes indicarle el número de filas de los triángulos con un entero positivo (n).
 * - Cada triángulo calculará su fila mayor utilizando la fórmula 2n-1.
 *
 * Ejemplo: Trifuerza 2
 * 
 *    *
 *   ***
 *  *   *
 * *** ***
 *
 */

 function dibujarTrifuerza(n){
   let base =2*n-1
     
   for(let i=1;i<=n;i++){
     let espacios=' '.repeat(n-i)
     let asteriscos="*".repeat(2*i-1) 
     console.log(espacios+asteriscos)
     
   }
      for(let i=1;i<=n;i++){
     let espacios=' '.repeat(n-i)
     let asteriscos="*".repeat(2*i-1) 
     let espaciomedio=" ".repeat(2*(n-i))
     console.log(espacios+asteriscos+espaciomedio+asteriscos)
     
   }
}

dibujarTrifuerza(3)