const getRandom = (int) => {
  return Math.floor(Math.random() * int);
};

const generatePassword = (
  length = 8,
  addUppercase = false,
  addSymbols = false,
  addNumbers = false
) => {
  const uppercase = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ";
  const lowercase = "abcdefghijklmnñopqrstuvwxyz";
  const symbols = `!@#$%^&*()_-+={}[];:'"/?\|<>,.~`;
  const numbers = "1234567890";
  let password = "",
    option = 0;

  for (let i = 0; i < length; i++) {
    option = getRandom(3);

    if (
      addUppercase === false &&
      addSymbols === false &&
      addNumbers === false
    ) {
      option = 0;
    } else if (addUppercase && addSymbols === false && addNumbers === false) {
      while (option === 3 || option === 2) {
        option = getRandom(3);
      }
    } else if (addUppercase && addSymbols && addNumbers === false) {
      while (option === 3) {
        option = getRandom(3);
      }
    } else if (addUppercase && addSymbols && addNumbers) {
      option = getRandom(3);
    } else if (addUppercase === false && addSymbols && addNumbers === false) {
      while (option === 1 || option === 3) {
        option = getRandom(3);
      }
    } else if (addUppercase === false && addSymbols && addNumbers) {
      while (option === 1) {
        option = getRandom(3);
      }
    } else if (addUppercase === false && addSymbols === false && addNumbers) {
      while (option === 1 || option === 2) {
        option = getRandom(3);
      }
    } else if (addUppercase && addSymbols === false && addNumbers) {
      while (option === 2) {
        option = getRandom(3);
      }
    }

    switch (option) {
      case 0:
        password += lowercase[getRandom(27)];
        break;
      case 1:
        password += uppercase[getRandom(27)];
        break;
      case 2:
        password += symbols[getRandom(31)];
        break;
      case 3:
        password += numbers[getRandom(10)];
        break;
    }
  }

  return password;
};

console.log(generatePassword());
