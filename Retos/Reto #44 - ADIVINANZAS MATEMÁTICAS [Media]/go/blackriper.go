package main

import (
	"fmt"
	"math/rand"
	"time"
)

/* definir metodos de trabajo*/
type MathematicalRiddles interface {
	PlayRiddles()
}

// implementar metodos de interface
type RiddlesGame struct {
	Sucess int
}

func (r *RiddlesGame) PlayRiddles() {
	var (
		res      int
		answer   int
		question int = 1
	)

	for {
		fmt.Println("***** MathematicalRiddles *****")
		x, signal, y := GeneratorRiddles(question)
		GetResultRiddle(x, y, &res, signal)
		fmt.Printf("Write the correct answer to the following operation %v %v %v = ", x, signal, y)
		fmt.Scanf("%d", &answer)
		time.Sleep(3 * time.Second)
		if answer != res {
			fmt.Println("you lost game  !!")
			fmt.Printf("you solved %v operations correctly ", r.Sucess)
			break
		} else if answer == res {
			question++
			r.Sucess++
		}

	}

}

/* funciones auxiliares*/
func GeneratorRiddles(question int) (x int, signal string, y int) {

	signals := []string{"+", "-", "*", "/"}

	switch {
	case question >= 1 && question <= 5:
		x = rand.Intn(9)
		y = rand.Intn(9)

	case question >= 6 && question <= 10:
		x = rand.Intn(99)
		y = rand.Intn(9)

	case question >= 11 && question <= 15:
		x = rand.Intn(99)
		y = rand.Intn(99)

	case question >= 16 && question <= 20:
		x = rand.Intn(999)
		y = rand.Intn(99)
	}
	signal = signals[rand.Intn(len(signals))]

	return x, signal, y
}

func GetResultRiddle(x, y int, res *int, signal string) {
	switch signal {
	case "+":
		*res = x + y
	case "-":
		*res = x - y
	case "*":
		*res = x * y
	case "/":
		*res = x / y
	}
}

func main() {
	var game MathematicalRiddles = &RiddlesGame{}
	game.PlayRiddles()
}
