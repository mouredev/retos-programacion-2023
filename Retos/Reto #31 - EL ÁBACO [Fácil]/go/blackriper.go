package main

import (
	"fmt"
	"strconv"
	"strings"
)

// metodos para trabajar
type Abaco interface {
	DrawAbaco()
	ReadNumber()
	PrintResult()
}

// estructura para implementar metodos
type Data struct {
	Original string
	Number   string
	Aba      []string
}

// leer datos del usuario
func (d *Data) ReadNumber() {
	isvalid := false
	for isvalid == false {
		fmt.Println("Enter a number: ")
		fmt.Scanf("%s", &d.Number)
		d.Original = d.Number
		d.Number = strings.ReplaceAll(d.Number, ".", "")

		if len(d.Number) > 7 {
			fmt.Println("The abacus only accepts numbers with length less than or equal to 7 ")
		} else if len(d.Number) <= 7 {
			isvalid = true
		}
	}
}

// funcion para dibujar abaco
func (d *Data) DrawAbaco() {
	abaco := make([]string, 7)
	diff := 7 - len(d.Number)
	if diff != 0 {
		d := 0
		for d < diff {
			abaco = append(abaco, DrawAccount("0"))
		}
	} else {
		for _, n := range d.Number {
			abaco = append(abaco, DrawAccount(string(n)))
		}
	}
	d.Aba = abaco
}

// funcion para imprimir resultado
func (d *Data) PrintResult() {
	for _, ab := range d.Aba {
		fmt.Println(ab)
	}
	fmt.Printf("Resultado: %v", d.Original)
}

// funcion auxilar para dibujar cuentas
func DrawAccount(num string) string {
	var count string
	n, _ := strconv.Atoi(num)
	switch {
	case n == 0:
		count = "---ooooooooo"
	case n == 9:
		count = "ooooooooo---"
	default:
		count = Draw(n)

	}
	return count
}

// funcion para dibujar cuenta cuando no es 0 o 9
func Draw(n int) string {
	var co string
	for c := 0; c < 9; c++ {
		if c == n {
			co = co + "---"
		}
		co = co + "o"
	}
	return co
}

// implemtacion de interface
func main() {
	var abaco Abaco = &Data{}
	abaco.ReadNumber()
	abaco.DrawAbaco()
	abaco.PrintResult()
}
