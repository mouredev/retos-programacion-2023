'use strict';

function excelColumnNumber(column) {
  const value = String(column).toUpperCase();
  if (!/^[A-Z]+$/.test(value)) throw new Error('Nombre de columna no válido');
  let result = 0;
  for (const letter of value) result = result * 26 + letter.charCodeAt(0) - 64;
  return result;
}

module.exports = { excelColumnNumber };

if (require.main === module) console.log(excelColumnNumber(process.argv[2] ?? 'CA'));
