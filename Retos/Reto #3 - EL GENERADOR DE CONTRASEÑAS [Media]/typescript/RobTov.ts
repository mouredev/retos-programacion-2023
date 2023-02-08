const letters: string = [...Array(26).keys()]
  .map((_, i) => i + 65)
  .map((c) => String.fromCharCode(c))
  .join("");
const digits: string = [...Array(10).keys()].join("");
const symbols: string = `!"#$%&'()*+,-./:;<=>?@[\\]^_\`{|}~`;

function passwordGenerator(
  len: number,
  up: boolean,
  dig: boolean,
  sym: boolean
): string {
  if (len < 8 || len > 16) {
    throw new Error("Debe tener una longitud entre 8 y 16 caracteres");
  }
  let valList =
    letters.toLowerCase() +
    (up ? letters : "") +
    (dig ? digits : "") +
    (sym ? symbols : "");
  let psswrd = "";
  for (let i = 0; i < len; i++) {
    psswrd += valList[Math.floor(Math.random() * valList.length)];
  }

  return psswrd;
}

const start = () => {
  console.log(passwordGenerator(8, false, false, false));
  console.log(passwordGenerator(9, true, false, false));
  console.log(passwordGenerator(10, false, true, false));
  console.log(passwordGenerator(11, false, false, true));
  console.log(passwordGenerator(12, true, true, false));
  console.log(passwordGenerator(13, true, false, true));
  console.log(passwordGenerator(14, false, true, true));
  console.log(passwordGenerator(15, true, true, true));
};

start();
