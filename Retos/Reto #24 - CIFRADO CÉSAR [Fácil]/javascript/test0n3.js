function CaesarCipher(str = "", action = "") {
  const alphabet = {
    a: 0,
    b: 1,
    c: 2,
    d: 3,
    e: 4,
    f: 5,
    g: 6,
    h: 7,
    i: 8,
    j: 9,
    k: 10,
    l: 11,
    m: 12,
    n: 13,
    ñ: 14,
    o: 15,
    p: 16,
    q: 17,
    r: 18,
    s: 19,
    t: 20,
    u: 21,
    v: 22,
    w: 23,
    x: 24,
    y: 25,
    z: 26,
  };

  const swiftDirections = { positive: 1, negative: -1 };

  let text = str.split("");
  const swiftDirection = swiftDirections["positive"];
  const swiftNumber = 3;
  const alphabetLength = Object.keys(alphabet).length;

  function act() {
    if (str.length == 0 || action.length == 0) {
      return "input missing";
    }
    return process_text();
  }

  function process_text() {
    let result = [];
    text.forEach((letter) => {
      let pos = alphabet[letter.toLowerCase()];
      if (pos == undefined) {
        result.push(letter);
      } else {
        let newLetter = Object.keys(alphabet)[newPosition(pos)];
        if (isUpcase(letter)) {
          result.push(newLetter.toUpperCase());
        } else {
          result.push(newLetter);
        }
      }
    });
    return result.join("");
  }

  function isUpcase(letter) {
    return letter == letter.toUpperCase();
  }

  function newPosition(position) {
    let offset = swiftDirection * swiftNumber;
    if (action == "decipher") {
      offset = -offset;
    }
    let newPosition = (position + offset) % alphabetLength;
    if (newPosition < 0) {
      newPosition = alphabetLength + newPosition;
    }
    return newPosition;
  }

  Object.defineProperty(this, "act", {
    get: function () {
      return act();
    },
  });
}

const testsCollections = {
  tests: [
    { str: "The quick brown fox jumps over the lazy dog.", action: "cipher" },
    { str: "Wkh txlfn eurzp ira mxosv ryhu wkh ñdcb grj.", action: "decipher" },
    { str: "Aquí va más texto.", action: "cipher" },
    { str: "Dtxí yd oáv whawr.", action: "decipher" },
    { str: "", action: "" },
  ],
  expecteds: [
    "Wkh txlfn eurzp ira mxosv ryhu wkh ñdcb grj.",
    "The quick brown fox jumps over the lazy dog.",
    "Dtxí yd oáv whawr.",
    "Aquí va más texto.",
    "input missing",
  ],
};

testsCollections.tests.forEach((test, index) => {
  const result = new CaesarCipher(test.str, test.action);
  console.log(result.act);
  console.log(result.act == testsCollections.expecteds[index]);
  console.log("----------------------------------------------------");
});
