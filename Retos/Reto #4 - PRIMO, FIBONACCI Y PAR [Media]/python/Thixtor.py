# Definimos funciones para cada condicion

def esPar(num):
    """Indica si un numero dado es par"""
    if num % 2 == 0:
        return True
    else:
        return False

def esPrimo(num):
    """Indica si un numero es primo"""
    if num == 0 or num == 1:
        return False
    else:
        for n in range(2, num): 
            if (num % n) == 0:
                return False
    return True
    

def esFibo(num):
    """Indica si un numero es fibonacci"""
    n = 0
    n1 = 1 # Numero n-1
    n2 = 0 # Numero n-2
    
    while n < num:
        n = n1 + n2
        n1 = n2
        n2 = n
    
    if n == num:
        return True
    else:
        return False

# Definimos la funcion que verificara el numero dado

def verificar_num(num):

    num_cond = "El " + str(num)
    
    if esPrimo(num):
        num_cond += " es primo,"
    else:
        num_cond += " no es primo,"

    if esFibo(num):
        num_cond += " fibonacci y"
    else:
        num_cond += " no es fibonacci y"

    if esPar(num):
        num_cond += " es par."
    else:
        num_cond += " no es par."
    
    print(num_cond)
    
# Ejecutamos la funcion solicitando un numero.

verificar_num(int(input("Que numero desea verificar? ")))
