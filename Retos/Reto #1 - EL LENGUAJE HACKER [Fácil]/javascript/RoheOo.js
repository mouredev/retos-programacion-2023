const leet = {
  a: "4", b: "I3", c: "[", d: ")", e: "3", f: "|=", g: "&", h: "#", i: "1",
  j: ",_|", k: ">|", l: "1", m: "[V]", n: "^/", o: "0", p: "|*", q: "(_,)",
  r: "I2", s: "5", t: "7", u: "(_)", v: "|/", w: "v²", x: "><", y: "j", z: "2",
  1: "L", 2: "R", 3: "E", 4: "A", 5: "S", 6: "b", 7: "T", 8: "B", 9: "g", 0: "o",
};

const transformText = (normalText) => {
  let newLeetText = "";
  for (let i = 0; i < normalText.length; i++) {
    if (normalText.charAt(i) === " ") {
      newLeetText += " ";
    } else {
      newLeetText += leet[`${normalText.charAt(i).toLowerCase()}`];
    }
  }
  console.log(newLeetText);
};

transformText("hi my birthday is October 21");
