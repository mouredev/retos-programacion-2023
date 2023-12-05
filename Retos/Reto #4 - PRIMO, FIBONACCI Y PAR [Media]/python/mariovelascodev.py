def what_is_it(number):
    #Variables
    result = "{number} ".format(number=number)
    fibonacci = [1, 1]
    count = 1

    try:
    
        #Comprobamos si el número es primo
        for index in range(2, number):
            if number % index == 0:
                result += "no es primo, "
                break
        else:
            result += "es primo, "

        #Comprobamos si es fibonacci
        #Sacamos la secuencia de Fibonacci del rango introducido por parametro y añadimos a la lista
        while count < number:
            next_number = fibonacci[count] + fibonacci[count - 1]
            fibonacci.append(next_number)

            #Si el último número es igual al introducido por parámetros paramos el bucle
            if next_number == number:
                break
            
            count+=1

        #Comprobamos si el último número es igual al introducido por parámetros
        if fibonacci[len(fibonacci)-1] == number:
            result += "es fibonacci"
        else:
            result += "no es fibonacci"

        #Comprobamos si el número es par
        if number % 2 == 0:
            result += " y es par"
        else:
            result += " y es impar"
        
        return result
    except TypeError:
        print("Debes introducir un número")

print(what_is_it(2))
print(what_is_it(7))
print(what_is_it(4))
print(what_is_it(0))
print(what_is_it(98))
