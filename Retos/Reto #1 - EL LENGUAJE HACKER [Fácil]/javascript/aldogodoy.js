function alphabet (letter) {
    const alfabeto = {
        a: "4",
        b: "I3",
        c: "©",
        d: "|)",
        e: "€",
        f: "ƒ",
        g: "9",
        h: "#",
        i: "1",
        j: "]",
        k: "1<",
        l: "£",
        m: "IVI",
        n: "И",
        o: "ø",
        p: "|*",
        q: "ℚ",
        r: "Я",
        s: "$",
        t: "7",
        u: "µ",
        v: "▼",
        w: "ω",
        x: "×",
        y: "¥",
        z: "2",
        ' ': ' '
    };
    return letter in alfabeto ? alfabeto[letter] : ' ';
}
  function leet(word) {
    const words = [...(word).trim().toLowerCase()]
    let auxWords = [];
    for(let i = 0; i < words.length; i++ ){
        auxWords.push(alphabet(words[i]))
    }
    return auxWords.join(' ')
  }
  leet('El lenguaje hacker');
