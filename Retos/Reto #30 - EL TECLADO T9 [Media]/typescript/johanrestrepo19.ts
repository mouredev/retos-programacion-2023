const KEYBOARD = {
  1: [",", ".", "?", "!"],
  2: ["A", "B", "C"],
  3: ["D", "E", "F"],
  4: ["G", "H", "I"],
  5: ["J", "K", "L"],
  6: ["M", "N", "O"],
  7: ["P", "Q", "R", "S"],
  8: ["T", "U", "V"],
  9: ["W", "X", "Y", "Z"],
  0: [" "],
};

const isHomogeneousString = (input: string): boolean => {
  const firstChar = input.charAt(0);
  for (let index = 0; index < input.length; index++)
    if (input.charAt(index) !== firstChar) return false;
  return true;
};

const transformT9ToString = (input: string, separator = "-"): string => {
  const sections = input.split(separator);
  const result: string[] = [];
  for (let index = 0; index < sections.length; index++) {
    const section = sections[index];
    if (!isHomogeneousString(section)) return "";
    const char = Number(section.charAt(0)) as keyof typeof KEYBOARD;
    const letter = (section.length - 1) % KEYBOARD[char].length;
    result.push(KEYBOARD[char][letter]);
  }
  return result.join("");
};

console.log(transformT9ToString("6-666-88-777-33-3-33-888-1111"));
console.log(
  transformT9ToString("5 666 44 2 66 0 777 33 7777 8 777 33 7 666 1111", " ")
);
console.log(
  transformT9ToString("5 666 44 2 66 0 777 33 7777 8 777 33 7 666 1111")
);
