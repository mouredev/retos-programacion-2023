function numberColumn(columnName){
    var colNum=0
    columnName=columnName.split("").reverse().join("");
    for (i=0;i<columnName.length;i++){
        charValue =parseInt(columnName[i],36)-9
        toAdd=((26**i)*charValue)
        colNum += toAdd
    }
    return colNum
}

console.log(numberColumn("A"))
console.log(numberColumn("Z"))
console.log(numberColumn("AA"))
console.log(numberColumn("CA"))