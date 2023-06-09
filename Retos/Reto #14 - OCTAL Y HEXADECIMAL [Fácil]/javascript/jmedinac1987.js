function createNewNumber(number, converTo) {
  const hexadecimal = [0,1,2,3,4,5,6,7,8,9,"A","B","C","D","E","F",];
  const octal = [0, 1, 2, 3, 4, 5, 6, 7];
    
  switch (converTo.toLowerCase()) {  
    case 'octal':        
        return convertNumber(number,octal);
    case 'hexadecimal':
        return convertNumber(number,hexadecimal);
    default:
        return 'Please, review your info, because the value of \'converTo\' is not valid: ' + converTo;        
  }
}

function convertNumber(number, base) {
  let operator = base.length;
  let result = "";

  while (number >= operator) {
    result = base[number % operator] + result;
    number = parseInt(number / operator);
  }
  result = base[number] + result;

  return result;
}

console.log(createNewNumber(678, 'Octal'));
console.log(createNewNumber(678, 'hexadEcimal'));
console.log(createNewNumber(678, 'hexadecima'));
