escalones = "x"
espacio = ""

# Pedimos el número entero para definir la escalera asegurándonos de que sea entero y que
# se repita si no es así. 

while type(escalones) != int:
    try:
        escalones = int(input("¿Cuántos escalones tiene la escalera a dibujar?"))
    except:
        print("No has introducido un número entero, vuelve a intentarlo")

# Lógica del programa.

# En función de si es negativo, 0 o positivo el número a dibujar se toma un valor u otro.
# Como para hacer la escalera hacia arriba hay que comenzar dibuando los escalones más alejados,
# se guardan todos los espacios necesarios en la variable "espacio y se utiliza espacio[:-2]
# para ir borrando los necesarios en cada paso.

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
