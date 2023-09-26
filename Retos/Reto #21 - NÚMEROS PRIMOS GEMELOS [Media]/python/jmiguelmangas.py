"""/*
 * Crea un programa que encuentre y muestre todos los pares de números primos
 * gemelos en un rango concreto.
 * El programa recibirá el rango máximo como número entero positivo.
 * 
 * - Un par de números primos se considera gemelo si la diferencia entre
 *   ellos es exactamente 2. Por ejemplo (3, 5), (11, 13)
 *
 * - Ejemplo: Rango 14
 *   (3, 5), (5, 7), (11, 13)
 */"""

def get_range():
    try:
        return int(input("Numero maximo: "))
    except ValueError:
        print("Introduce un numero entero positivo")
        
def check_prime(rango):
    lista =[]
    flag = True
    for i in range(2,rango):
        num = i
        for y in range(2, num):
            if (num % y) == 0:
                flag = False
                break 
        if flag != False:
            lista.append(num)
            
        flag = True
    return lista
def check_prime_twins(lista):
    tupla_twins = ()
    lista_tupla_twins = []
    for i in range(len(lista)):
        if i < len(lista) - 1:
            if (lista[i+1]) - (lista[i]) == 2:
                tupla_twins = (lista[i],lista[i+1])
                lista_tupla_twins.append(tupla_twins)
    return lista_tupla_twins
def main():
    rango = get_range()
    lista = check_prime(rango)
    print(f"Los primos gemelos del rango {rango} son: {str(check_prime_twins(lista))}")
if __name__ == "__main__":
    main()