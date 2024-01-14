const convertHexa = (n) => {
	let res = "";
	const hexaNums = [
		"0",
		"1",
		"2",
		"3",
		"4",
		"5",
		"6",
		"7",
		"8",
		"9",
		"A",
		"B",
		"C",
		"D",
		"E",
		"F",
	];

	while (n > 0) {
		let rem = n % 16;
		n = Math.floor(n / 16);
		res = hexaNums[rem] + res;
	}

	return res;
};

console.log(convertHexa(1820));
console.log(convertHexa(1970));
console.log(convertHexa(1976));
console.log(convertHexa(850));

const convertOctal = (n) => {
    let res = ""    
    while(n > 0) {
        let rem = n % 8
        n = Math.floor(n/8)
          res = `${rem}${res}`;
    }
    return res
}

console.log(convertOctal(8650))
console.log(convertOctal(1800))
