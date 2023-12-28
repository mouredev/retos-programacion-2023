package main

import (
	"fmt"
	"time"
)

// declarar tipos de datos y logica a utilizar

type CounterDown interface {
	ReadData()
	StartCounterDown()
}

type Down struct {
	Number  int
	Seconds int
}

// implementar metodos de la interface
func (d *Down) ReadData() {
	for d.Number <= 0 || d.Seconds <= 0 {
		fmt.Println("enter a number for the counter")
		fmt.Scanf("%d", &d.Number)

		fmt.Println("enters a period of time to decrease")
		fmt.Scanf("%d", &d.Seconds)

		if d.Number < 0 || d.Seconds < 0 {
			fmt.Println("only positive numbers are allowed")
		}
	}

}

func (d *Down) StartCounterDown() {
	fmt.Println(d.Number)
	for d.Number > 0 {
		time.Sleep(time.Duration(d.Seconds) * time.Second)
		d.Number--
		fmt.Println(d.Number)
	}
}

func main() {
	var counterdown CounterDown = &Down{}
	counterdown.ReadData()
	counterdown.StartCounterDown()
}
