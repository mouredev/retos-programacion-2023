 package main

import (
	"fmt"
	"log"

	"github.com/nsf/termbox-go"
)

type KonamiCode interface {
	Get() []rune
	Size() int
}

type KeyboardReader interface {
	ReadKeys() []rune
	IsKonamiCode(keys []rune) bool
	Notify(find bool) string
}

type Code struct{}

func (c *Code) Get() []rune {
	return []rune{38, 38, 40, 40, 37, 39, 37, 39, 66, 65}
}

func (c *Code) Size() int {
	return len(c.Get())
}

type Keyboard struct {
	KonamiCode KonamiCode
}

func NewKeyboard(konamiCode KonamiCode) *Keyboard {
	return &Keyboard{KonamiCode: konamiCode}
}

func (kb *Keyboard) ReadKeys() []rune {
	var inputUser []rune
	err := termbox.Init()
	if err != nil {
		log.Fatal(err)
	}
	defer termbox.Close()

	fmt.Println("You need more lives, enter the magic command: ")

loop:
	for {
		switch ev := termbox.PollEvent(); ev.Type {
		case termbox.EventKey:
			termbox.Sync()
			inputUser = append(inputUser, GetKeyCode(ev))
			fmt.Println(inputUser)
			if len(inputUser) == kb.KonamiCode.Size() {
				break loop
			}
		}
	}
	return inputUser
}

func (kb *Keyboard) IsKonamiCode(keys []rune) bool {
	for k := range keys {
		if keys[k] != kb.KonamiCode.Get()[k] {
			return false
		}
	}
	return true
}

func (kb *Keyboard) Notify(find bool) string {
	var option string
	if find {
		fmt.Println("Congratulations! You obtained 30 lives with the correct Konami code.")
		option = "N"
	} else {
		fmt.Println("Command wrong. Do you want to try again? (Y/N)")
		fmt.Scanf("%s", &option)
	}
	return option
}

func GetKeyCode(ev termbox.Event) rune {
	switch ev.Key {
	case termbox.KeyArrowUp:
		return 38
	case termbox.KeyArrowDown:
		return 40
	case termbox.KeyArrowLeft:
		return 37
	case termbox.KeyArrowRight:
		return 39
	default:
		return ev.Ch
	}
}

func main() {
	var option string
	konamiCode := &Code{}
	keyboard := NewKeyboard(konamiCode)

	for option != "N" {
		keys := keyboard.ReadKeys()
		isCode := keyboard.IsKonamiCode(keys)
		option = keyboard.Notify(isCode)
	}
}
