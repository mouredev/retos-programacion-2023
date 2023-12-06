const aurebesh = {
  a: "aurek",
  ae: "enth",
  b: "besh",
  c: "cresh",
  ch: "cherek",
  d: "dorn",
  e: "esk",
  eo: "onith",
  f: "forn",
  g: "grek",
  h: "herf",
  i: "isk",
  j: "jenth",
  k: "krill",
  kh: "krenth",
  l: "leth",
  m: "mern",
  n: "nern",
  ng: "nen",
  o: "osk",
  oo: "orenth",
  p: "peth",
  q: "qek",
  r: "resh",
  s: "senth",
  sh: "shen",
  t: "trill",
  th: "thesh",
  u: "usk",
  v: "vev",
  w: "wesk",
  x: "xesh",
  y: "yirt",
  z: "zerek",
  ",": ",",
  ".": ".",
  "?": "?",
  "!": "!",
  ":": ":",
  ";": ";",
  "-": "-",
  '"': '"',
  "'": "'",
  "(": "(",
  ")": ")",
  "/": "/",
  $: "$",
};

const toAurebesh = (word) => {
  let output = "";
  let idx = 0;
  while (idx < word.length) {
    let char = aurebesh[word[idx]];
    if (char == undefined) {
      char = word[idx];
    }
    if (idx + 1 < word.length) {
      let newWord = word[idx] + word[idx + 1];
      if (aurebesh[newWord] != undefined) {
        char = aurebesh[newWord];
        idx += 1;
      }
    }

    output += char;
    idx += 1;
  }
  return output;
};

const fromAurebesh = (word) => {
  let output = "";
  let idx = 0;
  while (idx < word.length) {
    let char = word[idx];
    let options = gatherFromAurebeshOptions(char);

    for (let key in options) {
      if (word.slice(idx, idx + options[key].length) != options[key]) {
        continue;
      }

      char = key;
      idx += options[key].length;
    }
    output += char;
    if (options.length == 0 || char == word[idx]) idx += 1;
  }
  return output;
};

const gatherFromAurebeshOptions = (char) => {
  let output = {};
  for (let key in aurebesh) {
    if (aurebesh[key].match(new RegExp(`^${char}`, "g"))) {
      output[key] = aurebesh[key];
    }
  }
  return output;
};

// console.log(`toAurebesh: ${toAurebesh("áb, é, ñ")}`);
// console.log(`toAurebesh: ${toAurebesh("biux")}`);
// console.log(`toAurebesh: ${toAurebesh("bars")}`);
// console.log(`toAurebesh: ${toAurebesh("barsh")}`);

// console.log(`fromAurebesh: ${fromAurebesh("ábesh, é, ñ")}`);
// console.log(`fromAurebesh: ${fromAurebesh("beshiskuskxesh")}`);
// console.log(`fromAurebesh: ${fromAurebesh("beshaurekreshsenth")}`);
// console.log(`fromAurebesh: ${fromAurebesh("beshaurekreshshen")}`);
