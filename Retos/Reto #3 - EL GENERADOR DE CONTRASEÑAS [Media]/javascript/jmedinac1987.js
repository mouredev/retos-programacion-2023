"use strict";

function passwordGenerator(parameters) {
  let formatSymbols = /[`!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?~]/;
  let formatCapitalLetters = /[A-Z]/;
  let formatNumbers = /[0-9]/;

  let password = "";
  if (parameters.Length === undefined)
    return "It is necessary to define a length between 8 and 16 characters";

  if (parameters.Length < 8 || parameters.Length > 16)
    return `length parameter does not meet supported length, supported length between 8 and 16 supplied length ${parameters.Length}`;

  password = calculatePassword(parameters);

  if (parameters.CapitalLetters && parameters.Numbers && parameters.Symbols) {
    if (
      !formatSymbols.test(password) ||
      !formatCapitalLetters.test(password) ||
      !formatNumbers.test(password)
    ) {
      password = passwordGenerator(parameters);
    }
  }

  if (parameters.CapitalLetters && parameters.Numbers) {
    if (!formatCapitalLetters.test(password) || !formatNumbers.test(password)) {
      password = passwordGenerator(parameters);
    }
  }

  if (parameters.CapitalLetters && parameters.Symbols) {
    if (!formatSymbols.test(password) || !formatCapitalLetters.test(password)) {
      password = passwordGenerator(parameters);
    }
  }

  if (parameters.Numbers && parameters.Symbols) {
    if (!formatSymbols.test(password) || !formatNumbers.test(password)) {
      password = passwordGenerator(parameters);
    }
  }

  if (parameters.CapitalLetters) {
    if (!formatCapitalLetters.test(password)) {
      password = passwordGenerator(parameters);
    }
  }

  if (parameters.Numbers) {
    if (!formatNumbers.test(password)) {
      password = passwordGenerator(parameters);
    }
  }

  if (parameters.Symbols) {
    if (!formatSymbols.test(password)) {
      password = passwordGenerator(parameters);
    }
  }

  return password;
}

function calculatePassword(parameters) {
    
  let numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
  let letters = [
    "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p"
    ,"q","r","s","t","u","v","w","x","y","z",
  ];
  let symbols = [
    "|","¬","!","#","$","%","&","/","\\","(",")","=","?","¿","¡","*",
    "-","+","[","]","}","{","-","_",";",",",".",":","°","<",">","'",
  ];

  let prePassword = ""; 

  prePassword = recalculatePassword(prePassword, parameters.Length, letters);
  
  if (parameters.CapitalLetters) {
    prePassword = recalculatePassword(prePassword, parameters.Length, []);    
  }
  
  if (parameters.Numbers) {
    prePassword = recalculatePassword(prePassword, parameters.Length, numbers)    
  }
  
  if (parameters.Symbols) {
    prePassword = recalculatePassword(prePassword, parameters.Length, symbols)    
  }

  return prePassword;
}

function recalculatePassword(prePassword, Length, characterArray){
  let newPrePassword = "";
  let arrayText = prePassword === "" ? "" : prePassword.split("");
  let recalculateLength = prePassword === "" ? Length : Length-1;

  for (let i = 0; i < recalculateLength; i++) {
    let random = Math.floor(Math.random() * recalculateLength);
    
    if(prePassword === ""){
      newPrePassword += characterArray[random];
    }else{
      if(characterArray.length === 0){        
        arrayText[random] = prePassword.charAt(random).toUpperCase();
      }else{
        arrayText[random] = characterArray[i] ?? arrayText[random];
      }      
    }      
  }

  if(prePassword != ""){
    arrayText.forEach((character) => {
      newPrePassword += character;
    });
  } 

  return newPrePassword;
}

let parameters = {
  Length: 8,
  CapitalLetters: true,
  Numbers: true,
  Symbols: true,
};

let response = passwordGenerator(parameters);

console.log(`length: ${response.length} - `, `Password: ${response}`);