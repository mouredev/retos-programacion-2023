/*
 * Crea tres test sobre el reto 12: "Viernes 13".
 * - Puedes copiar una solución ya creada por otro usuario en
 *   el lenguaje que estés utilizando.
 * - Debes emplear un mecanismo de ejecución de test que posea
 *   el lenguaje de programación que hayas seleccionado.
 * - Los tres test deben de funcionar y comprobar
 *   diferentes situaciones (a tu elección).
 */

// Visita mi repo en GitHub para ver y correr los tests de este código --> https://github.com/marcode24/weekly-challenges

const includesFriday13 = require('../12-viernes-13/solution');

describe('Challenge 12: Viernes 13', () => {
  const testCases = [
    {
      input: [2, 2016],
      output: false,
    },
    {
      input: [4, 1990],
      output: true,
    },
    {
      input: [7, 1990],
      output: true,
    },
    {
      input: [11, 2009],
      output: true,
    },
    {
      input: [8, 2010],
      output: true,
    },
    {
      input: [5, 2011],
      output: true,
    },
    {
      input: [1, 1985],
      output: false,
    },
    {
      input: [8, 2021],
      output: true,
    },
    {
      input: [1, 2023],
      output: true,
    },
    {
      input: [10, 2023],
      output: true,
    },
  ];

  it('should return a boolean type', () => {
    expect(typeof includesFriday13(1, 2023)).toBe('boolean');
  });

  it.each(testCases)('should return $output', (testCase) => {
    expect(includesFriday13(...testCase.input)).toBe(testCase.output);
  });
});

// Visita mi repo en GitHub para ver y correr los tests de este código --> https://github.com/marcode24/weekly-challenges
