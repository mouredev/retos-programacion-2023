function validateNumberBlock(numberBlock) {
  if (numberBlock.length == 0) return false;

  let regex = /^[0-9-]+$/;
  let theNumberBlockHasOnlyNumbersAndHyphens = regex.test(numberBlock);

  if (!theNumberBlockHasOnlyNumbersAndHyphens) return false;

  let arrayNumberBlock = [];
  let isNumberBlockValid = true;

  arrayNumberBlock = numberBlock.trim().split("-");

  arrayNumberBlock.forEach((element) => {
    let arrayElement = element.split("");
    if (arrayElement.length >= 2) {
      for (let i = 0; i < arrayElement.length; i++) {
        if (typeof arrayElement[i + 1] === "undefined") {
          if (arrayElement[i] != arrayElement[i - 1]) {
            isNumberBlockValid = false;
            break;
          }
        } else if (arrayElement[i] != arrayElement[i + 1]) {
          isNumberBlockValid = false;
          break;
        }
      }
    }
  });

  return { TrueOrFalse: isNumberBlockValid, ArrayTest: arrayNumberBlock };
}

function decodeMessage(numberBlock) {
  let responseValidateNumberBlock = validateNumberBlock(numberBlock);
  if (!responseValidateNumberBlock.TrueOrFalse)
    return "We're sorry, but your number block is invalid";

  let message = "";
  const decode = {
    2: "a",    22: "b",    222: "c",
    3: "d",    33: "e",    333: "f",
    4: "g",    44: "h",    444: "i",
    5: "j",    55: "k",    555: "l",
    6: "m",    66: "n",    666: "o",
    7: "p",    77: "q",    777: "r",    7777: "s",
    8: "t",    88: "u",    888: "v",
    9: "w",    99: "x",    999: "y",    9999: "z",
  };

  responseValidateNumberBlock.ArrayTest.forEach((element) => {
    if (typeof decode[element] === "undefined"){        
        message += " ";        
    } else {
        message += decode[element];
    }    
  });

  return message.toUpperCase();
}

console.log(decodeMessage("6-666-88-777-33-3-33-888"));
