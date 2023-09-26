'''
Reto #38: Las sumas
/*
 * Crea una función que encuentre todas las combinaciones de los números
 * de una lista que suman el valor objetivo.
 * - La función recibirá una lista de números enteros positivos
 *   y un valor objetivo.
 * - Para obtener las combinaciones sólo se puede usar
 *   una vez cada elemento de la lista (pero pueden existir
 *   elementos repetidos en ella).
 * - Ejemplo: Lista = [1, 5, 3, 2],  Objetivo = 6
 *   Soluciones: [1, 5] y [1, 3, 2] (ambas combinaciones suman 6)
 *   (Si no existen combinaciones, retornar una lista vacía)
 */
'''

def trobar_combinacio(target, numeros, combinacio_actual=[], suma_actual=0):
    global comptador

    if suma_actual == target:
        print("Combinació trobada:", combinacio_actual)
        comptador += 1
    elif suma_actual > target:
        return
    else:
        for i in range(len(numeros)):
            numero_actual = numeros[i]
            nous_numeros = numeros[i+1:]
            nova_combinacio = combinacio_actual + [numero_actual]
            nova_suma = suma_actual + numero_actual
            trobar_combinacio(target, nous_numeros, nova_combinacio, nova_suma)

# MAIN #############################################
if __name__ == "__main__":
    llista = input("numeros enters separats per coma:\n")
    target = int(input("numero enter com a objectiu del sumatori:\n"))
    comptador = 0

    numeros = []
    llista = llista.split(",")
    for num in llista:
        numeros.append(int(num))

    sumainicial = sum(numeros)
    if sumainicial < target:
        print([])
    else:
        trobar_combinacio(target, numeros)
        if comptador == 0:
            print([])
        else:
            print("S'han trobat", comptador, "combinacions")
