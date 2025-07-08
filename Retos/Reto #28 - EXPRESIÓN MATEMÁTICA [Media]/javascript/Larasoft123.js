function IsMathExpression(expression) {
  const components = expression.split(" ");
  const suppoted_operators = ["+", "-", "*", "/", "%"];

  const regex = "[a-zA-Z]+"

  if (expression.match(regex) != null) {
    return false;
  }

  

  if (components.length < 3 || components.length % 2 == 0) {
    return false;
  }

  for (let i = 0; i < components.length; i++) {
   if (i % 2 !== 0 && !suppoted_operators.includes(components[i])) {
     return false;
   }

  }


  return true;
}

console.log((IsMathExpression("3 + 5")))
console.log((IsMathExpression("3 a 5")))
console.log((IsMathExpression("-3 + 5")))
console.log((IsMathExpression("- 3 + 5")))
console.log((IsMathExpression("-3 a 5")))
console.log((IsMathExpression("-3+5")))
console.log((IsMathExpression("3 + 5 - 1 / 4 % 8")))
