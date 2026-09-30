'use strict';

function hasFridayThe13th(month, year) {
  if (!Number.isInteger(month) || month < 1 || month > 12 || !Number.isInteger(year)) {
    throw new Error('Mes o año no válido');
  }
  return new Date(Date.UTC(year, month - 1, 13)).getUTCDay() === 5;
}

module.exports = { hasFridayThe13th };

if (require.main === module) console.log(hasFridayThe13th(Number(process.argv[2]), Number(process.argv[3])));
