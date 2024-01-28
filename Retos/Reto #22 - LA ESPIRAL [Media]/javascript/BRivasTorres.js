const simbols = ["═", "║",  "╗", "╔", "╝", "╚"];

const createEspiral = (size) => {
	let espiral = "═".repeat(size - 1) + "╗";
	for (let row = 1; row < size; row++) {
        const currHalf = size / 2
        const spaces = size - row - 1 
        
		espiral +=
			row < currHalf
				? `\n${"║".repeat(row - 1)}╔${"═".repeat(
						size - (row * 2 + 1)
				  )}╗${"║".repeat(row)}`
				: `\n${"║".repeat(spaces)}╚${"═".repeat(
						row * 2 - size
				  )}╝${"║".repeat(spaces)}`;
	}
    return espiral
};

console.log(createEspiral(5))
console.log(createEspiral(15))
console.log(createEspiral(25))
console.log(createEspiral(50))
console.log(createEspiral(100))
console.log(createEspiral(40))
