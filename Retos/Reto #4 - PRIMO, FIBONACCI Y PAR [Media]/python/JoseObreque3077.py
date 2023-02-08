"""
Reto 4: Primo, Fibonacci y Par

Escribe un programa que, dado un número, compruebe y muestre si es primo,
fibonacci y par.
Ejemplos:
- Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
- Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
"""
from math import sqrt


class NumberChecker():
    """Clase para verificar propiedades de números enteros."""
    
    def __is_even(self, number):
        """
        Método privado que verifica si un número entero es par.
        
        Parametros:
            number: número entero mayor que cero.
            
        Retorna:
            True si el número es par, False en caso contrario.
        """
        return number % 2 == 0   
    
    def __is_fibonacci(self, number):
        """
        Método privado que verifica si un número entero pertenece a la
        secuencia de Fibonacci.
        
        Parámetros:
            number: número entero mayor que cero.
            
        Retorna:
            True si el número pertenece a la secuencia de Fibonacci, False en
            caso contrario.
        """
        # Valores iniciales de la secuencia de Fibonacci
        previous_fib = 0
        current_fib = 1
        
        # Obtención de valor de Fibonacci mayor o igual al entero dado
        while current_fib < number:
            previous_fib, current_fib = current_fib, previous_fib + current_fib
        
        return number == current_fib
    
    def __is_prime(self, number):
        """
        Método privado que verifica si un número entero es un número primo.
        
        Parámetros:
            number: número entero mayor que cero.
        
        Retorna:
            True si el número es primo, False en caso contrario.
        """
        # El número 1 no es primo
        if number == 1:
            return False
        
        # Se recorre desde 2 hasta raiz(n) buscando divisores
        for divisor in range(2, int(sqrt(number)) + 1):
            if number % divisor == 0:
                return False
        
        return True

    def multicheck(self, number):
        """
        Método que verifica si un número entero es par, primo y/o pertenece a
        la secuencia de Fibonacci.
        
        Muestra los resultados de estas verificaciones por consola.
        
        Parámetros:
            number: número entero mayor que cero.
        """
        # Excepcion para valores no admitidos
        if number <= 0 or not isinstance(number, int):
            error_message = 'Solo se aceptan números enteros mayores que cero.'
            raise(ValueError(error_message))
        
        # Validaciones/Comprobaciones
        validations = {
            'par': self.__is_even(number),
            'Fibonacci': self.__is_fibonacci(number),
            'primo': self.__is_prime(number)
        }
        
        # Entrega de Resultados
        print(f'Número evaluado: {number}')
        
        for label, result in validations.items():
            print(f"Es {label}: {'SI' if result else 'NO'}")
        print('')

if __name__ == '__main__':
    checker = NumberChecker()
    checker.multicheck(2)
    checker.multicheck(7)
    checker.multicheck(10.2) # Este caso arroja una excepción
