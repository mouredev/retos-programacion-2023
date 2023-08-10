const getColumnNumber = (col) => {
    return [...col].reduce((acc, val) => acc * 26 + val.charCodeAt(0) - 64, 0)
}

console.log(getColumnNumber('A'))   // 1
console.log(getColumnNumber('Z'))   // 26
console.log(getColumnNumber('AA'))  // 27
console.log(getColumnNumber('CA'))  // 79
console.log(getColumnNumber('AAK')) // 713