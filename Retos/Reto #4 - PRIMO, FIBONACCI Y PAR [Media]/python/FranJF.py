"""
/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */
"""
import math

class RetoCuatro():
    def __init__(self, numero:int):
        if type(numero) is not int:
            raise Exception("Necesito un numero valido.")
            
        resultado:str = f"{numero} "
        
        es_primo:bool = self.__es_primo(numero)
        es_fibonacci:bool = self.__es_fibonacci(numero)
        es_par:bool = True if numero % 2 == 0 else False
        
        resultado += "es primo, " if es_primo else "no es primo, "
        resultado += "es fibonacci " if es_fibonacci else "no es fibonacci "
        resultado += "y es par " if es_par else "y es impar"
        
        print(resultado)

    def __es_primo(self, numero:int):
        for i in range(2,numero):
            if (numero % i) == 0:
                return False
        return True

    def __es_fibonacci(self, numero:int):
        return self.__es_un_cuadrado_perfecto(5*numero*numero + 4) or self.__es_un_cuadrado_perfecto(5*numero*numero - 4)
    
    def __es_un_cuadrado_perfecto(self, numero:int):
        s = int(math.sqrt(numero))
        return s*s == numero
        
 
        
    
RetoCuatro(1)
RetoCuatro(5)
RetoCuatro(121)
