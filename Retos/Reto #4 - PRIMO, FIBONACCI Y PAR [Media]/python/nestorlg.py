def es_primo(num):
    for i in range(2, num - 1):
        if (es_primo(i) == True):
            if (num % i == 0):
                return False
                
    return True

def es_fibonacci(num):
    num_anterior_dos = 1
    num_anterior_uno = 1
    
    while (num_anterior_dos + num_anterior_uno <= num):
        num_actual       = num_anterior_dos + num_anterior_uno
        
        if (num_actual == num):
            return True
        
        num_anterior_dos = num_anterior_uno
        num_anterior_uno = num_actual
        
    return False
    
def es_par(num):
    return num % 2 == 0

def comprobar_numero(num):
    
    resultado = str(num)
    
    if (es_primo(num) == False):
        resultado += " no"
    
    resultado += " es primo, "
    
    if (es_fibonacci(num) == False):
        resultado += "no es "
        
    resultado += "fibonacci y es "
    
    if (es_par(num) == False):
        resultado += "im"
        
    resultado += "par"
    
    print(resultado)
        
    
comprobar_numero(2)  # Primo, Fibonacci, Par
comprobar_numero(3)  # Primo, Fibonacci, No Par
comprobar_numero(4)  # No Primo, No Fibonacci, Par
comprobar_numero(7)  # Primo, No Fibonacci, No Par
comprobar_numero(8)  # No Primo, Fibonacci, Par
comprobar_numero(9)  # No Primo, No Fibonacci, No Par
