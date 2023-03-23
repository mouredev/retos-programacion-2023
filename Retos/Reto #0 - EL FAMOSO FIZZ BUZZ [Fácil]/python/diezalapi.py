def famous_fizz_buzz():
    numbers = list(range(1,101))
    fizzbuzz = map(
        lambda x: 
        'fizzbuzz' if not (x % 15) else 'fizz' if not (x % 3) else 'buzz' if not (x % 5) else x, 
        numbers
        )
    print(*fizzbuzz, sep='\n')

famous_fizz_buzz()