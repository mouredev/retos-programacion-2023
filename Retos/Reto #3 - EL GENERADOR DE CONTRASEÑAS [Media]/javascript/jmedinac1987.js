"use strict";

let parameters = {
  Length: 16,
  CapitalLetters: true,
  Numbers: true,
  Symbols: true,
};

let response = passwordGenerator(parameters);

console.log(`length: ${response.length} - `, `Password: ${response}`);

function passwordGenerator(parameters) {

  let formatSymbols = /[`!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?~]/;
  let formatCapitalLetters = /[A-Z]/;
  let formatNumbers = /[0-9]/;
  let password = "";

  if (parameters.Length === undefined)
    return "It is necessary to define a length between 8 and 16 characters";

  if (parameters.Length < 8 || parameters.Length > 16)
    return `length parameter does not meet supported length, supported length between 8 and 16 supplied length ${parameters.Length}`;

  password = prePassword(parameters.Length);

  if (parameters.CapitalLetters) {
    password = addCapitalLetters(password);
  }

  if (parameters.Numbers) {
    password = addNumbers(password);
  }

  if (parameters.Symbols) {
    password = addSymbols(password);
  }

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

function prePassword(Length) {
  let letters = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", 
    "j", "k", "l", "m", "n", "o", "p", "q", "r", 
    "s", "t", "u", "v", "w", "x", "y", "z" ];

  let prePassword = "";

  for (let i = 0; i < Length; i++) {
    let random = Math.floor(Math.random() * (Length - 0 + 1) + 0);
    prePassword += letters[random];
  }

  return prePassword;
}

function addCapitalLetters(prePassword) {
  let arrayText = [];
  let newPrePassword = "";
  arrayText = prePassword.split("");

  for (let i = 0, j = arrayText.length; i < j; i++) {
    let random = Math.floor(Math.random() * (j - 0 + 1) + 0);
    arrayText[random] = prePassword.charAt(random).toUpperCase();
  }

  arrayText.forEach((letter) => {
    newPrePassword += letter;
  });

  return newPrePassword;
}

function addNumbers(prePassword) {
  let numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];

  let arrayText = [];
  let newPrePassword = "";
  arrayText = prePassword.split("");

  for (let i = 0, j = arrayText.length; i < j; i++) {
    let random = Math.floor(Math.random() * (j - 0 + 1) + 0);
    if (arrayText[random] != undefined)
      arrayText[random] = numbers[i] ?? arrayText[random];
  }

  arrayText.forEach((character) => {
    newPrePassword += character;
  });

  return newPrePassword;
}

function addSymbols(prePassword) {
  let symbols = [
    "|", "¬", "!", "#", "$", "%", "&", "/", "\\", "(", ")", "=", "?", 
    "¿", "¡", "*", "-", "+", "[", "]", "}", "{", "-", "_", ";", ",",
    ".", ":", "°", "<", ">", "'" ];

  let arrayText = [];
  let newPrePassword = "";
  arrayText = prePassword.split("");

  for (let i = 0, j = arrayText.length; i < j; i++) {
    let random = Math.floor(Math.random() * (j - 0 + 1) + 0);
    if (arrayText[random] != undefined)
      arrayText[random] = symbols[i] ?? arrayText[random];
  }

  arrayText.forEach((character) => {
    newPrePassword += character;
  });

  return newPrePassword;
}