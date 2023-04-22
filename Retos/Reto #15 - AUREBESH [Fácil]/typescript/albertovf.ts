const mapping = { 'a': 'æ', 'b': '“', 'c': '¢', 'd': 'ð', 'e': '€', 'f': 'đ', 'g': 'ŋ', 'h': 'ħ', 'i': '→', 'j': 'ˀ', 'k': 'ĸ', 'l': 'ł', 'm': 'µ', 'n': 'µ', 'o': 'ø', 'p': 'þ', 'q': '@', 'r': '¶', 's': 'ß', 't': 'ŧ', 'u': '↓', 'v': '„', 'w': 'ſ', 'x': '»', 'y': '←', 'z': '«', }

// const mapping = { 'a': '⠈⠁', 'b': '⠈⠃', 'c': '⠈⠉', 'd': '⠈⠙', 'e': '⠈⠑', 'f': '⠈⠋', 'g': '⠈⠛', 'h': '⠈⠓', 'i': '⠈⠊', 'j': '⠈⠚', 'k': '⠈⠅', 'l': '⠈⠇', 'm': '⠈⠍', 'n': '⠈⠝', 'o': '⠈⠕', 'p': '⠈⠏', 'q': '⠈⠟', 'r': '⠈⠗', 's': '⠈⠎', 't': '⠈⠞', 'u': '⠈⠥', 'v': '⠈⠧', 'w': '⠈⠺', 'x': '⠈⠭', 'y': '⠈⠽', 'z': '⠈⠵', '0': '⠐⠴', '1': '⠄', '2': '⠆', '3': '⠒', '4': '⠲', '5': '⠢', '6': '⠖', '7': '⠶', '8': '⠦', '9': '⠔', }

function humanToAurebesh(text: string): string {
    let result = '';

    for (let i = 0; i < text.length; i++) {
        const char = text[i].toLowerCase();
        result += mapping[char] || char;
    }
    return result;
}

function aurebeshToHuman(text: string): string {
    const mappingReverse = Object.fromEntries(Object.entries(mapping).map(([k, v]) => [v, k]))
    let result = '';

    for (let i = 0; i < text.length; i++) {
        const char = text.charAt(i);
        result += mappingReverse[char] || char;
    }
    return result;
}

function reto(text: string, human: boolean) {
    human ? console.log(humanToAurebesh(text)) : console.log(aurebeshToHuman(text))
}

let text1 = "a b c d e f g h i j k l m n o p q r s t u v w x y z - 0 1 2 3 4 5 6 7 8 9"
let text2 = "æ “ ¢ ð € đ ŋ ħ → ˀ ĸ ł µ µ ø þ @ ¶ ß ŧ ↓ „ ſ » ← « - 0 1 2 3 4 5 6 7 8 9"

reto(text1, true)
reto(text2,false)