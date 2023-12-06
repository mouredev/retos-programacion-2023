/*
 * Crea 3 funciones, cada una encargada de detectar si una cadena de
 * texto es un heterograma, un isograma o un pangrama.
 * - Debes buscar la definición de cada uno de estos términos.
 */

type Input = string;
type Output = boolean;

function isHeterogram(str: Input): Output {
  const charCount: Record<string, number> = {};

  str
    .toLowerCase()
    .replace(/\W/, '')
    .split('')
    .forEach(char => {
      if (charCount[char]) {
        charCount[char]++;
      } else {
        charCount[char] = 1;
      }
    });

  return Object.values(charCount).every(count => count === 1);
}

function isIsogram(str: Input): Output {
  const charCount: Record<string, number> = {};

  str
    .toLowerCase()
    .replace(/\W/, '')
    .split('')
    .forEach(char => {
      if (charCount[char]) {
        charCount[char]++;
      } else {
        charCount[char] = 1;
      }
    });

  return Object.values(charCount).every((count, i, array) => count === array[0]);
}

function isPangram(str: Input): Output {
  const charCount: Record<string, number> = {};

  str
    .toLowerCase()
    .replace(/\W/, '')
    .split('')
    .forEach(char => {
      if (charCount[char]) {
        charCount[char]++;
      } else {
        charCount[char] = 1;
      }
    });

  const a = 'a'.charCodeAt(0);
  const z = 'z'.charCodeAt(0);
  const alphabet = Array.from({ length: z - a + 1 }, (_, i) => String.fromCharCode(a + i));

  const sentenceChars = Object.keys(charCount);
  return alphabet.every(char => sentenceChars.includes(char));
}

const heterogramCases: { input: Input; expected: Output }[] = [
  {
    input: 'yuxtaponer',
    expected: true,
  },
  {
    input: 'centrifugado',
    expected: true,
  },
  {
    input: 'luteranismo',
    expected: true,
  },
  {
    input: 'adulterinos',
    expected: true,
  },
  {
    input: 'hiperblanduzcos',
    expected: true,
  },
];
heterogramCases.every(({ input, expected }) => {
  const received = isHeterogram(input);
  const hasPassed = received === expected;
  if (received === expected) {
    console.log('✅ PASSED');
  } else {
    console.log('❌ FAILED', { expected, received });
  }
  return hasPassed;
});

const isogramCases: { input: Input; expected: Output }[] = [
  {
    input: 'horseshoer',
    expected: true,
  },
  {
    input: 'race caller',
    expected: true,
  },
  {
    input: 'intestines',
    expected: true,
  },
  {
    input: 'Shanghaiings',
    expected: true,
  },
];
isogramCases.every(({ input, expected }) => {
  const received = isIsogram(input);
  const hasPassed = received === expected;
  if (received === expected) {
    console.log('✅ PASSED');
  } else {
    console.log('❌ FAILED', { expected, received });
  }
  return hasPassed;
});

const pangramCases: { input: Input; expected: Output }[] = [
  {
    input:
      'Benjamín pidió una bebida de kiwi y fresa. Noé, sin vergüenza, la más exquisita champaña del menú.',
    expected: true,
  },
];
pangramCases.every(({ input, expected }) => {
  const received = isPangram(input);
  const hasPassed = received === expected;
  if (received === expected) {
    console.log('✅ PASSED');
  } else {
    console.log('❌ FAILED', { expected, received });
  }
  return hasPassed;
});
