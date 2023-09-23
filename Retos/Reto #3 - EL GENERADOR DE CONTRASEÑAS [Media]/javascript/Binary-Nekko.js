const ascii = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '!', '"', '#', '$', '%', '&', '_', '?', '@']

const passwordGenerator = (limit = 8) => {
    let password = ''

    for (let i = 0; i < limit; i++) {
        const randomEl = ascii[Math.floor(Math.random() * ascii.length)]
        password += randomEl
    }

    console.log(password)
}

// Puedes especificar la longitud de la contraseña,
// pero por defecto es 8
passwordGenerator(16)
