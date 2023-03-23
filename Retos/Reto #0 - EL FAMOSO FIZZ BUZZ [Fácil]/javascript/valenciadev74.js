for (let i = 1; i < 101; i++) {
	if (i % 3 == 0 && i % 5 == 0){
		console.log("\t fizzbuzz")
	} else if (i % 3 == 0){
		console.log("\t fizz")
	} else if (i % 5 == 0){
		console.log("\t buzz")
	} else {
		console.log("\t", i)
	}
}