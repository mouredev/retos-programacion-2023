FizzBuzz(100)

function FizzBuzz (limit)
{
    for (let i = 1; i <= limit; i++)
    {
        console.log((( i % 3 == 0) && ( i % 5 == 0)) ? "Fizzbuzz" : ( i % 3 == 0) ? "Fizz" : ( i % 5 == 0) ? "Buzz" : i)
    }
}