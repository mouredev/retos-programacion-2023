function mathExpression(operation) {
  if (typeof operation !== "string")
    `type of: the operation ${operation} is false`;

  let lengthOperation = operation.trim().split(/\s+/);
  if (lengthOperation.length < 3) return `length: the operation ${operation} is false`;

  let regex =
    /^-?(\d+\.?\d*|\.\d+)\s[+\-*/%]\s-?(\d+\.?\d*|\.\d+)(\s[+\-*/%]\s-?(\d+\.?\d*|\.\d+))*$/;
  let isOperationInfoValid = regex.test(operation);
  if (!isOperationInfoValid)
    return `operanding: the operation ${operation} is false`;

  if (eval(operation) == 0 || eval(operation))
    return `the operation ${operation} is true`;
  return `result: the operation ${operation} is false`;
}

console.log(mathExpression("-2 + -2 + -2 / -3 * -3 - 3 + -8"));
