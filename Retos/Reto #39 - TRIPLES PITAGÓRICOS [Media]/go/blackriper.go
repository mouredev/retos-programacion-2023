package main

import (
	"fmt"
	"math"
)

// definir metodos de trabajo
type Pythagorean interface {
	ReadLimit()
	FindPythagoranNumbers()
	//PrintNumbers()
}

// implementar metodos
type NumberPy struct {
	Pyth  [][]int
	Limit int
}

// leer numero limite para buscar pitagoricos
func (n *NumberPy) ReadLimit() {
	fmt.Println("Enter a number to find Pythagorean numbers")
	fmt.Scanf("%d", &n.Limit)
}

// buscar numeros pitagoricos
func (n *NumberPy) FindPythagoranNumbers() {
	var (
		num int = 1
		nu  int = 1
	)
	for {
		py := IsPythagoran(num, num+1, num+2)
		if len(py) > 0 {
			for {
				if py[0]*nu <= n.Limit && py[1]*nu <= n.Limit && py[2]*nu <= n.Limit {
					npy := IsPythagoran(py[0]*nu, py[1]*nu, py[2]*nu)
					n.Pyth = append(n.Pyth, npy)
				} else {
					break
				}
				nu++
			}
			break
		}
		num++
	}
	fmt.Println(n.Pyth)
}

func IsPythagoran(num1, num2, num3 int) []int {
	var p []int
	n1 := math.Pow(float64(num1), 2)
	n2 := math.Pow(float64(num2), 2)
	n3 := math.Pow(float64(num3), 2)

	if (n1 + n2) == n3 {
		p = []int{num1, num2, num3}
	}
	return p
}

func main() {
	var pyth Pythagorean = &NumberPy{}
	pyth.ReadLimit()
	pyth.FindPythagoranNumbers()
}
