'use strict';

const assert = require('node:assert/strict');

function hasFridayThe13th(month, year) {
  if (!Number.isInteger(month) || month < 1 || month > 12 || !Number.isInteger(year)) {
    throw new Error('Mes o año no válido');
  }
  return new Date(Date.UTC(year, month - 1, 13)).getUTCDay() === 5;
}

function runTests() {
  assert.equal(hasFridayThe13th(1, 2023), true, 'enero de 2023 tuvo viernes 13');
  assert.equal(hasFridayThe13th(2, 2023), false, 'febrero de 2023 no tuvo viernes 13');
  assert.throws(() => hasFridayThe13th(13, 2023), /no válido/, 'un mes fuera de rango se rechaza');
  return 3;
}

module.exports = { hasFridayThe13th, runTests };

if (require.main === module) console.log(`${runTests()} tests superados`);
