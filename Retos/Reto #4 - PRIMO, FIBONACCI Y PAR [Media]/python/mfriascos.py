class Number: 

    def __init__(self,number) -> None:
        self.number = number


    def prime_number(self):
        if self.number > 2:
            for i in range(2,self.number):
                if self.number % i == 0:
                    return "no es primo"
            
        return "es primo"


    def fibonacci_number(self):
        fibo_numbers = [0,1]
        add = 0
        item = 0
        while add <= self.number:
            add = fibo_numbers[item] + fibo_numbers[item+1]
            fibo_numbers.append(add)
            item += 1
        
        if self.number in fibo_numbers:
            return 'fibonacci'

        return "no es fibonacci"

    def even_number(self):
        if self.number % 2 == 0:
            return "es par"
        
        return "es impar"

num = int(input('\nType a number -> '))

while num < 0:
    print('\nError')
    num = int(input('\n Type a number -> '))

number = Number(num)

print(f"\n {num} {number.prime_number()}, {number.fibonacci_number()} y {number.even_number()}\n")
