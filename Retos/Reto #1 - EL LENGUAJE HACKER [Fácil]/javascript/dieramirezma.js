// Reto #1 - EL "LENGUAJE HACKER"

function leet(text) {
    text = text.toUpperCase()

    const leet_alphabet = {
        A: "4", B: "l3", C: "[", D: ")", E: "3",
        F: "|=", G: "&", H: "#", I: "1", J: ",_|",
        K: ">|", L: "1", M: "/\\/\\", N: "^/", O: "0",
        P: "|*", Q: "(_,)", R: "l2", S: "5", T: "7",
        U: "(_)", V: "\\/", W: "\\/\\/", X: "><", Y: "j",
        Z: "2", 1: "L", 2: "R", 3: "E", 4: "A", 5: "S",
        6: "b", 7: "T", 8: "B", 9: "g", 0: "o"
    }

    let leet_text = text.split("")
    
    for (let i = 0; i < leet_text.length; i++) {
        if (leet_alphabet[leet_text[i]]) {
            leet_text[i] = leet_alphabet[leet_text[i]]
        }
    }
    return leet_text.join("")
}


let text = "¡Hola Brais! Saludos desde Colombia"
const x = leet(text)

console.log("Texto original: " + text)
console.log("Texto codificado en lenguaje hacker: " + x)
