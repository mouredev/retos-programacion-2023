package main

import (
	"fmt"
	"os"
	"strings"
)

var alphabet []string = []string{"A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"}

// definir metodos  de la interface
func ReadData(message string) (int, string) {
	var key int
	var text string
	fmt.Println("Introduce  extension key: ")
	fmt.Scanf("%d", &key)
	fmt.Println(message)
	fmt.Scanf("%s", &text)
	return key, text
}
func Cipher(key int, text string) string {
	mayus := strings.ToUpper(text)
	var cipher string
	for _, word := range mayus {
		for id, letter := range alphabet {
			if string(word) == letter {
				pos := (id + key) % len(alphabet)
				cipher += alphabet[pos]
			}
		}
	}
	return cipher

}

func Plain(key int, cipher string) string {
	mayus := strings.ToUpper(cipher)
	var plain string
	for _, word := range mayus {
		for id, letter := range alphabet {
			if string(word) == letter {
				pos := (id - key) % len(alphabet)
				if pos >= 0 {
					plain += alphabet[pos]
				} else {
					if (pos * -1) <= key {
						plain += alphabet[len(alphabet)-(pos*-1)]
					} else {
						plain += alphabet[pos*-1]
					}
				}
			}
		}
	}
	return plain
}

func menu_options() {
	var option int
	for option != 3 {
		fmt.Println("I am an encryption not a salad")
		fmt.Println("1.-Encryption")
		fmt.Println("2.-Decrypt")
		fmt.Println("3.-Exit")
		fmt.Scanf("%d", &option)
		switch option {
		case 1:
			key, text := ReadData("Introduce text to encrypt: ")
			cipher := Cipher(key, text)
			fmt.Printf("The New text is : %v \n", cipher)
		case 2:
			key, text := ReadData("Introduce text to decrypt: ")
			plain := Plain(key, text)
			fmt.Printf("The Original text is : %v \n", plain)
		case 3:
			os.Exit(0)
		}
	}
}

func main() {
	menu_options()
}
