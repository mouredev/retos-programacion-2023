# /*
# * Crea una función que dibuje una escalera según su número de escalones.
# * - Si el número es positivo, será ascendente de izquiera a derecha.
# * - Si el número es negativo, será descendente de izquiera a derecha.
# * - Si el número es cero, se dibujarán dos guiones bajos(__).
# *
# * Ejemplo: 4
# *         _
# *       _|
# *     _|
# *   _|
# * _|
# *
# */

# /**
# * Función que imprime una escalera de un determinado número de escalones
# * @ param steps número de escalones de la escalera
# */
def print_steps(steps):
    if steps == 0:
        print("__")
    else:
        if steps > 0:
            print(" " * (steps * 2) + "_")
        else:
            print("_")
        steps_recursive(steps, 1)


# /**
# * Función recursiva que imprime los escalones de la escalera
# * @ param steps número de escalones de la escalera
# * Si el número de escalones es positivo, la escalera es ascendente y si es negativo, es descendente
# */
def steps_recursive(steps, currentStep):
    # Caso base
    if currentStep > abs(steps):
        return
    if steps > 0:
        print(" " * ((steps - currentStep) * 2) + "_|")
    else:
        print(" " * ((currentStep) * 2-1) + "|_")

    # LLamada recursiva
    steps_recursive(steps, currentStep + 1)



# Función principal
def main():
    print_steps(14)
    print_steps(-7)
    print_steps(0)


main()