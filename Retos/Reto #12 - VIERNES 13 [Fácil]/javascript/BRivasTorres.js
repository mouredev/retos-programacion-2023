const isFriday13 = (month, year) => {
    let date = new Date(year, month - 1, 13)
    
    return date.getDay() === 5
}

console.log(isFriday13(1, 1930))
console.log(isFriday13(11, 1932))
console.log(isFriday13(10, 2023))
console.log(isFriday13(9, 1839))
console.log(isFriday13(15, 1945))