const leetTable: Record<string, string> = {
  A: "4",
  B: "I3",
  C: "[",
  D: ")",
  E: "3",
  F: "|=",
  G: "&",
  H: "#",
  I: "1",
  J: ",_|",
  K: ">|",
  L: "1",
  M: "//\\",
  N: "^/",
  O: "0",
  P: "|*",
  Q: "(_,)",
  R: "I2",
  S: "5",
  T: "7",
  U: "(_)",
  V: "/",
  W: "//",
  X: "><",
  Y: "`/",
  Z: "2",
  1: "L",
  2: "R",
  3: "E",
  4: "A",
  5: "S",
  6: "b",
  7: "T",
  8: "B",
  9: "g",
  0: "o",
}

/**
 * Translates a given text by replacing characters according to a provided leet table.
 *
 * @param {string} text - The text to be translated.
 * @param {Record<string, string>} leetTable - The leet table containing character mappings.
 * @return {string} The translated text.
 */
const translateLeet = (text: string = "", leetTable: Record<string, string>): string =>
  text
    .split("")
    .map((char) => leetTable[char.toUpperCase()] || char)
    .join("")

console.log(translateLeet("Hello World", leetTable))
