'use strict';

function helloWorld() {
  return '¡Hola Mundo!';
}

module.exports = { helloWorld };

if (require.main === module) console.log(helloWorld());
