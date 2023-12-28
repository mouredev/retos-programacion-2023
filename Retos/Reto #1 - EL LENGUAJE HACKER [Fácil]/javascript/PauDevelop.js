function leetTranslator (text) {
    const leet = ['o','L','R','E','A','S','b','T','B','g','4','|3', '[', ')', '3', '|=', '&', '#', '1', ',_|', '>|', '1', '^^', '^/', '0', '|*', '(_,)', '|2', '5', '7', '(_)', '|/', '(n)', '><', 'j', '2']
    const alfaNum = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    let translate = ''
    for (let i = 0; i < text.length; i++) {
        let character = text[i].toUpperCase()
        let position = alfaNum.indexOf(character)
        if (position >= 0) {
            translate += leet[position]
        } else {
            translate += text[i]
        }
    }
    return translate
}

console.log(leetTranslator('Esto es un mensaje de prueba'))