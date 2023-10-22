import numpy as np

def calculateSum(list_numbers: list, target: int) -> None:
    matriz_numbers = []
    res = []

    # Crea una primera matriz con todas las opciones posibles a nivel lista
    for i, number in enumerate(list_numbers):
        matriz_numbers.append(list_numbers.copy())
        list_numbers.append(list_numbers.pop(0))

    # Bucle para ir realizando todas las combinaciones posibles de cada una de las listas de la matriz
    for list_ in matriz_numbers:
        i = 1
        while i < len(list_):
            # Primera tanda de elementos a sumar
            first_numbers = list_[:i]
            
            # Crea una copia del listado original, eliminando los elementos que ya están en la primera tanda a sumar
            list_rest = list_.copy()
            _ = [list_rest.remove(n) for n in first_numbers]
            
            # Bucle for para ir sumando la primera tanda con el resto de elementos individualmente
            for number in list_rest:
                # Si encuentra una solución, comprueba que ya no esta en el resultado y la añade
                if np.sum(first_numbers) + np.sum(number) == target:
                    result = first_numbers + [number]
                    result.sort()

                    if not result in res:
                        res.append(result)

            i += 1

    print(f'Respuesta: {res}')

if __name__ == '__main__':
    # Se debería realizar un filtra más correcto de los dos inputs para filtrar errores
    list_ = input('Introduce una lista con números. Ejemplo: [1, 2, 3, 2]: \n')
    list_ = (
        list_.replace('[', '')
        .replace(']', '')
        .split(',')
    )
    list_ = [int(n) for n in list_]
    
    n_target = int(input('Introduce el número objetivo:\n'))
    calculateSum(list_, int(n_target))
