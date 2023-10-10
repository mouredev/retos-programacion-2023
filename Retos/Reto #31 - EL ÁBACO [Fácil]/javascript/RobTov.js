const abacus = (abacus) => {
  let outStr = "";
  abacus.forEach((r) => {
    let count = 0;
    for (let i = 0; i < 11; i++) {
      if (r[i] === "-") {
        outStr +=
          abacus.indexOf(r) == 0 || abacus.indexOf(r) == 3
            ? `${count}.`
            : count;
        break;
      } else {
        count += 1;
      }
    }
  });

  return outStr;
};

console.log(
  abacus([
    "O---OOOOOOOO",
    "OOO---OOOOOO",
    "---OOOOOOOOO",
    "OO---OOOOOOO",
    "OOOOOOO---OO",
    "OOOOOOOOO---",
    "---OOOOOOOOO",
  ])
);
