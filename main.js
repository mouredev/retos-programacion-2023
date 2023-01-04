let dictionary = {
    "a" : "4",
    "b" : "I3",
    "c" : "[",
    "d" : ")",
    "e" : "3",
    "f" : "|=",
    "g" : "&",
    "h" : "#",
    "i" : "1",
    "j" : ",_|",
    "k" : ">|",
    "l" : "£",
    "m" : "[V]",
    "n" : "[\]",
    "o" : "0",
    "p" : "|*",
    "q" : "(_,)",
    "r" : "I2",
    "s" : "5",
    "t" : "7",
    "u" : "(_)",
    "v" : "|/",
    "w" : "'//",
    "x" : "><",
    "y" : "`/",
    "z" : "2",
    " " : " ",
    "1" : "L",
    "2" : "R",
    "3" : "E",
    "4" : "A",
    "5" : "S",
    "6" : "G",
    "7" : "T",
    "8" : "B",
    "9" : "g",
    "0" : "o",
    "," : ",",
    ";" : ";",
    "." : ".",
    "[" : "[",
    "]" : "]",
    "<" : "<",
    ">" : ">",
    "'" : "'",    

}
let texto = document.getElementById('text')
let res = document.getElementById('res')
function consola(){
    let temp = []
    for (let i = 0; i < texto.value.length; i++) {
        temp.push(dictionary[texto.value[i].toLowerCase()])   
    }
    res.innerHTML = temp.join('')
    
}





