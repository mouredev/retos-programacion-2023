const countBackwards = (count, seconds) => {
    if(count % 1 !== 0 || seconds % 1 !== 0) return "Solo se permiten numero enteros"
    if(count < 0 || seconds < 0) return "Solo se permiten numeros positivos"
    
    
    const intervalId = setInterval(() => {
		console.log(count);
		count -= 1;
		if (count < 0) {
			clearInterval(intervalId);
		}
	}, seconds);
}

console.log(countBackwards(5, 1000));
console.log(countBackwards(500, 3000));
console.log(countBackwards(10, 8000));
console.log(countBackwards(25, 4000));