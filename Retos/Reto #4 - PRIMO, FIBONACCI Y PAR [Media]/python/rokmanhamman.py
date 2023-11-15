### RETO 4

"""/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo,
 * fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */"""

class Number():
    def __init__(self, num):
        self.value = num

    def check_even(self): #chequeo si es par
        if self.value % 2 == 0:
            paridad = "es par"
        else:
            paridad = "es impar"
        return paridad
    
    def check_fibonacci(self): #chequeo si pertenece a un numero de fibonacci
        fibo_list = [0, 1]
        while self.value > fibo_list[-1]:
            fibo_list.append(fibo_list[-2] + fibo_list[-1])
        
        if self.value in fibo_list:
            fibo = "es fibonacci"
        else:
            fibo = "no es fibonacci"
        
        return fibo

    def check_primo(self):
        if self.value < 2:
            primitud = "indefinido"
        else:
            list_resto=[]
            for w in range(1,self.value+1):
                resto = self.value % w
                list_resto.append(resto)
            
            if list_resto.count(0) == 2:
                primitud = "es primo"
            else:
                primitud = "no es primo"

        return primitud



n= Number(7)

print(f"{n.value}  {n.check_primo()}, {n.check_fibonacci()} y {n.check_even()}")


        
    
"""for x in range(50):
    print("------------------------------------------------")
    n= Number(x)
    print(f"{n.value} {n.check_primo()}, {n.check_fibonacci()} y {n.check_even()}")
"""





        