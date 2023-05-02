const stairsGenerator = (input) => {
  let stairs = "";

  if (input <= 0) stairs = downwardStairs(Math.abs(input));

  if (input > 0) stairs = upwardStairs(input);

  return stairs.join("\n");
};

const downwardStairs = (input) => {
  let stairs = ["_"];
  if (input == 0) stairs[0] += "_";

  let stair = 1;
  while (stair <= input) {
    stairs.push(`${" ".repeat(2 * stair - 1)}|_`);
    stair += 1;
  }
  return stairs;
};

const upwardStairs = (input) => {
  let maxSpaceLength = 1 + 2 * input;
  let stairs = [`${" ".repeat(maxSpaceLength - 1)}_`];
  let stair = 1;
  while (stair <= input) {
    stairs.push(`${" ".repeat(maxSpaceLength - (2 * stair + 1))}_|`);
    stair += 1;
  }
  return stairs;
};

// console.log(stairsGenerator(0));
// console.log(stairsGenerator(-5));
// console.log(stairsGenerator(5));
