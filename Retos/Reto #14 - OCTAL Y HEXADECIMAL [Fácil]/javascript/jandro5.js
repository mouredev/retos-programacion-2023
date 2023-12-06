// Bases
const hexadecimal = [0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F']
const octal = [0,1,2,3,4,5,6,7]
const binario = [0,1]

// Función nativa
function decTo(num, base){
    return num.toString(base)
}

// Función manual
function decToBase(num, base) {
	let operador = base.length
  let final = ''

  while (num >= operador) {
  	final = base[num % operador] + final
  	num = parseInt(num / operador)
  }
  final = base[num] + final
	
	return final
}

// Ejemplo en: https://jsfiddle.net/jandro5/v9xd0r4o/

// Comprobaciones
console.log(decTo(85500, 16) , decToBase(85500, hexadecimal))
console.log(decTo(5, 16) , decToBase(5, hexadecimal))
console.log(decTo(85500, 8) , decToBase(85500, octal))
console.log(decTo(5, 8) , decToBase(5, octal))
console.log(decTo(85500, 2) , decToBase(85500, binario))
console.log(decTo(5, 2) , decToBase(5, binario))
