package main

import (
	"fmt"
	"strings"
)

func escalera(n int) {
    if n < 0 {
        n = n * -1
        texto := "|_"
        for n > 0 {
            println(texto)
            texto = "  " + texto
            n = n - 1
        }
    } else if n > 0 {
        espacio := "  "
        n -= 1
        fmt.Println((strings.Repeat(espacio, n + 1)) + "_")
        for n > 0 {
            resultado := strings.Repeat(espacio, n) + "_|"
            fmt.Println(resultado)
            n = n -1
        }
    } else {
        fmt.Println("__")
    }
}

func main() {
    escalera(-4)
}