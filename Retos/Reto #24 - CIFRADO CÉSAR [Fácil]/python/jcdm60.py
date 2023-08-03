# Reto #24: Cifrado César
#### Dificultad: Fácil | Publicación: 12/06/23 | Corrección: 19/06/23

## Enunciado

#
# Crea un programa que realize el cifrado César de un texto y lo imprima.
# También debe ser capaz de descifrarlo cuando así se lo indiquemos.
#
# Te recomiendo que busques información para conocer en profundidad cómo
# realizar el cifrado. Esto también forma parte del reto.
#

class CifradorCesar:
    def __init__(self, desplazamiento):
        self.desplazamiento = desplazamiento

    def cifrar(self, texto):
        resultado = self.transformar_texto(texto, self.desplazamiento)
        return resultado

    def descifrar(self, texto):
        resultado = self.transformar_texto(texto, -self.desplazamiento)
        return resultado

    def transformar_texto(self, texto, desplazamiento):
        resultado = ""
        for caracter in texto:
            if caracter.isalpha():
                codigo = ord(caracter) + desplazamiento
                if caracter.isupper():   # Letras mayúsculas
                    codigo = (codigo - 65) % 26 + 65
                else:                    # Letras minúsculas
                    codigo = (codigo - 97) % 26 + 97
                caracter_transformado = chr(codigo)
                resultado += caracter_transformado
            else:
                resultado += caracter
        return resultado


class ConsolaUsuario:
    def ejecutar(self):
        texto = input("Ingrese el texto: ")
        desplazamiento = int(input("Ingrese el desplazamiento: "))
        modo = input("Ingrese 'cifrar' o 'descifrar': ")

        cifrador = CifradorCesar(desplazamiento)

        if modo.lower() == "cifrar":
            resultado = cifrador.cifrar(texto)
        elif modo.lower() == "descifrar":
            resultado = cifrador.descifrar(texto)
        else:
            resultado = "Modo inválido. Ingrese 'cifrar' o 'descifrar'."

        print("Resultado:", resultado)


if __name__ == "__main__":
    consola_usuario = ConsolaUsuario()
    consola_usuario.ejecutar()
