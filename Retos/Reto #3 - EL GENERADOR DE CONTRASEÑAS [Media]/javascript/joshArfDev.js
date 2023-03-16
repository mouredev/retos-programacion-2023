const passwordGenerate = (range, uppercase, numbers, symbols) => {
  //space to our password
  let password = "";

  //features for our password
  const capitalLetters = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ";
  const lowerLetters = "abcdefghijklmnñopqrstuvwxyz";
  const number = "123456789";
  const symbol = ".?,;-_¡!¿*%&$/()[]{}|@><";

  //bind everything
  let bind = "";

  //scenarios
  //with or without uppercase
  uppercase ? (bind += capitalLetters) : (bind += lowerLetters);

  //with or without numbers
  numbers ? (bind += number) : bind;

  //with or without symbols
  symbols ? (bind += symbol) : bind;

  //controling the length of our password
  if (range >= 8 && range <= 16) {
    for (let index = 0; index < range; index++) {
      let generating = Math.floor(Math.random() * bind.length);
      password += bind.charAt(generating);
    }
  } else {
    return `Error: length ${range} for your password is not permitted`;
  }

  return `Your password is: ${ password }`
};

console.log( passwordGenerate( 4, true, true, true ) )
