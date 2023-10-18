/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */

function randInt(min_: number, max_: number): number {
  const min = Math.ceil(min_);
  const max = Math.floor(max_);
  return min + Math.floor(Math.random() * (max - min + 1));
}

function generatePassword(size: number, allowedChars: string): string {
  return Array.from({ length: size }, () => allowedChars[randInt(0, allowedChars.length - 1)]).join(
    '',
  );
}

const LOWERCASE_CHARS = 'abcdefghijklmnopqrstuvwxyz';
const UPPERCASE_CHARS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
const NUMBERS = '0123456789';
const SYMBOLS = '!@#$%^&*()_+-={}[]|:;\\"\'`>,.?/';

function generateAllowedCharsChecker(allowedChars: string) {
  return (received: string) => received.split('').some(char => allowedChars.includes(char));
}

interface Props {
  size?: number;
  uppercase?: boolean;
  numbers?: boolean;
  symbols?: boolean;
}

function passwordGenerator({
  size = 8,
  uppercase = true,
  numbers = true,
  symbols = true,
}: Props = {}): string {
  if (size < 8 || size > 16) {
    throw new Error('Invalid size. Must have between 8 and 16 characters (both inclusive).');
  }
  const conditions = [generateAllowedCharsChecker(LOWERCASE_CHARS)];
  let allowedChars = LOWERCASE_CHARS;

  if (uppercase) {
    allowedChars += UPPERCASE_CHARS;
    conditions.push(generateAllowedCharsChecker(UPPERCASE_CHARS));
  }

  if (numbers) {
    allowedChars += NUMBERS;
    conditions.push(generateAllowedCharsChecker(NUMBERS));
  }

  if (symbols) {
    allowedChars += SYMBOLS;
    conditions.push(generateAllowedCharsChecker(SYMBOLS));
  }

  let randomChars = generatePassword(size, allowedChars);
  while (!conditions.every(condition => condition(randomChars))) {
    randomChars = generatePassword(size, allowedChars);
  }

  return randomChars;
}

function test() {
  // Arrange
  // Act
  const received = passwordGenerator();
  console.log({ received });

  // Assert
  const conditions = [
    (received: string) => received.length === 8,
    generateAllowedCharsChecker(LOWERCASE_CHARS),
    generateAllowedCharsChecker(UPPERCASE_CHARS),
    generateAllowedCharsChecker(NUMBERS),
    generateAllowedCharsChecker(SYMBOLS),
  ];
  conditions.every(condition => {
    const hasPassed = condition(received);
    if (hasPassed) {
      console.log('✅ PASSED');
    } else {
      console.log('❌ FAILED', condition.toString());
    }
    return hasPassed;
  });
}

test();
