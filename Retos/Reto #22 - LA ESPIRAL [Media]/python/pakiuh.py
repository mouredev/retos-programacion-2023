"""
 * Crea una función que dibuje una espiral como la del ejemplo.
 * - Únicamente se indica de forma dinámica el tamaño del lado.
 * - Símbolos permitidos: ═ ║ ╗ ╔ ╝ ╚
 *
 * Ejemplo espiral de lado 5 (5 filas y 5 columnas):
 * ════╗
 * ╔══╗║
 * ║╔╗║║
 * ║╚═╝║
 * ╚═══╝
"""

n = int(input("Introduce el tamaño del lado: "))
antes = 0
durante = 0
despues = 0
mitad = n//2
if n%2 == 0:
    print("═"*(n)+"╗")
    for i in range(mitad-1):
        antes = i
        durante =(n-2)-(2*i)
        despues = i+1
        if antes < 0:
            antes = 0
        if durante < 0:
            durante = 0
        if despues < 0:
            despues = 0
        #print(i,n)    
        print("║"*antes,
        "╔",
        "═"*durante,
        "╗",
        "║"*despues,
        sep="")

    for i in range(1,mitad+1):
        antes = mitad-i
        durante =(2*i-1)
        despues = mitad-i
        if antes < 0:
            antes = 0
        if durante < 0:
            durante = 0
        if despues < 0:
            despues = 0
        #print(i,n)    
        print("║"*antes,
        "╚",
        "═"*durante,
        "╝",
        "║"*despues,
        sep="")

if n%2 !=0:
    print("═"*(n-1)+"╗")
    for i in range(mitad):
        antes = i
        durante =(n-3)-(2*i)
        despues = i+1
        if antes < 0:
            antes = 0
        if durante < 0:
            durante = 0
        if despues < 0:
            despues = 0
        #print(i,n)    
        print("║"*antes,
        "╔",
        "═"*durante,
        "╗",
        "║"*despues,
        sep="")

    for i in range(1,mitad+1):
        antes = mitad-i
        durante =(2*i-1)
        despues = mitad-i
        if antes < 0:
            antes = 0
        if durante < 0:
            durante = 0
        if despues < 0:
            despues = 0
        #print(i,n)    
        print("║"*antes,
        "╚",
        "═"*durante,
        "╝",
        "║"*despues,
        sep="")
"""
for i in range(n-1): # Imprime la primera fila de lado n
    print("═", end="")

print("╗")
#Imprimimos la 2ª fila
print("╔", end="")
for i in (range(1, n-2)):
    print("═", end="")
print("╗","║", sep="")

#Imprimimos la 3ª fila
print("╚", end="")
for i in (range(1, n-2)):
    print("═", end="")
print("╝","║", sep="")

#Imprimimos la última fila
print("╚═", end="")
for i in range(2, n-1):
    print("═", end="")
print("╝")

for i in range(n):
    for j in range (n-1): 
        print("═"*(i)+"╗"+"║\n"*(j),end="")
    #print("╗","║"*, sep="")

for i in range(n-1): # Imprime la última columna de lado n
    print(" " * (n-1), "║", sep="")

print(" " * (n-2), "╝")

for i in range(n-2):
    print("═", end="")

print("╝")
"""