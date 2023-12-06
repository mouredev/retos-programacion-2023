function AreTheyTheSameText(textOne, textTwo) {
  let arrayTextOne = textOne.split("");
  let arrayTextTwo = textTwo.split("");
  let arrayResult = [];

  if (arrayTextOne.length !== arrayTextTwo.length)
    return "they are texts with different lengths";

  for (let i = 0; i < arrayTextOne.length; i++) {
    if (arrayTextOne[i] !== arrayTextTwo[i]) {
      arrayResult.push(arrayTextTwo[i]);
    }
  }

  if (arrayResult.length == 0) return "the texts are the same";

  return arrayResult;
}

console.log(AreTheyTheSameText("Me llamo mouredev", "Me llemo mouredov"));
console.log(AreTheyTheSameText("Me llamo.Brais Moure", "Me llamo brais moure"));
console.log(AreTheyTheSameText("Me llamo George y está es mi historia", "Me llamo George y está es mi historia"));
