/*
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 */

function fizzBuzz() {
  Array.from({ length: 100 }, (_, i) => i + 1).forEach(num => {
    const isBy3 = num % 3 === 0;
    const isBy5 = num % 5 === 0;
    if (isBy3 && isBy5) {
      console.log('fizzbuzz');
    } else if (isBy3) {
      console.log('fizz');
    } else if (isBy5) {
      console.log('buzz');
    } else {
      console.log(num);
    }
  });
}

function test() {
  // Arrange
  let myOutput = '';
  const log = console.log;
  console.log = arg => {
    log(arg);
    myOutput += `${arg}\n`;
  };

  // Act
  fizzBuzz();

  // Assert
  console.log = log;
  const expectedOutput =
    [
      1,
      2,
      'fizz',
      4,
      'buzz',
      'fizz',
      7,
      8,
      'fizz',
      'buzz',
      11,
      'fizz',
      13,
      14,
      'fizzbuzz',
      16,
      17,
      'fizz',
      19,
      'buzz',
      'fizz',
      22,
      23,
      'fizz',
      'buzz',
      26,
      'fizz',
      28,
      29,
      'fizzbuzz',
      31,
      32,
      'fizz',
      34,
      'buzz',
      'fizz',
      37,
      38,
      'fizz',
      'buzz',
      41,
      'fizz',
      43,
      44,
      'fizzbuzz',
      46,
      47,
      'fizz',
      49,
      'buzz',
      'fizz',
      52,
      53,
      'fizz',
      'buzz',
      56,
      'fizz',
      58,
      59,
      'fizzbuzz',
      61,
      62,
      'fizz',
      64,
      'buzz',
      'fizz',
      67,
      68,
      'fizz',
      'buzz',
      71,
      'fizz',
      73,
      74,
      'fizzbuzz',
      76,
      77,
      'fizz',
      79,
      'buzz',
      'fizz',
      82,
      83,
      'fizz',
      'buzz',
      86,
      'fizz',
      88,
      89,
      'fizzbuzz',
      91,
      92,
      'fizz',
      94,
      'buzz',
      'fizz',
      97,
      98,
      'fizz',
      'buzz',
    ].join('\n') + '\n';
  if (myOutput === expectedOutput) {
    console.log('✅ PASS');
  } else {
    expectedOutput;
    console.log('❌ FAIL', {
      expected: expectedOutput,
      received: myOutput,
    });
  }
}

test();
