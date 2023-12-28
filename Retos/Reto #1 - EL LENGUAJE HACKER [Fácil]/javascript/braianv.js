function leet(text) {
  let hackerLanguage = [
    "4",
    "I3",
    "[",
    ")",
    "3",
    "|=",
    "&",
    "#",
    "1",
    ",_|",
    ">|",
    "1",
    "/\\/\\",
    "^/",
    "0",
    "|*",
    "(_,)",
    "l2",
    "5",
    "7",
    "|_|",
    "\\/",
    "\\/\\/",
    "><",
    "`/",
    "2",
  ];

  let newText = text.toLowerCase().split("");
  let replaceText = newText.map((l) => {
    return l
      .replace(/a/g, hackerLanguage[0])
      .replace(/b/g, hackerLanguage[1])
      .replace(/c/g, hackerLanguage[2])
      .replace(/d/g, hackerLanguage[3])
      .replace(/e/g, hackerLanguage[4])
      .replace(/f/g, hackerLanguage[5])
      .replace(/g/g, hackerLanguage[6])
      .replace(/h/g, hackerLanguage[7])
      .replace(/i/g, hackerLanguage[8])
      .replace(/j/g, hackerLanguage[9])
      .replace(/k/g, hackerLanguage[10])
      .replace(/l/g, hackerLanguage[11])
      .replace(/m/g, hackerLanguage[12])
      .replace(/n/g, hackerLanguage[13])
      .replace(/o/g, hackerLanguage[14])
      .replace(/p/g, hackerLanguage[15])
      .replace(/q/g, hackerLanguage[16])
      .replace(/r/g, hackerLanguage[17])
      .replace(/s/g, hackerLanguage[18])
      .replace(/t/g, hackerLanguage[19])
      .replace(/u/g, hackerLanguage[20])
      .replace(/v/g, hackerLanguage[21])
      .replace(/w/g, hackerLanguage[22])
      .replace(/x/g, hackerLanguage[23])
      .replace(/y/g, hackerLanguage[24])
      .replace(/z/g, hackerLanguage[25]);
  });
  return replaceText;
}
