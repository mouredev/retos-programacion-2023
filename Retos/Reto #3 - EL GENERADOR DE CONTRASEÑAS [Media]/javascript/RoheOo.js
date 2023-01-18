const getRandom = (max) => {
  return Math.floor(Math.random() * max);
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
    if (!addUppercase && !addSymbols && !addNumbers) {
      option = 0;
    } else if (addUppercase && !addSymbols && !addNumbers) {
      while (option === 3 || option === 2) {
        option = getRandom(3);
      }
    } else if (addUppercase && addSymbols && !addNumbers) {
      while (option === 3) {
        option = getRandom(3);
      }
    } else if (addUppercase && addSymbols && addNumbers) {
      option = getRandom(3);
    } else if (!addUppercase && addSymbols && !addNumbers) {
      while (option === 1 || option === 3) {
        option = getRandom(3);
      }
    } else if (!addUppercase && addSymbols && addNumbers) {
      while (option === 1) {
        option = getRandom(3);
      }
    } else if (!addUppercase && !addSymbols && addNumbers) {
      while (option === 1 || option === 2) {
        option = getRandom(3);
      }
    } else if (addUppercase && !addSymbols && addNumbers) {
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
