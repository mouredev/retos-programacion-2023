# Reto #21: Números primos gemelos
#### Dificultad: Media | Publicación: 22/05/23 | Corrección: 29/05/23

## Enunciado

#
# Crea un programa que encuentre y muestre todos los pares de números primos
# gemelos en un rango concreto.
# El programa recibirá el rango máximo como número entero positivo.
# 
# - Un par de números primos se considera gemelo si la diferencia entre
#   ellos es exactamente 2. Por ejemplo (3, 5), (11, 13)
#
# - Ejemplo: Rango 14
#   (3, 5), (5, 7), (11, 13)
#

class PrimosGemelos:
    def __init__(self, fin):
        self.fin = fin

    def es_primo(self, numero):
        if numero < 2:
            return False
        for i in range(2, int(numero ** 0.5) + 1):
            if numero % i == 0:
                return False
        return True

    def numeros_primos_gemelos(self):
        gemelos = []
        for numero in range(3, self.fin - 1): # solo itero numeros impares
            if self.es_primo(numero) and self.es_primo(numero + 2):
                par = (numero, numero + 2)
                gemelos.append(par)
        return gemelos

if __name__ == "__main__":

    rango = int(input("Ingrese el número final del rango: "))

    pr = PrimosGemelos(rango)
    primos_gemelos = pr.numeros_primos_gemelos()
    print("Números primos gemelos en el rango dado:", primos_gemelos)
