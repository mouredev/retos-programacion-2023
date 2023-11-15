const LABELS = [
  // 0 - 6
  'A', 'B', 'C', 'D', 'E', 'F', 'G',
  // 7 - 13
  'H', 'I', 'J', 'K', 'L', 'M', 'N',
  // 14 - 20
  'O', 'P', 'Q', 'R', 'S', 'T', 'U',
  // 21 - 25
  'V', 'W', 'X', 'Y', 'Z'];
function columnIndex(columnText) {
  const letters = columnText.toUpperCase().split('');
  return letters.reduce((total, digit) => total * 26 + LABELS.indexOf(digit) + 1, 0);
}

['A', 'AA', 'CA', 'ZZ'].forEach(test => console.log(`Índice para ${test}=${columnIndex(test)}`));
