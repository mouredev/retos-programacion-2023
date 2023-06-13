encrypt("Lorem ipsum dolor sit amet.", 6)
decrypt("gjmzh dknph yjgjm ndo vhzo.", 21)

function encrypt(text: string, numberEncrypt: number): void {
    let result = ""
    const letters = text.toLowerCase().split("")
    letters.forEach((letter: string) => {
        result += (letter < "a" || letter > "z")? letter : (letter.charCodeAt(0) + numberEncrypt > 122) ? String.fromCharCode(letter.charCodeAt(0) + numberEncrypt - 26) : String.fromCharCode(letter.charCodeAt(0) + numberEncrypt)
    })
    console.log(result)
}

function decrypt(cesar: string, numberDecrypt: number): void {
    let result = ""
    const letters = cesar.toLowerCase().split("")
    letters.forEach((letter: string) => {
        result += (letter < "a" || letter > "z")? letter : (letter.charCodeAt(0) - numberDecrypt < 97) ? String.fromCharCode(letter.charCodeAt(0) - numberDecrypt + 26) : String.fromCharCode(letter.charCodeAt(0) - numberDecrypt)
    })
    console.log(result)
}
