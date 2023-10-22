function multiplicacion(i: number, j: number): string {
  return `${i} x ${String(j).padStart(2)} = ${i * j}`
}

function tablaMultiplicar(numero: number): string {
  const lines = [] as string[]
  for (let i = 1; i <= 10; i++) {
    const line = multiplicacion(numero, i)
    lines.push(line)
  }
  return lines.join('\n')
}

let numero: number = 5
console.log(tablaMultiplicar(numero))
/**
5 x  1 = 5
5 x  2 = 10
5 x  3 = 15
5 x  4 = 20
5 x  5 = 25
5 x  6 = 30
5 x  7 = 35
5 x  8 = 40
5 x  9 = 45
5 x 10 = 50
 */
