package main

import (
	"fmt"
	"time"
)

// definir metodos de trabajo
type Random interface {
	GenerateNumber()
	ShowNumber()
}

// implementar  metodos de trabajo
type Generator struct {
	Num int
}

func (g *Generator) GenerateNumber() {
	seed := int(time.Now().Unix() % 100)
	num := (5*seed + 7) % 8
	num2 := num * 8
	if num2 >= 0 && num2 <= 100 {
		g.Num = num2
	}

}

func (g Generator) ShowNumber() {
	fmt.Println(g.Num)
}

/*
func main() {
	var rand Random = &Generator{}
	rand.GenerateNumber()
	rand.ShowNumber()
}*/
