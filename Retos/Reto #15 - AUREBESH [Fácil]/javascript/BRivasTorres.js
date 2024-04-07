const aurebeshAlphabet = {
	a: "aurek",
	b: "besh",
	c: "cresh",
	d: "dorn",
	e: "esk",
	f: "forn",
	g: "grek",
	h: "herf",
	i: "isk",
	j: "jenth",
	k: "krill",
	l: "leth",
	m: "merm",
	n: "nern",
	o: "osk",
	p: "peth",
	q: "qek",
	r: "resh",
	s: "senth",
	t: "trill",
	u: "usk",
	v: "vev",
	w: "wesk",
	x: "xesh",
	y: "yirt",
	z: "zerek",
	ae: "enth",
	eo: "onith",
	kh: "krenth",
	ng: "nen",
	oo: "orenth",
	sh: "sen",
	th: "thesh",
};

const convertLanguaje = (languaje, s) => {
    let res = ""
    
    if(languaje.toLowerCase() === "aurebesh") {
        for(let i = 0; i < s.length; i++) {
            isLetter = s[i] in aurebeshAlphabet
            let val = aurebeshAlphabet[s[i]]
            isLetter ? res += val : res += s[i] 
            res += val + " "
        }
    } else {
        let arr = s.split(" ")
        for(let i = 0; i < arr.length; i++) {
            for(const key in aurebeshAlphabet) {
                if(aurebeshAlphabet[key] === arr[i]) {
                    res += key
                }
            }
        }
    }
    return res.trim()
};


console.log(convertLanguaje("aurebesh", "hola"));
console.log(convertLanguaje("aurebesh", "buenos dias"));
console.log(convertLanguaje("español", "herf osk leth aurek"));