const charType = { 0: "ascii", 1: "numbers", 2: "symbols" };
const alphabet = "abcdefghijklmnopqrstuvwxyz";
const numbers = "0123456789";
const symbols = "-!().?[]_`~@#$^&*+=";

const passwordGenerator = (
  passLength,
  allowUpcase,
  allowNumbers,
  allowSymbols
) => {
  if (passLength < 8) passLength = 8;
  if (passLength > 16) passLength = 16;

  let errors = 1;
  let passString = "";
  while (errors != 0) {
    passString = "";
    while (passString.length < passLength) {
      passString += genCharacter(allowUpcase, allowNumbers, allowSymbols);
    }
    errors = checkPassword(passString, allowUpcase, allowNumbers, allowSymbols);
  }
  return passString;
};

const genCharacter = (allowUpcase, allowNumber, allowSymbols) => {
  let dataBank = alphabet;
  if (allowUpcase) dataBank += alphabet.toUpperCase();
  if (allowNumber) dataBank += numbers;
  if (allowSymbols) dataBank += symbols;
  return dataBank[Math.floor(Math.random() * dataBank.length)];
};
const checkPassword = (
  passwordCandidate,
  allowUpcase,
  allowNumber,
  allowSymbols
) => {
  let errors = 0;
  if (["-", "."].includes(passwordCandidate[0])) errors += 1;
  if (allowUpcase && !passwordCandidate.match(/[A-Z]/g)) errors += 1;
  if (allowNumber && !passwordCandidate.match(/[0-9]/g)) errors += 1;
  if (allowSymbols && !passwordCandidate.match(/[-!().?\[\]_`~@#$^&*+=]/g))
    errors += 1;
  return errors;
};

// caracteres tolerados para password:
// Lowercase characters {a-z}
// Uppercase characters {A-Z}
// Numbers {0-9}
// Exclamation point {!}
// Open parenthesis {(}
// Close parenthesis {)}
// Dash {-}; this character is not supported as the first character in the user ID or password
// Period {.}; this character is not supported as the first character in the user ID or password
// Question mark {?}
// Open bracket {[}
// Close bracket {]}
// Underscore {_};

// this is the only supported special character in IBM i:
// Grave accent {`}
// Tilde {~}
// Commercial at {@}
// Number sign {#}
// Dollar sign {$}
// Circumflex accent {^}
// Ampersand {&}
// Asterisk
// {*}
// Plus sign {+}
// Equals sign {=}

const tests = [
  [8, true, false, false],
  [10, true, true, false],
  [10, true, true, true],
  [10, false, true, true],
  [10, false, false, true],
  [7, false, false, false],
  [18, false, false, false],
];

errors = 0;
tests.forEach((test) => {
  resp = passwordGenerator(...test);

  if (test[0] < 8 && resp.length != 8) errors += 1;
  else if (test[0] > 16 && resp.length != 16) errors += 1;

  if (["-", "."].includes(resp[0])) errors += 1;
  if (test[1] && !resp.match(/[A-Z]/g)) errors += 1;
  if (test[2] && !resp.match(/[0-9]/g)) errors += 1;
  if (test[3] && !resp.match(/[-!().?\[\]_`~@#$^&*+=]/)) errors += 1;

  console.log("\n\noriginal: ", test);
  console.log("\n", resp);
  console.log(`\nerrors: ${errors}`);
});

console.log(
  `\n\nTests${errors != 0 ? " not " : " "}passed, ${errors} errors\n`
);
