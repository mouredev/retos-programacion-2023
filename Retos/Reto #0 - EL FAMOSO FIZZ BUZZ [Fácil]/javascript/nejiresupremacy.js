for (let i = 1; i <= 100; i++) {
    let toPrint = i;

    if ((i % 3) === 0 && (i % 5 === 0)) toPrint = 'fizzbuzz';
    else if ((i % 3) === 0) toPrint = 'fizz';
    else if ((i % 5) === 0) toPrint = 'buzz';

    console.log(toPrint);
};