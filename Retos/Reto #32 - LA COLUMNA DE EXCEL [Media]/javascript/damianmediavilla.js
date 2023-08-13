
 function numberColumn(columnName){
    var num=0
    columnName=columnName.split("").reverse().join("");
    for (i=0;i<columnName.length;i++){
        cn =parseInt(columnName[i],36)-9
        digit=((26**i)*cn)
        i==0?sum=cn : sum=digit;
        num += sum
        //console.log(`letra: ${columnName[i]} valorLetra ${cn} pos ${i} digit ${digit} sumaremos: ${sum}`)
    }
    return num
}

console.log(numberColumn("A"))
console.log(numberColumn("Z"))
console.log(numberColumn("AA"))
console.log(numberColumn("CA"))