package main

import (
	"fmt"
)

// definir funciones para trabajar
type KeyboardT9 interface {
	DecodeT9() string
}

// tipo de dato a recibir
type Block struct {
	T9 string
}

// funcion para decodificar los numeros
func (b *Block) DecodeT9() string {
	var before string
	var text string
	var count int

	for idx, lett := range b.T9 {

		car := string(lett)

		if car == "-" {
			text = text + NumberToText(before, count)
			count = 0
		} else {
			if before == car {
				count++
			} else {
				count = 1
			}
			before = car
			if idx == len(b.T9)-1 {
				text = text + NumberToText(before, count)
				break
			}
		}
	}

	return text
}

// funcion auxilar para obtener las letras
func NumberToText(num string, count int) string {
	var letter string
	switch {
	case num == "0":
		letter = " "
	case num == "2" && count == 1:
		letter = "a"
	case num == "2" && count == 2:
		letter = "b"
	case num == "2" && count == 3:
		letter = "c"
	case num == "3" && count == 1:
		letter = "d"
	case num == "3" && count == 2:
		letter = "e"
	case num == "3" && count == 3:
		letter = "f"
	case num == "4" && count == 1:
		letter = "g"
	case num == "4" && count == 2:
		letter = "h"
	case num == "4" && count == 3:
		letter = "i"
	case num == "5" && count == 1:
		letter = "j"
	case num == "5" && count == 2:
		letter = "k"
	case num == "5" && count == 3:
		letter = "l"
	case num == "6" && count == 1:
		letter = "m"
	case num == "6" && count == 2:
		letter = "n"
	case num == "6" && count == 3:
		letter = "o"
	case num == "6" && count == 4:
		letter = "ñ"
	case num == "7" && count == 1:
		letter = "p"
	case num == "7" && count == 2:
		letter = "q"
	case num == "7" && count == 3:
		letter = "r"
	case num == "7" && count == 4:
		letter = "s"
	case num == "8" && count == 1:
		letter = "t"
	case num == "8" && count == 2:
		letter = "u"
	case num == "8" && count == 3:
		letter = "v"
	case num == "9" && count == 1:
		letter = "w"
	case num == "9" && count == 2:
		letter = "x"
	case num == "9" && count == 3:
		letter = "y"
	case num == "9" && count == 4:
		letter = "z"
	}
	return letter
}

func main() {
	// salida mouredev
	//entry := "6-666-88-777-33-3-33-888"
	//salida hola soy goku
	entry := "44-666-555-2-0-7777-666-999-0-4-666-55-88"
	var key KeyboardT9 = &Block{T9: entry}
	text := key.DecodeT9()
	fmt.Printf("Entrada: %v \n", entry)
	fmt.Printf("Salida: %v \n", text)

}
