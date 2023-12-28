package main

import (
	"fmt"
	"log"
	"os"
)

/*Metodos de trabajo*/
type File interface {
	ReadData()
}

/*implementacion de metodos de la interface*/
const fileName string = "text.txt"

type Content struct {
	Text string
}

// leer datos del usuario
func (c *Content) ReadData() {
	var option string

	switch {
	case ExistFile(fileName) == true:
		fmt.Println("existing file detected, do you want to continue writing y/n")
		fmt.Scanf("%s", &option)
		if option == "y" {
			prevText := ReadFile()
			c.Text = prevText
			WhenTxt(&c.Text, true)
		}
		WhenTxt(&c.Text, false)

	case ExistFile(fileName) == false:
		WhenTxt(&c.Text, false)
	}

	WriteData(c.Text)

}

/*Metodos auxiliares*/
// leer nuevo string
func WhenTxt(text *string, exists bool) {
	var aux string
	fmt.Println("enter the text to write and press enter to write on a new line press [E] Exit")
	for {
		if exists == true {
			aux = *text
			fmt.Printf("Existing text\n %v", aux)
		}
		fmt.Scanf("%s", &aux)
		if aux == "E" {
			break
		}
		*text = *text + (aux + "\n")
		aux = ""

	}
}

// escribir en fichero
func WriteData(text string) {
	data := []byte(text)
	if err := os.WriteFile(fileName, data, 0644); err != nil {
		log.Fatal(err)
	}
	fmt.Println("File writing correcty!")
}

// leer fichero
func ReadFile() string {
	file, err := os.ReadFile(fileName)
	if err != nil {
		log.Fatal(err)
	}
	return string(file)
}

// comprobar si existe un fichero
func ExistFile(path string) bool {
	if _, err := os.Stat(path); err != nil {
		return false
	}
	return true
}

func main() {
	var file File = &Content{}
	file.ReadData()
}
