import { describe, test } from "node:test";
import assert from "node:assert/strict";

const tecladoT9 = (secuencia) => {

  // TABLA DE DIGITOS
  const tabla = {
    "0": [" "],
    "2": ['A', 'B', 'C'],
    "3": ['D', 'E', 'F'],
    "4": ['G', 'H', 'I'],
    "5": ['J', 'K', 'L'],
    "6": ['M', 'N', 'O'],
    "7": ['P', 'Q', 'R', 'S'],
    "8": ['T', 'U', 'V'],
    "9": ['W', 'X', 'Y', 'Z']
  }

  // Se inicializa la cadena
  let cadena = "";

  // Se extraen los digitos y se guardan en un array
  const secuenciaPartida = secuencia.split("-");

  for (const digito of secuenciaPartida) {

    // Primero se comprueba si solo hay sólo digito, por lo que se añade
    // a la cadena el primer elemento que tenga la clave ese dígito.
    // En caso opuesto, se añadirá la cadena el valor que hay dentro de la
    // clave de ese dígito, utilizando la longitud de ese digito - 1.
    if (digito.length === 1) {
      cadena += tabla[digito[0]][0]
    } else {
      cadena += tabla[digito[0]][digito.length - 1]
    }
  }

  return cadena;
}

/* TESTS */
describe("Tests del teclado T9", () => {
  test("Debe devolver PEPE", () => {
    const resultado = tecladoT9("7-33-7-33");
    assert.equal(resultado, "PEPE");
  });
  test("Debe devolver MOUREDEV", () => {
    const resultado = tecladoT9("6-666-88-777-33-3-33-888");
    assert.equal(resultado, "MOUREDEV");
  });
  test("Debe devolver MIDUDEV", () => {
    const resultado = tecladoT9("6-444-3-88-3-33-888");
    assert.equal(resultado, "MIDUDEV");
  });
  test("Debe devolver FEDERICO", () => {
    const resultado = tecladoT9("333-33-3-33-777-444-222-666");
    assert.equal(resultado, "FEDERICO");
  });
  test("Debe devolver MOMO", () => {
    const resultado = tecladoT9("6-666-6-666");
    assert.equal(resultado, "MOMO");
  });
  test("Debe devolver MIKA", () => {
    const resultado = tecladoT9("6-444-55-2");
    assert.equal(resultado, "MIKA");
  });
  test("Debe devolver PATRISIO", () => {
    const resultado = tecladoT9("7-2-8-777-444-7777-444-666");
    assert.equal(resultado, "PATRISIO");
  });
  test("Debe devolver CARLOS AZAUSTRE", () => {
    const resultado = tecladoT9("222-2-777-555-666-7777-0-2-9999-2-88-7777-8-777-33");
    assert.equal(resultado, "CARLOS AZAUSTRE");
  });
})
