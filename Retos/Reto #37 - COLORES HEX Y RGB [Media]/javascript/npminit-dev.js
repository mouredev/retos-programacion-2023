/*
 * Crea las funciones capaces de transformar colores HEX
 * a RGB y viceversa.
 * Ejemplos:
 * RGB a HEX: r: 0, g: 0, b: 0 -> #000000
 * HEX a RGB: hex: #000000 -> (r: 0, g: 0, b: 0)
 */

function fromHexToRGB(hex) {
  if(hex.length !== 4 && hex.length !== 7) throw new Error('invalid hex format, only #xxx and #xxxxxx allowed')
  let rgb = [];
  let number = hex.slice(1);
  let step = number.length / 3
  for(let i = 0; i < number.length; i += step) 
    step === 2 ? 
    rgb.push(parseInt(`${number[i]}${number[i + 1]}`, 16)) :
    rgb.push(parseInt(`${number[i]}${number[i]}`, 16))
  return `rgb(${rgb.join(', ')})`
}

function fromRGBToHex(rgb) {
  if(!/rgb\(\d{1,3}, ?\d{1,3}, ?\d{1,3}\)/gmi.test(rgb)) throw new Error('invalid rgb format, only rgb(xxx,xxx,xxx) or RGB(xxx, xxx, xxx) without spaces optionally, allowed')
  let numbers = rgb.slice(4, rgb.length - 1)
  numbers = numbers.split(',')
  if(numbers.some(num => parseInt(num) > 255)) throw new Error('rgb value out of bounds! range must be a number between 0 and 255 (both included)')
  for(let i = 0; i < numbers.length; i++) {
    let hexFrag = parseInt(numbers[i]).toString(16)
    hexFrag = hexFrag.padStart(2, 0)
    numbers[i] = hexFrag
  }
  return `#${numbers.join('')}`
}

/* TESTS */

console.log(fromHexToRGB('#AFB')) // rgb(170, 255, 187)
console.log(fromHexToRGB('#F5F5F5')) // rgb(245, 245, 245)
console.log(fromHexToRGB('#abba17')) // rgb(171, 186, 23)
console.log(fromHexToRGB('#56aaBB')) // rgb(86, 170, 187)
console.log(fromHexToRGB('#000')) // rgb(0, 0, 0)
// console.log(fromHexToRGB('#1234')) throws an 'hex format' error!!

console.log(fromRGBToHex('rgb(255, 255, 255)'))
console.log(fromRGBToHex('rgb(0, 0, 0)'))
console.log(fromRGBToHex('RGB(145, 10, 1)'))
console.log(fromRGBToHex('rgb(11, 120, 0)'))
console.log(fromRGBToHex('rgb(98, 155, 20)')) 
// console.log(fromRGBToHex('RGB(12,,201)')) throws an 'rgb format' error!!
// console.log(fromRGBToHex('rgb(256, 0, 0)')) throws an 'out of range' error!!


