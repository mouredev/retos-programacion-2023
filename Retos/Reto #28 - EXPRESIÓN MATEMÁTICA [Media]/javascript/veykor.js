function verifyMathExpresion(s) {
	//Check if input is empty or there is any match with the mathematical expression structure and verify if the length between the input and the match is equal
	var a;
	return !( !s || !(a = s.match(/(((-?\d+(\.\d+)? ?)([+/*%-] ))+)(-?\d+(\.\d+)?)/)) || a[0].length != s.length );
}
