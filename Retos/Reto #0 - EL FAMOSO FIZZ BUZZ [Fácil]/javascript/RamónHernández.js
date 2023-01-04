

for(let i = 1; i <= 100; i++){
    
    (i % 3 === 0 && i % 5 === 0) ? console.log("fizzbuzz") 
    : (i % 3 === 0) ? console.log("fizz")
    : (i % 5 === 0) ? console.log("buzz") : console.log(i);
}
