class ValidadorExpresion:
    def __init__(self, expresion):
        self.expresion = expresion
        self.elementos = self.expresion.split()
        self.operadores = ['+', '-', '*', '/', '%']

    def validar_expresion(self):
        for elemento in self.elementos:
            if elemento.isdigit() or elemento.replace('.', '', 1).isdigit():
                continue
            elif elemento not in self.operadores:
                return False
        return True


def validar_decorador(func):
    def wrapper(expresion):
        elementos = expresion.split()
        operadores = ['+', '-', '*', '/', '%']
        for elemento in elementos:
            if elemento.isdigit() or elemento.replace('.', '', 1).isdigit():
                continue
            elif elemento not in operadores:
                return False
        return func(expresion)
    return wrapper


@validar_decorador
def validar_expresion(expresion):
    return True


if __name__ == '__main__':
    expresion_1 = "5 + 6 / 7 - 4"
    expresion_2 = "5 a 6"
    expresion_3 = "5 $ 6"


    validador = ValidadorExpresion(expresion_1)

    validador.expresion = expresion_2
    print(validar_expresion(expresion_1))  # Output: True
    print(validar_expresion(expresion_2))  # Output: False
    print(validar_expresion(expresion_3))  # Output: False
