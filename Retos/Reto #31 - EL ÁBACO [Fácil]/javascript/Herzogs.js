const array = [
    "O---OOOOOOOO",
    "OOO---OOOOOO",
    "---OOOOOOOOO",
    "OO---OOOOOOO",
    "OOOOOOO---OO",
    "OOOOOOOOO---",
    "---OOOOOOOOO"
]

let res=""

array.forEach( (el,index) =>{
    res += el.indexOf('-')
    if(index%3 == 0 && index+1 < array.length)
     res+='.'
})
console.log("ABACO");
console.log(array);
console.log("Resultado:",res)