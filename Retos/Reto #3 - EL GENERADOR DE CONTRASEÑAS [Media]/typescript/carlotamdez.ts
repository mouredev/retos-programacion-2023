/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */
const LENGTH_DEFAULT = 10;

const lettersLowerArray = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'];

const lettersUpperArray = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'];

const numbersArray = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'];

const caracteresArray = [
  '!', '@', '#', '$', '%', '&', '*', '(', ')', '-', '+', '=', 
  '[', ']', '{', '}', '|', '/', '\\', ':', ';', ',', '.', '<', '>', 
  '?', '_', '^', '~', '`'
];

const generate = (long?: number, mayus?: boolean, num?:boolean, simb?: boolean) => {
  const longitud = long == undefined? LENGTH_DEFAULT : long<17 && long>7 ? long : LENGTH_DEFAULT;
  const password = generatorAll(longitud,mayus,num,simb);
  console.log(password);
}

const generatorAll = (long: number, mayus?: boolean, num?: boolean, simb?: boolean): string => {
  const options: string[] = [];
  if (!mayus) options.push(...lettersLowerArray);
  if (mayus) options.push(...lettersLowerArray, ...lettersUpperArray);
  if (num) options.push(...numbersArray);
  if (simb) options.push(...caracteresArray);

  const password: string[] = [];
  for (let i = 0; i < long; i++) {
    const randomIndex = generarNumeroAleatorio(0, options.length);
    password.push(options[randomIndex]);
  }

  return password.join('');
};


function generarNumeroAleatorio(minimo: number, maximo: number) {
  const numeroAleatorio = Math.floor(Math.random() * (maximo - minimo)) + minimo;
  return numeroAleatorio;
}



generate(1,false,true,true);
