def comparar_cadenas(cadena1: str, cadena2: str) -> list[str]:
    n = len(cadena1)
    m = len(cadena2)
    s = min(n, m)
    letras_diferentes = []
    for i in range(s):
        if cadena1[i] != cadena2[i]:
            letras_diferentes.append(cadena2[i])
    if n > m:
        for k in range(m, n):
            letras_diferentes.append("")
    elif m > n:
        for j in range(n, m):
            letras_diferentes.append(cadena2[j])
    return letras_diferentes


# Se debe ingresar primero la cadena original
# y luego la cadena a comparar, ambas separadas por un salto de linea.
if __name__ == "__main__":
    cadena1 = input().strip()
    cadena2 = input().strip()
    letras_diferentes = comparar_cadenas(cadena1, cadena2)
    print(letras_diferentes)
