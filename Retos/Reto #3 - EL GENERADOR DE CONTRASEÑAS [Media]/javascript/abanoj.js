/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */

const rangeGenerator = (start=0, stop, step=1) => {
  return Array.from({ length: (stop - start) / step + 1}, (_, i) => start + (i * step));
}

const retoTres = (length = 8, capital = false, numbers = false, symbols = false ) => {
  let options = rangeGenerator(97,122).map(e => String.fromCharCode(e));
  let password = '';

  if(length < 8) length = 8;
  if(length > 16) length = 16;

  if(capital)
    options = options.concat(rangeGenerator(65,90).map(e => String.fromCharCode(e)));

  if(numbers)
    options = options.concat(rangeGenerator(48,57).map(e => String.fromCharCode(e)));

  if(symbols){
    options = options.concat(rangeGenerator(33,47).map(e => String.fromCharCode(e)));
    options = options.concat(rangeGenerator(58,64).map(e => String.fromCharCode(e)));
    options = options.concat(rangeGenerator(91,96).map(e => String.fromCharCode(e)));
  }
    
  console.log(options);
  for (let i = 0; i < length; i++) {
    password += options[Math.floor(Math.random() * options.length)];
  }
  return password;
}

retoTres()