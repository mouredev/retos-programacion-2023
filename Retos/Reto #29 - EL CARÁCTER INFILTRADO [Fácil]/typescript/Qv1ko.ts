infiltrator("The infiltrated character", "the infiltrat3d-character")

function infiltrator(base: string, str: string) {

    let characters: string[] = []

    if (base.length === str.length) {

        for (let i = 0; i < base.length; i++) {

            if (base[i] !== str[i]) {
                characters.push(str[i])
            }

        }

    }

    console.log(characters)

}
