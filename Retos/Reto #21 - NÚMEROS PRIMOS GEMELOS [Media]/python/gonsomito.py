"""
 * Crea un programa que encuentre y muestre todos los pares de números primos gemelos en un rango concreto.
 * El programa recibirá el rango máximo como número entero positivo.
 * 
 * - Un par de números primos se considera gemelo si la diferencia entre
 *   ellos es exactamente 2. Por ejemplo (3, 5), (11, 13)
 *
 * - Ejemplo: Rango 14
 *   (3, 5), (5, 7), (11, 13)
"""
#funcion busca_primos_gemelos recorrerá el rango hasta el entero dado iterando cada vez. cada primo 
#que encuentre lo meterá en una lista. Al final, si hay primos suficientes crea una lista sólo con los gemelos.
#la devuelve e imprime
def busca_primos_gemelos(num):
    primos_totales = list()
    primos_gemelos = list()
    for n in range(2,num+1):
        es_primo=True
        for i in range(2, n):
            if n%i == 0:
                es_primo=False
                break
        if es_primo:
            primos_totales.append(n)
            if len(primos_totales)>1 and (primos_totales[-1]-primos_totales[-2] == 2):
                primos_gemelos.append((primos_totales[-2],primos_totales[-1]))
    return primos_gemelos

    
numero=input("DAME UN NÚMERO: ")
if numero.isdigit():
    print(busca_primos_gemelos(int(numero)))
else:
    print("NO ES UN VALOR CORRECTO!")
