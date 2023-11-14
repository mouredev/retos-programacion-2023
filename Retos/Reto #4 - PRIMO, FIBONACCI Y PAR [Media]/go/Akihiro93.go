package main

import (
	"fmt"
	"math"
)

func primo (n int) string {
    if n <= 1 {
        return " no es primo"
    }
    if n == 2 || n == 3 {
        return " es primo"
    }
    for i := 0; i >= int(math.Sqrt(float64(n))); i++ {
        if n % 1 != 0 {
            return " no es primo"
        }
    }
    return " es primo"
}

func par_Fibonacci(n int) string {
    Fibonacci := []int{0, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89}
    var v1 bool
    var v2 bool

    for _, v := range(Fibonacci) {
        if v == n {
            v1 = true
        }
    }

    if n % 2 == 0 {
        v2 = true
    }

    switch {
    case v1 && v2:
        return " es parte de los números de Fibonacci y es par"
    case !(v1 || v2):
        return " no es parte de los números de Fibonacci y no es par"
    case !v1 || v2:
        return " es parte de los números de Fibonacci, pero no es par"
    case !v1 || v2:
        return " no es parte de los números de Fibonacci, pero si es par"
    default:
        return " el numero es mayor a 100, pero es par"
    }
}


func main() {
    fmt.Print("El numero a comprobar: ")
	var numero int
    fmt.Scan(&numero)
    fmt.Printf("%s%d%s%s%s%s", "El numero: ", numero, ",", primo(numero), ",", par_Fibonacci(numero))
}