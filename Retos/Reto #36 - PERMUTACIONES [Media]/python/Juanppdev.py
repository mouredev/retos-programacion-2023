# Función iterativa para generar todas las permutaciones de una string en Python
def permutations(s):
 
    # Caja base
    if not s:
        return []
 
    # crear una lista para almacenar permutaciones (parciales)
    partial = []
 
    # inicializa la lista con el primer carácter de la string
    partial.append(s[0])
 
    # do para cada carácter de la string especificada
    for i in range(1, len(s)):
 
        # considerar permutaciones parciales previamente construidas una por una
 
        # iterar hacia atrás
        for j in reversed(range(len(partial))):
 
            # eliminar la permutación parcial actual de la lista
            curr = partial.pop(j)
 
            for k in range(len(curr) + 1):
                partial.append(curr[:k] + s[i] + curr[k:])
 
    print(partial, end='')
 
 
if __name__ == '__main__':
 
    s = 'ABC'
    permutations(s)