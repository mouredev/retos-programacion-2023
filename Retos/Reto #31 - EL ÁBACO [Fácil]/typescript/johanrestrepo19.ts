type Item = "O" | "-";
type Row =
  `${Item}${Item}${Item}${Item}${Item}${Item}${Item}${Item}${Item}${Item}${Item}${Item}`;
type Abacus = [Row, Row, Row, Row, Row, Row, Row];

const abacusToNumber = (abacusTable: Abacus): string => {
  const digits: number[] = [];
  abacusTable.forEach((row) => {
    const items = row.split("");
    let digit = 0;
    for (let index = 0; index < items.length; index++) {
      if (items[index] === "-") break;
      digit++;
    }
    digits.push(digit);
  });
  return digits.join("");
};

console.log(
  abacusToNumber([
    "O---OOOOOOOO",
    "OOO---OOOOOO",
    "---OOOOOOOOO",
    "OO---OOOOOOO",
    "OOOOOOO---OO",
    "OOOOOOOOO---",
    "---OOOOOOOOO",
  ])
);
console.log(
  abacusToNumber([
    "OOOOOOOOO---",
    "OOOOOOOOO---",
    "OOOOOOOOO---",
    "OOOOOOOOO---",
    "OOOOOOOOO---",
    "OOOOOOOOO---",
    "OOOOOOOOO---",
  ])
);

console.log(
  abacusToNumber([
    "O---OOOOOOOO",
    "OO---OOOOOOO",
    "OOO---OOOOOO",
    "OOOO---OOOOO",
    "OOOOO---OOOO",
    "OOOOOO---OOO",
    "OOOOOOO---OO",
  ])
);
