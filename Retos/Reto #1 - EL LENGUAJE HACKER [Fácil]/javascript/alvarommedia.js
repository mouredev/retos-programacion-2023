const leetCode = {
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

function lenguajeHacker(text) {
	let textHacker = "";
	for (char of text) {
		textHacker += convertidorAHacker(char);
	}
	console.log(textHacker);
}

const convertidorAHacker = (value) => {
	value = value.toLowerCase();
	return leetCode[value] || value; 
};

lenguajeHacker("patatas con mejillones");
