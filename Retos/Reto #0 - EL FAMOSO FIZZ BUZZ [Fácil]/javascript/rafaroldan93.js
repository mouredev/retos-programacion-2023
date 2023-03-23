let n = 1;
while (n <= 100) {
    if (n % 3 == 0 && n % 5 == 0) {
        console.log("fizzbuzz");
    } else if (n % 3 == 0) {
        console.log("fizz");
    } else if (n % 5 == 0) {
        console.log("buzz");
    } else {
        console.log(n);
    }
    n += 1;
}