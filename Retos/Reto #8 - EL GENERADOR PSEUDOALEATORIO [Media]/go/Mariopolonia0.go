package main

import (
    "fmt"
    "time"
)

func main() {
    var semilla, hasta, numero, numeroDos, contador int

    // time.Now().Unix() devuelve el tiempo actual en segundos desde la Epoch (01/01/1970)
    semilla = int(time.Now().Unix() % 100)
    hasta = 0
    numero = 0
    numeroDos = 0
    contador = 0

    fmt.Println("¿Cuántos números aleatorios se imprimirán?")
    fmt.Scanln(&hasta)

    for contador < hasta {
        numero = (5*semilla + 7) % 8
        numeroDos = numero * 8

        if numeroDos > 0 && numeroDos < 100 {
            fmt.Println(numeroDos)
            contador = contador + 1
        }

        semilla = numero
    }
}
