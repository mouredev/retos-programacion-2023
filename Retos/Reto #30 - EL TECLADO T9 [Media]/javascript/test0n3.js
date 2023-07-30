//
// Los primeros dispositivos móviles tenían un teclado llamado T9
// con el que se podía escribir texto utilizando únicamente su
// teclado numérico (del 0 al 9).
//
// Crea una función que transforme las pulsaciones del T9 a su
// representación con letras.
// - Debes buscar cuál era su correspondencia original.
// - Cada bloque de pulsaciones va separado por un guión.
// - Si un bloque tiene más de un número, debe ser siempre el mismo.
// - Ejemplo:
//     Entrada: 6-666-88-777-33-3-33-888
//     Salida: MOUREDEV
//

const cellphoneDial = (input) => {
  const dial = {
    1: "1",
    2: "ABC2",
    3: "DEF3",
    4: "GHI4",
    5: "JKL5",
    6: "MNO6",
    7: "PQRS7",
    8: "TUV8",
    9: "WXYZ9",
    0: " 0",
    "*": "*",
    "#": "#",
  };

  return input
    .split("-")
    .map((char) => {
      let char_pos = (char.length % dial[char[0]].length) - 1;
      return dial[char[0]].slice(char_pos)[0];
    })
    .join("");
};

const tests = {
  inputs: [
    "6-666-88-777-33-3-33-888",
    "8-444-6-33-0-8-666-0-7777-555-33-33-7",
    "6-999-0-66-88-6-22-33-777-0-444-7777-0-99999-4444-77777-0-4444-2222-2222-0-3333-2222-4444",
    "6-99999999-0-8-33-777777777-8",
  ],
  outputs: ["MOUREDEV", "TIME TO SLEEP", "MY NUMBER IS 947 422 324", "MY TEST"],
};

let errors = 0;
tests.inputs.forEach((input, index) => {
  const result = cellphoneDial(input);
  if (result != tests.outputs[index]) {
    errors += 1;
    console.log(
      `Error - input: ${input}, expected: ${tests.outputs[index]}, result: ${result}`
    );
  }
});
console.log(`Errors: ${errors}`);
