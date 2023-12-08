const leetAlphabet = {
	a: "4",
	b: "13",
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
	m: "|/|",
	n: "^/",
	o: "0",
	p: "|*",
	q: "(_,)",
	r: "|2",
	s: "5",
	t: "7",
	u: "(_)",
	v: "/",
	w: "//",
	x: "><",
	y: "`j",
	z: "2",
	1: "L",
	2: "R",
	3: "E",
	4: "A",
	5: "S",
	6: "b",
	7: "T",
	8: "B",
	9: "g",
	0: "o",
};

const lenguajeHacker = (s) => {
	let r = "";
	for (let char of s.toLowerCase()) {
		let isChar = leetAlphabet[char];
		isChar ? (r += isChar) : (r += char);
	}
	return r;
};

console.log(lenguajeHacker("Reto mouredev #4"));
console.log(lenguajeHacker("Hola Mundo"));
