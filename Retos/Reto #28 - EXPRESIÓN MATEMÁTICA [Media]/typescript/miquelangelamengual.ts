const checkMathExpression = (expression: string): boolean => {
  try {
    eval(expression);
    return true;
  } catch (error) {
    return false;
  }
};

console.log(checkMathExpression("5 + 6 / 7 - 4"));
console.log(checkMathExpression("5 a 6"));
