const countText = (s) => {
    if(typeof s !== "string") return "Enter text"
    
    const regEx = /\.|\.\./g;
    const sArr = s.split(" ")

    let totalWords = sArr.length
    let averageLength = Math.floor(s.length / totalWords);
    let points = s.match(regEx)
    let sentences = points ? points.length : 0
    let longestWord = ""    
    
    for(let i = 0; i < sArr.length; i++) {
        let currWord = sArr[i]
        if(currWord.length > longestWord.length) {
            longestWord = currWord
        }
    }
    
    return `-Total words = ${totalWords}\n -Average length of words = ${averageLength} \n -Number of sentences = ${sentences} \n -Longest Word = ${longestWord} `;
}

console.log(countText("texto de prueba para ejercicio. hola. como."))
console.log(countText("text to. practice logical programming."))
console.log(countText("hello hello"))
console.log(countText("texto de prueba para ejercicio. hola. como."))