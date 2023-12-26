function leetify(text) {
  let dictionary = {
    a: "4",
    b: "8",
    c: "©",
    d: "[)",
    e: "3",
    f: "ƒ",
    g: "6",
    h: ")-(",
    i: "1",
    j: "_|",
    k: "|<",
    l: "|_",
    m: "IVI",
    n: "||",
    o: "Ø",
    p: "|o",
    q: "9",
    r: "Я",
    s: "§",
    t: "7",
    u: "µ",
    v: "/",
    w: "//",
    x: "Ж",
    y: "Ч",
    z: "2",
  };

  let textLeet = "";

  for (let i = 0; i < text.length; i++) {
    if (dictionary.hasOwnProperty(text[i])) {
      textLeet += dictionary[text[i]];
    } else {
      textLeet += text[i];
    }
  }
  console.log(textLeet);
}

leetify("a veces me siento solo, y me lanzo a la calleeee (8)");
