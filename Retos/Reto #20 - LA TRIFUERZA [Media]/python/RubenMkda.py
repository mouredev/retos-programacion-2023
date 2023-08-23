def trifuerza(rows):

    for n in range(1, rows*2+1):

        formule = 2*n-1
        formule2 = rows*2
        spaces = rows*2-n

        # Draw top triangle
        if n <= rows:
            print(" "*spaces + "*"*(formule))

        # Draw bottom triangles
        if n > rows:
            print(" "*spaces + "*"*( formule - formule2 ), end="")
            print(' '*(formule2-n+spaces+1), end='')
            print("*"*(formule-formule2))
        
if __name__ == "__main__":

    while True:

        rows = input("Por favor ingrese el numero de filas: ")
        if rows.isdigit():
            rows = int(rows)
            print("Trifuerza: ", rows)
            trifuerza(rows)
            break
    
        else:
            print("El numero debe ser un número entero. Intente de nuevo.")