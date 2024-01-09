const createLadder = (n) => {
    if(n === 0) return  "__"
    
    let steps = "_|"
    let res = ""
    let spaces = ""
    
    if(n > 0) {
        let i = 0
        let temp = ""
        while(n !== 0) {
            temp += steps[i]
            i === 1 ? temp += "\n" + spaces : null
            i === 1 ? (i = 0) : i++;
            spaces += " ";
            n--
        }
        res = temp.split(" ").reverse().join(" ")
    } else {
        spaces += "  "
        let temp = ""
        let i = 0;
		while (n !== 0) {            
			temp += steps[i];
			i === 0 ? (temp += "\n" + spaces) : null;
			i === 1 ? (i = 0) : i++;
			spaces += " ";
			n++;
		}
        res = temp
    }
    return res
}

console.log(createLadder(-3))
console.log(createLadder(-7))
console.log(createLadder(10))
console.log(createLadder(18))