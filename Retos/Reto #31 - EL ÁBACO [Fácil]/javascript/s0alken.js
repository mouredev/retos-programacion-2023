const decodeAbacus = (array) => {
    return Number(array.reduce((acc, val) => acc += val.split('---')[0].length, ''))
}

const array = [
    "O---OOOOOOOO",
    "OOO---OOOOOO",
    "---OOOOOOOOO",
    "OO---OOOOOOO",
    "OOOOOOO---OO",
    "OOOOOOOOO---",
    "---OOOOOOOOO"
]

console.log(decodeAbacus(array))