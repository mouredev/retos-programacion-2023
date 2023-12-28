/* 
Ciclo sencillo con la solucion:

for (let num:number = 1; num <=100; num++)
{
  let reemplazo:string = '';
  
  if (num % 3 == 0) reemplazo += 'fizz';
  if (num % 5 == 0) reemplazo += 'buzz';

  console.log(reemplazo.length > 0 ? reemplazo : num);
} 
*/

/* Ciclo dentro de funcion para retornar string con la solucion: */

const fizzbuzz = ():string => {
  const listado:Array<string | number> = [];

  for (let num:number = 1; num <=100; num++)
  {
    let reemplazo:string = '';
    
    if (num % 3 == 0) reemplazo += 'fizz';
    if (num % 5 == 0) reemplazo += 'buzz';

    listado.push(reemplazo.length > 0 ? reemplazo : num);
  }

  return listado.join('\n');
};

console.log(fizzbuzz());
