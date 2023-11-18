function abaco(numero) {
  return numero.toString().padStart(7, '0').split('')
    .map(x => Number(x))
    .map(digit => `${'0'.repeat(digit)}---${'0'.repeat(9 - digit)}`);
}

[1302790, 0, 9999999].forEach(n => {
  console.log(n);
  console.log(abaco(n));
});
