""" Escribe un programa que, dado un número, compruebe y muestre si es primo,
    fibonacci y par.
    Ejemplos:
    - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
    - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"""


class CracteristicaNumero:
    # Constructor
    def __init__(self, numero):
        if type(numero) is not int:
            raise Exception("Error, es necesario un numero entero.")

        resultado = f'El numero {numero}, '

        par: bool = self._es_par(numero)
        primo: bool = self._es_primo(numero)
        fibo: bool = self._es_fibo(numero)

        if par == True:
            resultado += 'es par, '
        else:
            resultado += 'no es par, '

        if primo == True:
            resultado += 'es primo '
        else:
            resultado += 'no es primo '
        if fibo == True:
            resultado += 'y es fibonacci.'
        else:
            resultado += 'y no es fibonacci.'

        print(resultado)

    def _es_par(self, numero):
        if numero % 2 == 0:
            return True
        else:
            return False

    def _es_primo(self, numero):
        for x in range(2, numero):
            if numero % x == 0:
                return False
        return True

    def _es_fibo(self, numero):
        a, b = 0, 1
        while b < numero:
            a, b = b, a + b
        return True if b == numero else False


CracteristicaNumero(3)
CracteristicaNumero(20)
CracteristicaNumero(15)
CracteristicaNumero(8)