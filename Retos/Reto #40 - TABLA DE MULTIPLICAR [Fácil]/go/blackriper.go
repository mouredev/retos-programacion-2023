package main

import "fmt"

// definir metodos de trabajos
type Table interface {
	ReadNumber()
	PrintTable()
}

// implementar metodos de trabajo
type Multiplication struct {
	Number int
}

func (m *Multiplication) ReadNumber() {
	fmt.Println("What multiplication table do you want to view?")
	fmt.Scanf("%d", &m.Number)
}

func (m *Multiplication) PrintTable() {
	fmt.Printf("Multiplication table  %v \n", m.Number)
	for n := 1; n <= 10; n++ {
		fmt.Printf("%v x %v = %v \n", m.Number, n, (m.Number * n))
	}
}

func main() {
	var multab Table = &Multiplication{}
	multab.ReadNumber()
	multab.PrintTable()
}
