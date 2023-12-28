decimalConverter(21)

function decimalConverter(decimal) {
    let number = decimal
    let octal = ""
    let hex = ""
    let hexValues = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
    while(number > 0) {
        octal = number % 8 + octal
        number = Math.floor(number / 8)
    }
    octal = (octal === "")? "0" : octal
    console.log(decimal + " in octal is " + octal)
    number = decimal
    while(number > 0) {
        hex = hexValues[number % 16] + hex;
        number = Math.floor(number / 16)
    }
    hex = (hex === "")? "0" : hex;
    console.log(decimal + " in hex is 0x" + hex);
}
