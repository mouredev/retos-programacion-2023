def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def encontrar_pares_gemelos(rango_maximo):
    pares_gemelos = []
    for numero in range(2, rango_maximo - 1):
        if es_primo(numero) and es_primo(numero + 2):
            pares_gemelos.append((numero, numero + 2))
    return pares_gemelos

rango_maximo = int(input("Ingrese el rango máximo: "))
pares_gemelos = encontrar_pares_gemelos(rango_maximo)
print("Los pares de números primos gemelos en el rango", rango_maximo, "son:")
for par in pares_gemelos:
    print(par)