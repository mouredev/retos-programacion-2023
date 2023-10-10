package main

import (
	"fmt"
	"strings"
)

// metodos de trabajo
type Leet interface {
	ReadText()
	TrasformTexttoLeet() string
}

// implementamos metodos
type Hacker struct {
	Text string
}

func (h *Hacker) ReadText() {
	var input string
	fmt.Println("Introduce a text for trasformate a leet")
	fmt.Scanf("%s", &input)
	h.Text = strings.ToUpper(input)
}

func (h *Hacker) TrasformTexttoLeet() string {
	leet := map[string]string{"A": "4", "B": "I3", "C": "[", "D": ")", "E": "3", "F": "|=", "G": "&", "H": "#", "I": "1", "J": ",_|", "K": ">|", "L": "1", "M": "JVI", "N": "^/", "O": "0", "P": "|*", "Q": "(_,)", "R": "I2", "S": "5", "T": "7", "U": "(_)", "V": "|/", "W": "(n)", "X": "><", "Y": "j", "Z": "2"}
	var hackerText string
	for _, let := range h.Text {
		hackerText = hackerText + leet[string(let)]
	}

	return hackerText
}

func main() {
	var hacker Leet = &Hacker{}
	hacker.ReadText()
	fmt.Printf("text hacking is %v", hacker.TrasformTexttoLeet())
}
