// Reto #0 - EL FAMOSO "FIZZ BUZZ"

function FIZZ_BUZZ() {
    for (let i = 1; i < 101; i++) {
        if (i % 3 === 0) {
            if (i % 5 === 0) {
                console.log("fizzbuzz")
            } else {
                console.log("fizz");
            }
        } else if (i % 5 === 0) {
            console.log("buzz")
        } else {
            console.log(i)
        }
    }
}

FIZZ_BUZZ()