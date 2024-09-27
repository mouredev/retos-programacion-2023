def primo_fibonacci_par():

    numero = int(input('ingresa un numero'))

    def primo():
        for i in range (2, numero):
            if numero%i == 0:
                return "no es primo"
        return "es primo"


    def fibonacci():
        n1 = 0
        n2 = 1
        suma = 0
        while suma < numero:
            suma = n1 + n2
            n1 = n2  
            n2 = suma
            if suma == numero:
                return "es fibonacci"
            elif suma > numero:
                return "no es fibonacci"
            

    def par():
        if numero % 2 == 0:
            return "es par"
        else:
            return "es impar"
        
    print(f'el numero {numero} {primo()}, {fibonacci()} y {par()}')


primo_fibonacci_par()
    




