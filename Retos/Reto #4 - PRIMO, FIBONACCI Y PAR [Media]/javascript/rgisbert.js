/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */

class analyzeNumber {
    #number;

    constructor(number) {
        this.#number = number;
    }

    isFibonacci() {
        const fibonacci = [1];
        
        while (fibonacci.at(-1) < this.#number) {
            const last = fibonacci.at(-1)
            const penultimate = fibonacci.length > 1 ? fibonacci.at(-2) : 0;
        
            fibonacci.push(last + penultimate)
        }
        
        return fibonacci.includes(this.#number);
    }

    isPair() {
        return this.#number % 2 === 0;
    }

    isPrime() {
        if (this.#number === 0 || this.#number === 1) return "no es primo";

        return new Array(this.#number - 1)
            .fill()
            .map( (_, i) => i+2)
            .every( n => this.#number === n ? true : !(this.#number % n === 0));
    }

    resultChallenge4() {
        const result = `${this.isPrime() ? "" : "no "}es primo,` +
        `${this.isFibonacci() ? "" : " no"} es fibonacci y ` +
        `es ${this.isPair() ? "par" : "impar"}`;

        return `${this.#number} ${result}.`
    }
}

num = new analyzeNumber(2)
console.log(num.resultChallenge4());
