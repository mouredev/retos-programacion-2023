# Lógica de la función.

# En función de si es negativo, 0 o positivo el número a dibujar se toma un valor u otro.
# Como para hacer la escalera hacia arriba hay que comenzar dibuando los escalones más alejados,
# se guardan todos los espacios necesarios en la variable "espacio y se utiliza espacio[:-2]
# para ir borrando los necesarios en cada paso.

def escalera(escalones):
    espacio = ""
    if escalones == 0:
        print("__")
    elif escalones > 0:
        for i in range(0,escalones):
            espacio = espacio + "  "
        print(espacio + "_")
        for i in range(0,escalones):
            espacio = espacio[:-2]
            print(espacio + "_|")
    elif escalones < 0:
        print("_")
        espacio = espacio + " "
        for i in range(0,-escalones):
            print(espacio + "|_")
            espacio = espacio + "  "

