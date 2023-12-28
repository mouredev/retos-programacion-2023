function passwordGenerator(length, upper, numbers, symbols) {   
  
  let characters = "abcdefghijklmnopqrstuvwxyz";
  let characterUpper = characters.toUpperCase();
  let numbersCharacters = "0123456789";
  let symbolsCharacters = "!#$%&/()=?¡¿";
  let allCharacters = "";
  let password = "";

  for (let i = 0; i < length; i++) {
    if (upper) {
      allCharacters += characters + characterUpper;
    } else {
      allCharacters += characters;
    }
    if (numbers) {
      allCharacters += numbersCharacters;
    }
    if (symbols) {
      allCharacters += symbolsCharacters;
    }
    random = Math.floor(Math.random() * allCharacters.length);
    password += allCharacters.charAt(random);
  }
  console.log(password);
  return password;
}
passwordGenerator(8); 
passwordGenerator(8, true, true, true); 
passwordGenerator(10, false, true, true);
passwordGenerator(13, true, true, true);
passwordGenerator(16, true, false, true);
passwordGenerator(20, true, true, true);
passwordGenerator(8, false, false, false);
passwordGenerator(10, true, true, false);
passwordGenerator(14, false, false, true);

