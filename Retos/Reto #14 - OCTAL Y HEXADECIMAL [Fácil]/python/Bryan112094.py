# Crea una función que reciba un número decimal y lo trasforme a Octal
# y Hexadecimal.
# - No está permitido usar funciones propias del lenguaje de programación que
# realicen esas operaciones directamente.

class decimal:
    def __init__(self):
        pass

    def convertTo(self, numero, base):
        result = []
        hexa_code = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

        while numero >= base:
            resto = int(numero % base)
            numero = int(numero / base)
            if resto > 9 and base == 16:
                result.insert(0, hexa_code[resto])
            else:
                result.insert(0, str(resto))

        result.insert(0, str(numero))
        valor = "".join(result)
        
        return valor
    
    def start(self):
        numero = input("Ingrese el número decimal positivo: ")
        try:
            numero = int(numero)
            if numero >= 0:
                print(f"En octal es: {self.convertTo(numero, 8)}")
                print(f"En hexadecimal es: {self.convertTo(numero, 16)}")
            else:
                print('Valor ingresado es negativo')
        except ValueError:
            print('Valor ingresado incorrecto')

convertir = decimal()
convertir.start()
