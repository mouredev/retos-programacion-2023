def suma_objetivo(lista, n):
    def encontrar_combinaciones(objetivo, indice, combinaciones):
        if objetivo == 0:
            solucion.append(sorted(combinaciones[:]))
            return
        if objetivo < 0 or indice == len(lista):
            return
        for i in range(indice, len(lista)):
            combinaciones.append(lista[i])
            encontrar_combinaciones(objetivo - lista[i], i + 1, combinaciones)
            combinaciones.pop()

    solucion = []
    encontrar_combinaciones(n, 0, [])
    
    # Eliminamos los duplicados usando set y sorted para ordenar
    solucion = list(set(tuple(sorted(combinacion_final)) for combinacion_final in solucion))
    return [list(combinacion_final) for combinacion_final in solucion]

print(suma_objetivo([2, 1, 3, 1, 4], 6))