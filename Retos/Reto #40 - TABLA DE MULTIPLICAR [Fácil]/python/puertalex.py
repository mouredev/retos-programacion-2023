def genera_tabla(numero :int) -> str:
    
    tabla = ""
    i = 1
    
    while i <= 10:
        resultado = numero * i
        tabla += (f"{numero} X {i} = {resultado}\n")
        i += 1
    
    return tabla

while(True):
    print("Introduce un numero entre 1 y 10:")
    try:
        entrada = int(input())
        if entrada >= 1 and entrada <= 10:
            print(genera_tabla(entrada))
            break
        else:
            print("Debes introducir un número entre 1 y 10")
    except Exception as e:
        print("Solo esta permitido introducir números")
        