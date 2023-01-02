

export const fizzBuzzFunction = (value : number): string => {
    if( value % 3 === 0 && value % 5 === 0)
        return `${value} - fizzbuzz`;
    else if (value % 3 === 0)
        return `${value} - fizz`;
    else if (value % 5 === 0)
        return `${value} - buzz`;
    else
        return `${value}`;
}

for (let i = 1; i <= 100; i++) {
    console.log(`${fizzBuzzFunction(i)}`)
}
