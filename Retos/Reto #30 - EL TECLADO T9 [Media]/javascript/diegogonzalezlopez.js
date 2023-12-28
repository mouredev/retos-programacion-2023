const testInput = '66-666666-6-88-777-2222-0-222-2-22-777-666-66';

const t9Keyboard = [[' '],[',','.','?','!'],['A','B','C'],['D','E','F'],['G','H','I'],['J','K','L'],['M','N','O'],['P','Q','R','S'],['T','U','V'],['W','X','Y','Z']];

const regexp = /^[0-9]+$/;

function textFromT9(input) {

  // separamos los grupos de pulsaciones en un array
  const arrayInputs = input.split('-');

  // creamos una variable como string vacía donde iremos metiendo los caracteres de salida del teclado t9
  let result = '';

  for (element of arrayInputs) {

    // chequeamos que la entrada solo contenga números
    if (!regexp.test(element)) {
      return 'La entrada debe contener solo grupos de números separados por -';
    }

    // obtenemos la cantidad de pulsaciones de cada elemento del array
    let pulsations = element.length;

    // en el teclado t9, al llegar al último valor de una tecla, la siguiente pulsación vuelve al primer valor, por lo que corregimos el valor de la variable 'pulsations' restando el total de valores de la tecla correspondiente siempre que 'pulsations' supere dicho valor
    while (pulsations > t9Keyboard[element[0]].length) pulsations -= t9Keyboard[element[0]].length;

    // añadimos el caracter correspondiente de cada grupo de pulsaciones al resultado
    result += t9Keyboard[element[0]][pulsations-1];

  }

  return result;

}

console.log(textFromT9(testInput));
