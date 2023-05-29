def es_primo(n):
    if n <= 1:
        return False
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    
    return True

def encontrar_pares_primos_gemelos(rango_maximo):
    pares_gemelos = []
    
    for i in range(2, rango_maximo - 1):
        if es_primo(i) and es_primo(i + 2):
            pares_gemelos.append((i, i + 2))
    
    return pares_gemelos

rango_maximo = int(input("Ingrese el rango máximo: "))

pares_gemelos = encontrar_pares_primos_gemelos(rango_maximo)

print("Pares de números primos gemelos encontrados:")
for par in pares_gemelos:
    print(par)
