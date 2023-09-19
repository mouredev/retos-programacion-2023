#!/usr/bin/awk -f

BEGIN {
    # Punto 1: Hola, mundo!
    print "Hola, mundo!"

    # Punto 2: Crea una variable de texto o string
    miTexto = "¡Hola desde AWK!"

    # Punto 3: Crea una variable de número entero
    miEntero = 42

    # Punto 4: Crea una variable de número con decimales
    miDecimal = 3.14

    # Punto 5: Crea una variable de tipo booleano
    miBooleano = 1  # 1 representa verdadero, 0 representa falso

    # Punto 6: Crea una constante (no es directamente soportado en AWK)

    # Punto 7: Usa un if, else if y else
    if (miEntero > 50) {
        print "El número es mayor que 50"
    } else if (miEntero < 50) {
        print "El número es menor que 50"
    } else {
        print "El número es igual a 50"
    }

    # Punto 8: Crea un Array
    split("1 2 3 4 5", miArray)

    # Punto 9: Crea una lista (Array en AWK)
    miLista[1] = "Manzana"
    miLista[2] = "Banana"
    miLista[3] = "Naranja"

    # Punto 10: Crea una tupla (no aplicable en AWK)

    # Punto 11: Crea un set (no aplicable en AWK)

    # Punto 12: Crea un diccionario (no es directamente soportado en AWK)

    # Punto 13: Usa un ciclo for
    for (i in miArray) {
        print miArray[i]
    }

    # Punto 14: Usa un ciclo foreach (no es soportado directamente en AWK)

    # Punto 15: Usa un ciclo while
    contador = 0
    while (contador < 3) {
        print "Contador: " contador
        contador++
    }

    # Punto 16: Crea una función sin parámetros que no retorne nada (no es aplicable en AWK)

    # Punto 17: Crea una función con parámetros que no retorne nada (no es aplicable en AWK)

    # Punto 18: Crea una función con parámetros que retorne valor (no es aplicable en AWK)

    # Punto 19: Crea una clase (no es directamente soportado en AWK)

    # Punto 20: Muestra control de excepciones (no es soportado en AWK)
}
