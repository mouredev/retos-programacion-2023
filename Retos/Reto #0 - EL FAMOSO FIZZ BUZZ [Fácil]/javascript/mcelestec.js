const fizzBuzz = (inf, sup) => {
    for (let i = inf; i <= sup; i++) {
        const text = `${i % 3 === 0 ? 'fizz' : ''}${i % 5 === 0 ? 'buzz' : ''}`;
        console.log(text ? text : i);
    }
}

fizzBuzz(1, 100);