# Escribe un programa que muestre por consola (con un print) los
# números de 1 a 100 (ambos incluidos y con un salto de línea entre
# cada impresión), sustituyendo los siguientes:
# - Múltiplos de 3 por la palabra "fizz".
# - Múltiplos de 5 por la palabra "buzz".
# - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".

#Se crea un bucle que vaya de 1 al 100, agregamos +1 porque sino contaria hasta 99
for i in range (1,100+1):
    #Creamos una condicion para asegurarnos de que i sea multiplo de 3 y 5
    if i % 3 == 0 and i % 5 == 0:
       #si se cumple la condicion de arriba imprime 
       print ("fizzbuzz")
    #Con esta condicion al no cumplirse la de arriba entonces puede que solo sea multiplo de 3
    elif i % 3 == 0 :
        #si se cumple la condicion de arriba imprime 
        print ("fizz")
    #Con esta condicion al no cumplirse la de arriba entonces puede que solo sea multiplo de 5
    elif i % 5 == 0:
         #si se cumple la condicion de arriba imprime 
        print ("buzz")
    #Esta línea imprimirá el valor de la variable "i" si no se cumple ninguna de las condiciones anteriores 
    else: 
        print (i)
    

