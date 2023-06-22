package main

/*
  1.- go mod init  nombre_del_modulo
  2.- go get github.com/nsf/termbox-go libreria para escuhar la entrada del teclado
  3.- happy coding
*/
import (
	"fmt"

	"github.com/nsf/termbox-go"
)

// definir tipos de datos e interface
type Konami interface {
	Get() []rune
	Size() int
}

type Keyboard interface {
	ReadKeys() []rune
	IsKonamiCode(keys []rune) bool
	Notification(find bool) string
}

type Code struct{}

// obtener codigo Konami en formato keycode
func (c *Code) Get() []rune {
	return []rune{38, 38, 40, 40, 37, 39, 37, 39, 66, 65}

}

// obtener el tamaño del arreglo
func (c *Code) Size() int {
	return len(c.Get())
}

type FindCode struct {
	Konami
}

// Leer entrada de teclado y deterse cuando este tenga diez caracteres para evaluar code
func (f *FindCode) ReadKeys() []rune {
	var inputUser []rune
	err := termbox.Init()
	if err != nil {
		panic(err)
	}
	defer termbox.Close()

	fmt.Println("You need more lifes introduce a magic command: ")

loop:
	for {
		switch ev := termbox.PollEvent(); ev.Type {
		case termbox.EventKey:
			termbox.Sync()
			inputUser = append(inputUser, GetKeyCode(&ev))
			fmt.Println(inputUser)
			if len(inputUser) == f.Konami.Size() {
				break loop
			}
		}
	}
	return inputUser

}

// comparar slices de rune para saber si hay un konami code
func (f *FindCode) IsKonamiCode(keys []rune) bool {
	for k := range keys {
		if keys[k] != f.Konami.Get()[k] {
			return false
		}
	}
	return true
}

// funcion para notificar el resultado ha sido correcto o no en caso de no volver a intentar
func (f *FindCode) Notification(find bool) string {
	var option string
	if find {
		fmt.Println("congratulations  you obtained 30 lives correct konami code commad ")
		option = "N"
	} else {
		fmt.Println("Command wrong do you want try again Y/N ")
		fmt.Scanf("%s", &option)
	}
	return option
}

// funcion para obtener key code de arrows
func GetKeyCode(ev *termbox.Event) rune {
	var key rune
	switch ev.Key {
	case termbox.KeyArrowUp:
		key = 38
	case termbox.KeyArrowDown:
		key = 40
	case termbox.KeyArrowLeft:
		key = 37
	case termbox.KeyArrowRight:
		key = 39
	default:
		key = ev.Ch
	}
	return key
}

func main() {
	var option string
	konami := Code{}
	var program Keyboard = &FindCode{Konami: &konami}
	for option != "N" {
		keys := program.ReadKeys()
		isCode := program.IsKonamiCode(keys)
		option = program.Notification(isCode)
	}
}
