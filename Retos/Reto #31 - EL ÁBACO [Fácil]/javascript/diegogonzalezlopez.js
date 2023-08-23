const arrayAbacus = ['O---OOOOOOOO',
  'OOO---OOOOOO',
  '---OOOOOOOOO',
  'OO---OOOOOOO',
  'OOOOOOO---OO',
  'OOOOOOOOO---',
  '---OOOOOOOOO'];

function returnNumber(array) {

  let multiplicator = 1000000;
  let result = 0;

  for (element of array) {
    let counter = 0;
    for (char of element) {
      if (char == 'O') counter++;
      else break;
    }
    result += counter * multiplicator;
    multiplicator = multiplicator / 10;
  }

  return result;

}

console.log(returnNumber(arrayAbacus));
