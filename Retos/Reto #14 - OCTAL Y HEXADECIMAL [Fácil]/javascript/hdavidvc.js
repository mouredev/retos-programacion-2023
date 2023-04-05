
let octal = [];
let hex = [];
let temp;
let result = ''
let hexas = {
    10: 'A',
    11: 'B',
    12: 'C',
    13: 'D',
    14: 'E',
    15: 'F'
}
function calculo(decimal,base,array){
    while(decimal>=1) {
        temp = decimal % base;
        decimal= parseInt(decimal/base);
        array.push(temp)        
    }
    if (decimal ==1) array.push(decimal)
    array.reverse();
}
function DecimalToOctal(decimal) {
    result = ''
    calculo(decimal,8,octal);
    octal.forEach(element =>  result+= element.toString());
    return result
}

function DecimalToHex(decimal) {
    result = ''
    calculo(decimal,16,hex);
    hex.forEach((element,i) =>  
        {
            if(element > 9) {
                hex[i] = hexas[element]
            }
            result+= hex[i].toString()
        });

        return result
        }
function main(decimal) {
   console.log("En Decimal: " + decimal);
   console.log("En Octal: "+ DecimalToOctal(decimal));
   console.log("En Hexadecimal: "+ DecimalToHex(decimal));   
}
main(987)