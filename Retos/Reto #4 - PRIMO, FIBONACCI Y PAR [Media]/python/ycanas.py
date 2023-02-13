class Number():
    def __init__(self, n):
        self.n = n

    def is_fibonacci(self):
        fib, num = 0, 1

        while fib < self.n:
            piv = fib
            fib = fib+num
            num = piv

        return True if self.n == fib else False

    def is_even(self):
        return self.n % 2 == 0

    def is_prime(self):
        if self.n < 2:
            return False

        if self.n > 2 and self.is_even():
            return False

        for i in range(2, self.n//2):
            if self.n % i == 0:
                return False

        return True

    def check(self):
        result = ""
        
        result += f"{self.n} es primo, " if self.is_prime() else f"{self.n} no es primo, "
        result += f"es fibonacci " if self.is_fibonacci() else f"no es fibonacci "
        result += f"y es par" if self.is_even() else f"y no es par"

        return result


number = Number(2)
print(number.check())
