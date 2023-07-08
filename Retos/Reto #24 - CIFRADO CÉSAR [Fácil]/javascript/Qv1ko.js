encrypt("Lorem ipsum dolor sit amet.", 6)
decrypt("gjmzh dknph yjgjm ndo vhzo.", 21)

function encrypt(text, number) {
    let result = ""
    const letters = text.toLowerCase().split("")
    letters.forEach(letter => {
        result += (letter < "a" || letter > "z") ? letter : (letter.charCodeAt(0) + number > 122)? String.fromCharCode(letter.charCodeAt(0) + number - 26) : String.fromCharCode(letter.charCodeAt(0) + number)
    })
    console.log(result)
}

function decrypt(cesar, number) {
    let result = ""
    const letters = cesar.toLowerCase().split("")
    letters.forEach(letter => {
        result += (letter < "a" || letter > "z")? letter : (letter.charCodeAt(0) - number < 97)? String.fromCharCode(letter.charCodeAt(0) - number + 26) : String.fromCharCode(letter.charCodeAt(0) - number)
    })
    console.log(result)
}
