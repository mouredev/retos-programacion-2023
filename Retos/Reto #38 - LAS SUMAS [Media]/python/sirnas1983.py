def las_sumas(lista : list, objective : int) -> list[list]:
    resultado = []
    for x,elem in enumerate(lista):
        for y in range(x + 1, len(lista)):
            parcial = []
            parcial.append(elem)
            for z in range(y, len(lista)):
                if lista[z] + sum(parcial) == objective:
                    parcial.append(lista[z])
                    resultado.append(parcial)
                    break
                elif lista[z] + sum(parcial) > objective:
                    break
                else:
                    parcial.append(lista[z])
    return resultado
