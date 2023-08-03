import math

class twinPrimes():
    def __init__(self):
        self.twin1 = 2
        self.twin2 = 0
        self.result = ""

    def is_prime(self, num):
        if (num==0 or num==1):
            return False
        for x in range(2, int(math.sqrt(num) + 1)):
            if num % x == 0:
                return False
        return True

    def print_result(self, tw1, tw2):
        self.result += ("" if len(self.result)==0 else ", ") + "(" + str(tw1) + ", " + str(tw2) + ")"

    def twins(self, x):
        if x - self.twin1 == 2:
            self.twin2 = x
            self.print_result(self.twin1, self.twin2)
            self.twin1 = self.twin2
        else:
            self.twin1 = x

    def ranges(self, ran):
        for x in range(ran+1):
            if self.is_prime(x):
                self.twins(x)
        print(self.result)

try:
    valor = int(input("Ingrese un rango: "))
    twin_primes = twinPrimes()
    if valor >= 5:
        twin_primes.ranges(valor)
    else:
        print("Valor mínimo es: 5")
except:
    print('Solo ingresar números')
