const parameters = ["uppercase", "numbers", "symbols"];

const parametersCount = Math.trunc(Math.random() * 3) + 1;

const letters = {
    1: "a",
    2: "b",
    3: "c",
    4: "d",
    5: "e",
    6: "f",
    7: "g",
    8: "h",
    9: "i",
    10: "j",
    11: "k",
    12: "l",
    13: "m",
    14: "n",
    15: "o",
    16: "p",
    17: "q",
    18: "r",
    19: "s",
    20: "t",
    21: "u",
    22: "v",
    23: "w",
    24: "x",
    25: "y",
    26: "z",
};

const symbols = {
    1: ".",
    2: ",",
    3: ";",
    4: ":",
    5: "-",
    6: "_",
    7: "[",
    8: "]",
    9: "{",
    10: "}",
    11: "*",
    12: "?",
    13: "¿",
    14: "¡",
    15: "!",
    16: "$",
    17: "/",
    18: "(",
    19: ")",
    20: "=",
    21: "&",
    22: "#",
};

const genPassword = (parametersCount) => {
    let hasUppercase = false;
    let hasNumbers = false;
    let hasSymbols = false;

    for (let i = 0; i < parametersCount; i++) {
        const parameter = parameters[Math.trunc(Math.random() * 3)];
        if (parameter == "uppercase") {
            hasUppercase = true;
        } else if (parameter == "numbers") {
            hasNumbers = true;
        } else {
            hasSymbols = true;
        }
    }
    const passLength = Math.trunc(Math.random() * 9) + 8;
    let password = "";
    for (let i = 0; i < passLength; i++) {
        const parameterSelected = Math.trunc(Math.random() * 3) + 1;
        if (parameterSelected == 1) {
            const letter =
                letters[
                    Math.trunc(Math.random() * Object.entries(letters).length) +
                        1
                ];
            if (hasUppercase) {
                password = password.concat(
                    Math.trunc(Math.random() * 2) == 0
                        ? letter
                        : letter.toUpperCase()
                );
            } else {
                password = password.concat(letter);
            }
        } else if (parameterSelected == 2 && hasNumbers) {
            password = password.concat(Math.trunc(Math.random() * 10));
        } else if (hasSymbols) {
            const symbol =
                symbols[
                    Math.trunc(Math.random() * Object.entries(symbols).length) +
                        1
                ];
            password = password.concat(symbol);
        } else {
            const letter =
                letters[
                    Math.trunc(Math.random() * Object.entries(letters).length) +
                        1
                ];
            if (hasUppercase) {
                password = password.concat(
                    Math.trunc(Math.random() * 2) == 0
                        ? letter
                        : letter.toUpperCase()
                );
            } else {
                password = password.concat(letter);
            }
        }
    }
    return password
};

console.log(genPassword(parametersCount));
