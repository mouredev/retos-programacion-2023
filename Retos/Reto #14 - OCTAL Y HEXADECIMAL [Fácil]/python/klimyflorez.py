# Reto #14: Octal y Hexadecimal
#### Dificultad: Fácil | Publicación: 03/04/23 | Corrección: 10/04/23
## Enunciado
#
# Crea una función que reciba un número decimal y lo trasforme a Octal
# y Hexadecimal.
# - No está permitido usar funciones propias del lenguaje de programación que
# realicen esas operaciones directamente.
#
class DecimalConverter:
    def __init__(self):
        pass
    
    def to_octal(self, num):
        if not isinstance(num, int):
            raise TypeError("El número debe ser entero.")
        if num < 0:
            raise ValueError("El número debe ser positivo.")
        octal_num = ""
        while num != 0:
            octal_num = str(num % 8) + octal_num
            num //= 8
        return octal_num
    
    def to_hexadecimal(self, num):
        if not isinstance(num, int):
            raise TypeError("El número debe ser entero.")
        if num < 0:
            raise ValueError("El número debe ser positivo.")
        hex_num = ""
        while num != 0:
            rem = num % 16
            if rem < 10:
                hex_num = str(rem) + hex_num
            else:
                hex_num = chr(ord('A') + rem - 10) + hex_num
            num //= 16
        return hex_num

if __name__ == '__main__':
    dc = DecimalConverter()
    while True:
        try:
            decimal_num = int(input("Ingrese un número decimal positivo: "))
            octal_num = dc.to_octal(decimal_num)
            hex_num = dc.to_hexadecimal(decimal_num)
            print("Octal:", octal_num)
            print("Hexadecimal:", hex_num)
            break
        except ValueError:
            print("El valor ingresado debe ser un número entero positivo.")
        except Exception as e:
            print(e)