function isHeterograma(text) {
    const letters = text.toLowerCase().split("");
    const lettersCount = {};
    letters.forEach((l) => {
        lettersCount[l] = 0;
    });
    letters.forEach((l) => {
        if (Object.keys(lettersCount).includes(l)) {
            lettersCount[l]++;
        }
    });
    return Object.values(lettersCount).every((l) => l == 1);
}

function isPangrama(text) {
    const accents = {
        á: "a",
        é: "e",
        í: "i",
        ó: "o",
        ú: "u",
        ü: "u",
    };
    const letters = text
        .toLowerCase()
        .split("")
        .filter(
            (l) =>
                l != " " &&
                l != "." &&
                l != "," &&
                l != "!" &&
                l != ":" &&
                l != "¡" &&
                l != "?" &&
                l != "¿",
        )
        .map((l) => (accents[l] ? accents[l] : l));
    const lettersSet = new Set(letters);
    return lettersSet.size == 27;
}
