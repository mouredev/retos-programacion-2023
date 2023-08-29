passGen(10, true, false, true)

function passGen(len: number, upper: boolean, num: boolean, simb: boolean) {

    let password = ""

    let chars = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    const upperLetters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    const numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    const simbols = ["`", "~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "{", "]", "}", "\\", "|", ";", ":", "'", "\"", ",", "<", ".", ">", "/", "?"]

    len = (len < 8)? 8 : (len > 16)? 16 : len;

    if (upper) {
        chars.push(...upperLetters)
    }

    if (num) {
        chars.push(...numbers)
    }

    if (simb) {
        chars.push(...simbols)
    }

    for (let i = 0; i < len; i++) {
        password += chars[Math.floor(Math.random() * chars.length)]
    }

    console.log(password)

}
