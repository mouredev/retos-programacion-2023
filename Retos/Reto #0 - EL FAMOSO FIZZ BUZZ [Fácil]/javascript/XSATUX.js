alert("RETO FIZZ BUZZ'");

for(x = 1;x <= 100;x++){
    if (x % 3 === 0 && x % 5 === 0) console.log(x + " fizzbuzz");
    else if (x % 5 === 0) console.log(x + " buzz");
    else if (x % 3 === 0) console.log(x + " fizz");
    else console.log(x)
}  