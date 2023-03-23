interface Char {
  A: string;
  B: string;
  C: string;
  D: string;
  E: string;
  F: string;
  G: string;
  H: string;
  I: string;
  J: string;
  K: string;
  L: string;
  M: string;
  N: string;
  O: string;
  P: string;
  Q: string;
  R: string;
  S: string;
  T: string;
  U: string;
  V: string;
  W: string;
  X: string;
  Y: string;
  Z: string;
  1: string;
  2: string;
  3: string;
  4: string;
  5: string;
  6: string;
  7: string;
  8: string;
  9: string;
  0: string;
  " ": string;
  "?": string;
  "!": string;
}
const LEETALPHABET: Char = {
  A: "4",
  B: "l3",
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
  M: "/'/'",
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
  Y: "j",
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
  " ": " ",
  "?": "?",
  "!": "!",
};

function TransformText(LEETALPHABET: Char, message: string): void {
  let messageTranformed: string = "";
  for (let i: number = 0; i < message.toUpperCase().length; i++) {
    messageTranformed += LEETALPHABET[message[i]];
  }
  console.log(messageTranformed);
}

TransformText(LEETALPHABET, "HOPE THIS IS RIGHT");

export {};
