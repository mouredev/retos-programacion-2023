const getNumber = (): number => {
  const value = prompt("Ingrese un número");

  return Number(value);
};

const generateMultiplicationTable = (): void => {
  const value: number = getNumber();

  for (let i = 1; i <= 10; i++) {
    console.log(`${value} x ${i} = ${value * i}`);
  }
};

generateMultiplicationTable();
