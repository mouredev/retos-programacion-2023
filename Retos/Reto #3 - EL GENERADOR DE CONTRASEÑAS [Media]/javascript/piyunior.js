async function generatePassword() {
    const letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    let min = Math.ceil(0);
    let max = Math.floor(26);
    let character = '';
    let count = 1
    let limit = Math.round(Math.random() * 16)
    let lastLetter = '';
    while (limit < 8) {
        limit = Math.round(Math.random() * 16)
    }
    while (count < limit) {
        let upperCase = Math.round(Math.random() * 49) % 7 == 0
        let aleatory = upperCase ? String(letters[Math.floor(Math.random() * (max - min) + min)]).toLowerCase() : String(letters[Math.floor(Math.random() * (max - min) + min)]).toUpperCase();
        lastLetter = aleatory;
        character += aleatory;
        count += 1
    }
    do {
        character = character.concat(Math.round(Math.random() * 14))
    } while (character.length == 16);
    console.log(character)
}

generatePassword();