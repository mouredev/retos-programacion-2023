function fizzBuzz(){
    return Array.from(
        { length : 100 }, (value, key) => {
            const number = key + 1;
            return (number % 3 === 0 && number % 5 === 0)
            ? 'fizzbuzz'
            : (number % 3 === 0) 
                ? 'fizz'
                : (number % 5 === 0)
                    ? 'buzz'
                    : number;
    }).join('\n')
}

console.log(fizzBuzz());