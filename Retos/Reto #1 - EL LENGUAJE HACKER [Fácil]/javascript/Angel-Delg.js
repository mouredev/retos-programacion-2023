const TranslateStringToHackerLanguage = text => {

   const StringTraslated = []
   const decorators = {
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
      l: "£",
      m: "JVI",
      n: "^/",
      o: "0",
      p: "|*",
      q: "(_,)",
      r: "I2",
      s: "5",
      t: "7",
      u: "(_)",
      v: "|/",
      w: "VV",
      x: "><",
      y: "j",
      z: "2",
      1: "L",
      2: "R",
      3: "E",
      4: "A",
      5: "S",
      6: "b",
      7: "T",
      8: "B",
      9: "q",
      0: "()"
   }

   for(let i = 0; i < text.length; i++){
      StringTraslated.push(decorators[text.toLowerCase()[i]])
   }

   return StringTraslated.join('')
}
console.log(TranslateStringToHackerLanguage("AngelDelgado"));