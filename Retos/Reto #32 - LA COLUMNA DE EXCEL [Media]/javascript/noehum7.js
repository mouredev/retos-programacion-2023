function columnNumberExcel(name) {
  const alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'];

  return name.split("").reduce((acc, currentValue, index) => {
    const indice = alphabet.findIndex(letter => letter === currentValue) + 1;
    acc += indice * Math.pow(alphabet.length, (name.length - index - 1));
    return acc;
  }, 0)
}

console.log(columnNumberExcel("DC"));
