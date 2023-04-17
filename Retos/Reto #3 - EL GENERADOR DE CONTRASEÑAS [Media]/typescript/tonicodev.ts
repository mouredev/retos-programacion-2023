type LengthPass = 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16;

class CharactersBuilder {
    readonly letters = "abcdefghijklmnopqrstuvwxyz";
    readonly numbers = "0123456789";
    readonly symbols = "&/\\^=?!@#$%*+.,:;|()[]{}<>-_";
    characters = "";
    
    constructor(withUpperCase: boolean) {
        if (withUpperCase) {
            this.characters = this.letters.toUpperCase();
        } else {
            this.characters += this.letters;
        }
    }

    withNumbers(addNumbers: boolean): CharactersBuilder {
        if (addNumbers) {
            this.characters += this.numbers;
        }
        return this;
    }

    withSymbols(addSymbols: boolean): CharactersBuilder {
        if (addSymbols) {
            this.characters += this.symbols;
        }
        return this;
    }

    build(): string {
        return this.characters;
    }
}

function generateRandomPassword(length: LengthPass, withUpperCase: boolean = false, withNumbers: boolean = true, withSymbols: boolean = true): string {
    let characters =
        new CharactersBuilder(withUpperCase)
            .withNumbers(withNumbers)
            .withSymbols(withSymbols)
            .build();

    let password = "";
    for (let i = 0; i < length; i++) {
        password += characters[Math.floor(Math.random() * characters.length)];
    }
    return password;
}


//console.log(generateRandomPassword(7)); // No compila
console.log(generateRandomPassword(10));
console.log(generateRandomPassword(8, true));
console.log(generateRandomPassword(12, false,false,false));
console.log(generateRandomPassword(12, false,false,true));
 