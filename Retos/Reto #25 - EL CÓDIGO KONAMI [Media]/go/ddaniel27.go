package main

import (
	"fmt"

	"github.com/nsf/termbox-go"
)

func main() {
	var inputUser []rune
	err := termbox.Init()
	if err != nil {
		panic(err)
	}
	defer termbox.Close()

	for {
		switch ev := termbox.PollEvent(); ev.Type {
		case termbox.EventError:
			panic(ev.Err)
		case termbox.EventInterrupt:
			return
		case termbox.EventKey:
			termbox.Sync()
			inputUser = append(inputUser, getKey(ev))
			if checkKonamiCode(inputUser) {
				fmt.Println("Konami Code")
				return
			}
		}
	}
}

func checkKonamiCode(k []rune) bool {
	println(string(k))
	konamiCode := []rune{'↑', '↑', '↓', '↓', '←', '→', '←', '→', 'B', 'A'}
	if len(k) < len(konamiCode) {
		return false
	}
	if len(k) > len(konamiCode) {
		k = k[len(k)-len(konamiCode):]
	}
	for i := 0; i < len(konamiCode); i++ {
		if k[i] != konamiCode[i] {
			return false
		}
	}
	return true
}

func getKey(key termbox.Event) rune {
	switch key.Key {
	case termbox.KeyArrowUp:
		return '↑'
	case termbox.KeyArrowDown:
		return '↓'
	case termbox.KeyArrowLeft:
		return '←'
	case termbox.KeyArrowRight:
		return '→'
	case termbox.KeySpace:
		return ' '
	case termbox.KeyEnter:
		return '\n'
	case termbox.KeyTab:
		return '\t'
	case termbox.KeyBackspace:
		return '\b'
	case termbox.KeyEsc:
		return 27
	default:
		return key.Ch
	}
}
