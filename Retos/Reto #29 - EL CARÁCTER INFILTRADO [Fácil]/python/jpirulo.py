from termcolor import colored

class ComparadorCadenas:
    def __init__(self, cadena1, cadena2):
        self.cadena1 = cadena1
        self.cadena2 = cadena2
        self.longitud = len(cadena1)
        self.diferencias = []

    def encontrar_diferencias(self):
        for i in range(self.longitud):
            if self.cadena1[i] != self.cadena2[i]:
                self.diferencias.append(colored(self.cadena2[i], 'red'))
            else:
                self.diferencias.append(self.cadena2[i])

    def mostrar_diferencias(self):
        print("Diferencias: " + " ".join(self.diferencias))

def resaltar_diferencias(func):
    def wrapper(*args, **kwargs):
        comparador = func(*args, **kwargs)
        comparador.encontrar_diferencias()
        comparador.mostrar_diferencias()
    return wrapper

@resaltar_diferencias
def obtener_cadenas():
    cadena1 = input("Ingrese la primera cadena de texto: ")
    cadena2 = input("Ingrese la segunda cadena de texto: ")
    return ComparadorCadenas(cadena1, cadena2)

if __name__ == "__main__":
    obtener_cadenas()
