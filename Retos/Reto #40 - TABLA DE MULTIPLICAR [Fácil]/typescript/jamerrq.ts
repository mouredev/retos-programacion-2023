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
