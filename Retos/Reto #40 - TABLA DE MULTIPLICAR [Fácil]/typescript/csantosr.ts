const tabla = (num: number): string => {
  return `\tTabla del ${num}
  
  \t${Array(10).fill(null).map((_, n) => `${num} x ${n+1} = ${num*(n+1)}`).join('\n\t')}`
}

console.log(tabla(7))