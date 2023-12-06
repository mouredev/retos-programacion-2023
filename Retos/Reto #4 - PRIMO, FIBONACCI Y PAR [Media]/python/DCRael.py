import math

class Tipo_number():

    def isperfectsquare(self, x):
        s = int(math.sqrt(x))
        if s * s == x:
            return 'Es fibonacci'
        else:
            return 'No es fibannaci'

    def isfibo(self, n):
        return self.isperfectsquare(5*n*n + 4) or self.isperfectsquare(5*n*n - 4)

    def is_par(self, n):
        if n % 2 == 0:
            return 'Es par'
        else:
            return 'Es impar'


    def is_primo(self, n):
        if n <= 1:
            return 'No es primo'
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return 'No es primo'
        return 'Es primo'

try:    
    num = int(input('Ingresa un numero: '))
    n = Tipo_number()
    print(f'{num}: {n.isfibo(num)}, {n.is_par(num)},y {n.is_primo(num)}')
except:
    print('numero ingresado invalido')
