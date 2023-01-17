function textToHackerText(textInput) {
  const dictionaryHacker = {
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
    m: "/\\",
    n: "^/",
    o: "0",
    p: "|*",
    q: "(_,)",
    r: "I2",
    s: "5",
    t: "7",
    u: "(_)",
    v: "/",
    w: "//",
    x: "><",
    y: "j",
    z: "2",
  };
  let textHacker = "";

  for (const iterator of textInput) {
    textHacker +=
      iterator in dictionaryHacker ? dictionaryHacker[iterator] : iterator;
  }

  console.log(textHacker);
}

textToHackerText("Hello World");
