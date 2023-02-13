/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
*/

type genPassProps = {
  long: number;
  mayusc: boolean;
  numbers: boolean;
  symbols: boolean;
};

const lowerLetters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
];
const upperLetter = lowerLetters.map((letter: string) => letter.toUpperCase());
const defaultNumbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"];
const defaultSymbols = ["|", "°", "!", "#", "$", "%", "&", "/", "(", ")", "=", "?", "¡", "¿", "{", "}", "[", "]", "+", "*", "_", "@", ":", "-",
];

function checkLong(long: number): boolean {
  return long >= 8 && long <= 16 ? true : false;
}

function genRandomIndex(min: number, max: number): number {
  return parseInt((Math.random() * (max - min) + min).toString());
}

function genPass({ long, mayusc, numbers, symbols }: genPassProps): string {
  let password = "";

  if (!checkLong(long)) {
    return `ERROR: Long must be beetwen 8 and 16`;
  }

  for (let i = 0; i <= long; i++) {
    if (mayusc) {
      password += upperLetter[genRandomIndex(0, 26)];
      password += lowerLetters[genRandomIndex(0, 26)];
    } else {
      password += lowerLetters[genRandomIndex(0, 26)];
    }

    if (numbers) {
      password += defaultNumbers[genRandomIndex(0, 9)];
    }

    if (symbols) {
      password += defaultSymbols[genRandomIndex(0, 23)];
    }
  }

  password = password
    .slice(0, long)
    .split("")
    .sort(() => Math.random() - 0.5)
    .join("");

  return `Your password is: ${password}`;
}

function main() {
  const coldPass = genPass({
    long: 8,
    mayusc: false,
    numbers: true,
    symbols: false,
  });
  console.log(coldPass);

  const jxPass = genPass({
    long: 12,
    mayusc: false,
    numbers: true,
    symbols: true,
  });
  console.log(jxPass);

  const rxPass = genPass({
    long: 16,
    mayusc: true,
    numbers: false,
    symbols: true,
  });
  console.log(rxPass);
}

main();
