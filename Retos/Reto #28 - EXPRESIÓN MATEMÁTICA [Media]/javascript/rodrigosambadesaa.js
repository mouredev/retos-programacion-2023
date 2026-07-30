'use strict';

function isValidExpression(expression) {
  const number = '[+-]?(?:\\d+(?:\\.\\d+)?|\\.\\d+)';
  const pattern = new RegExp(`^${number}(?:\\s+[+\\-*/%]\\s+${number})+$`);
  return pattern.test(String(expression));
}

module.exports = { isValidExpression };

if (require.main === module) console.log(isValidExpression(process.argv.slice(2).join(' ') || '5 + 6 / 7 - 4'));
