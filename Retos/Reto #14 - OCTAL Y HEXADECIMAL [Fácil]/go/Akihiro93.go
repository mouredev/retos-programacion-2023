package main

import (
	"fmt"
	"strconv"
)

func invertirString(s string) string {
	n := len(s)
	invertido := make([]byte, n)
	for i := 0; i < n; i++ {
		invertido[i] = s[n-1-i]
	}
	return string(invertido)
}

func octal(n int) {
	resultado := ""
	d := n
	m := 0
	for d >= 8 {
		m = d % 8
		d = d / 8
		resultado = resultado + strconv.Itoa(m)
	}
	resultado = resultado + strconv.Itoa(d)
	resultado = invertirString(resultado)
	fmt.Println("El numero: ", n, " en octal es: ", resultado)
}

func hexadecimal(n int) {
    hexadecimal_dict := map[int]string {
        10:"A", 11:"B", 12:"C", 13:"D", 14:"E", 15:"F"}
    var resultado string
    d := n
    var m int
    if d >= 16{
        for d >= 16 {
            m = d % 16
            d = d / 16
            if m >= 10 && m < 16 {
                resultado += hexadecimal_dict[m]
            } else {
                resultado += strconv.Itoa(m)
            }
        }
    }
    if d >= 10 && d <= 15 {
        resultado += hexadecimal_dict[d]
    } else {
        resultado += strconv.Itoa(d)
    }
    
    resultado = invertirString(resultado)
    fmt.Println("El numero: ", n, " en hexadecimal es: ", resultado)
}

func main() {
    fmt.Println("El numero a convertir:")
    var numero int
    fmt.Scanln(&numero)
    octal(numero)
    hexadecimal(numero)
}