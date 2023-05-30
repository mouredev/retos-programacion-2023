def decorador_mostrar_pares_gemelos(func):
    def wrapper(self):
        pares_gemelos = func(self)
        print(f"Pares de números primos gemelos en el rango dado ({self.rango_maximo}):")
        if pares_gemelos == []:
            print(f"No se encontraron pares Gemelos para este rango({self.rango_maximo}):")
 
        for par in pares_gemelos:
             print(par)
    return wrapper

class NumerosPrimosGemelos:
    def __init__(self, rango_maximo):
        self.rango_maximo = rango_maximo
        self.pares_gemelos = []

    def es_primo(self, num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    @decorador_mostrar_pares_gemelos
    def encontrar_pares_gemelos(self):
        for num in range(2, self.rango_maximo - 1):
            if self.es_primo(num) and self.es_primo(num + 2):
                self.pares_gemelos.append((num, num + 2))
        return self.pares_gemelos
if __name__ == "__main__":
    rango_maximo = int(input("Ingresa el rango máximo: "))
    numeros_primos_gemelos = NumerosPrimosGemelos(rango_maximo)
    numeros_primos_gemelos.encontrar_pares_gemelos()