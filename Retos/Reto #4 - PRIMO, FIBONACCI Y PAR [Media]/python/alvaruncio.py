def es_primo_fibonnaci_par(number):
    
    mensaje_final = f"{number} "
    
    #Primo
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                mensaje_final += "no es primo, "
                break
        else:
            mensaje_final += "es primo, "
    else:
         mensaje_final += "no es primo, "

    #Fibonnaci
    first_number = 1
    second_number = 1
    fibonnaci = 0
    while fibonnaci < number:
        fibonnaci = first_number + second_number
        first_number = second_number
        second_number = fibonnaci
    if fibonnaci != number:
            mensaje_final += "no es fibonacci y "
    else:
           mensaje_final += "fibonacci y "
    #Par
    
    if number % 2 == 0:
        mensaje_final += "es par."
    else:
        mensaje_final += "es impar."

    print(mensaje_final)

                

print(es_primo_fibonnaci_par(1))
