for (let index = 1; index <= 100; index++) {
    let divisibleByThree = index % 3 === 0;
    let divisibleByFive = index % 5 === 0;
    
    if (divisibleByThree && divisibleByFive) console.log(index, 'fizzbuzz');
    else if (divisibleByThree) console.log(index, 'fizz');
    else if (divisibleByThree) console.log(index, 'buzz');
    else console.log(index);
}