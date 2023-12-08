def encontrar_caracter_infiltrado(cad1, cad2):
    infiltrados = []
    if len(cad1) != len(cad2):
        return infiltrados  # Retorna una lista vacía si las cadenas no tienen la misma longitud
    for i in range(len(cad1)):
        if cad1[i] != cad2[i]:
            infiltrados.append(cad1[i])
    return infiltrados 

print("Pusho.Dev")
print("https://puschoft.blogspot.com")

# Solicitar al usuario ingresar textos para identificar
cad1 = input("Ingrese la primera cadena: ")
cad2 = input("Ingrese la segunda cadena: ")

# Mostrar los Resultados de este ejercicio
resp = encontrar_caracter_infiltrado(cad1, cad2)
print("Los caracteres infiltrados son:", resp)
print("Muchas Gracias por participar ...")