'use strict';

const delay = milliseconds => new Promise(resolve => setTimeout(resolve, milliseconds));

async function countdown(start, seconds, write = console.log, wait = delay) {
  if (!Number.isInteger(start) || start < 1 || !Number.isInteger(seconds) || seconds < 1) {
    throw new Error('Los parámetros deben ser enteros positivos');
  }
  const values = [];
  for (let value = start; value >= 0; value--) {
    values.push(value);
    write(value);
    if (value > 0) await wait(seconds * 1000);
  }
  return values;
}

module.exports = { countdown };

if (require.main === module) countdown(Number(process.argv[2] ?? 5), Number(process.argv[3] ?? 1)).catch(console.error);
