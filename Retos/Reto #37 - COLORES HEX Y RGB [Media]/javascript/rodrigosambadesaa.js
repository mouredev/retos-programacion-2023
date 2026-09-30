'use strict';

function rgbToHex(red, green, blue) {
  const values = [red, green, blue];
  if (!values.every(value => Number.isInteger(value) && value >= 0 && value <= 255)) {
    throw new Error('Los valores RGB deben estar entre 0 y 255');
  }
  return `#${values.map(value => value.toString(16).padStart(2, '0')).join('').toUpperCase()}`;
}

function hexToRgb(hex) {
  const match = String(hex).match(/^#?([0-9a-f]{6})$/i);
  if (!match) throw new Error('Color HEX no válido');
  return {
    r: parseInt(match[1].slice(0, 2), 16),
    g: parseInt(match[1].slice(2, 4), 16),
    b: parseInt(match[1].slice(4, 6), 16)
  };
}

module.exports = { rgbToHex, hexToRgb };

if (require.main === module) {
  console.log(rgbToHex(46, 204, 113));
  console.log(hexToRgb('#2ECC71'));
}
