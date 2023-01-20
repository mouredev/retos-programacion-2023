const leetAlphabet = {
  a: "4",
  b: "I3",
  c: "[",
  d: ")",
  e: "3",
  f: "|=",
  g: "&",
  h: "#",
  i: "1",
  j: ",_|",
  k: ">|",
  l: "1",
  m: "/\\/\\",
  n: "^/",
  o: "0",
  p: "|*",
  q: "(_,)",
  r: "I2",
  s: "5",
  t: "7",
  u: "(_)",
  v: "\\/",
  w: "\\/\\/",
  x: "><",
  y: "j",
  z: "2",
};

const leetify = (input) => {
  let result = "";
  for (let character of input) {
    const convertion = leetAlphabet[character] || character;
    result = result + convertion;
  }
  console.log(result)
};

leetify("leet");
