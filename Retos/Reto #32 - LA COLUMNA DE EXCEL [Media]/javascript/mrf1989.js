// Author: mrf1989

const ALPHABET = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
  "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"];

try {
  const userInput = prompt("Introduce la columna de la hoja de cálculo\nPor ejemplo, AA:")
    .toUpperCase()
    .trim();
  // TODO: Se podría introducir un validador, por ejemplo, para evitar números en el input.

  const input = userInput.split("").reverse();

  let acum = 0;
  for (let i = 0; i <= input.length; i++) {
    acum += ((ALPHABET.length ** i) * (ALPHABET.indexOf(input[i]) + 1));
  }

  const res = `La columna introducida, ${userInput}, corresponde con el número ${acum}.`;
  console.log(res);
  alert(res);
}
catch (error) {
  console.error("Se ha cancelado la operación");
}
