# Reto #16: LA ESCALERA
# Crea una función que dibuje una escalera según su número de escalones.
# - Si el número es positivo, será ascendente de izquiera a derecha.
# - Si el número es negativo, será descendente de izquiera a derecha.
# - Si el número es cero, se dibujarán dos guiones bajos (__).

# Autor: Clark - @ClarkCodes
# Fecha de Resolución: 18/04/2023

# Atributos Globales
escalonAscendente = "_|"
escalonDescendente = "|_"

# Función
def escalera():
    print( "\n*** Reto #16: La Escalera - By ClarkCodes ***" )

    while True:
        try:
            spacesCant = -1
            print( "\nPara salir del programa ingrese la letra 'q'." )
            userInput = input( "Ingrese el número de escalones que desea en la escalera: " )

            if( userInput == 'q' or userInput == 'Q' ): #Condición de Salida del Bucle y Terminación del Script
                print( "\nMuchas gracias por ejecutar este Script, hasta la próxima... Happy Coding!, bye :D\nClark." )
                break

            cantEscalones : int = int( userInput )
            stairs = abs( cantEscalones )
            print( "Esta es su escalera:\n" )

            if ( cantEscalones == 0 ):
                print( "__" )

            elif ( cantEscalones < 0 ):
                print( "_" )

                # Se dibuja la Escalera Descendente
                for stairNumber in range( stairs ): # spacesCant empieza en -1
                    spacesCant += 2 # Con el incremento en cada iteración siempre va a ser impar, lo cual se busca para los espacios cuando es descendente según el algoritmo establecido en base a la morfología de la escalera

                    for spaces in range( spacesCant ): # Se imprimen los espacios en blanco sin salto de línea necesarios hasta el próximo escalón.
                        print( " ", end = "" )

                    print( escalonDescendente )

            else: #cantEscalones > 0
                spacesCant = ( cantEscalones * 2 ) # Se posiciona el cursor para imprimir el primer caracter '_' necesario, cada escalon mide 2 caracteres, por ello se multiplica la cantidad de escalones x2

                for spaces in range( spacesCant ): # Se imprimen los espacios en blanco sin salto de línea necesarios igual a la cantidad de escalones para imprimir el caracter inicial '_' necesario
                    print( " ", end = "" )
                
                print( "_" )
                
                # Se dibuja la Escalera Ascendente
                for stairNumber in range( stairs ): 
                    spacesCant -= 2 # Con el decremento de la longitud del escalón en cada iteración siempre va a ser par, lo cual se busca

                    for spaces in range( spacesCant ): # Se imprimen los espacios en blanco sin salto de línea necesarios hasta el próximo escalón
                        print( " ", end = "" )

                    print( escalonAscendente )

        except ValueError:
            print("\n* Valor No Válido *:\nLa cantidad de escalones solo puede ser un número entero, ingréselo nuevamente.\n")
        except:
            print("Oops... algo más no ha salido bien, revisar por favor.")


# Llamada a la Función
escalera()
