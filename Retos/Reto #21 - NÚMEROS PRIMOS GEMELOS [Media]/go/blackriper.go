package main

import "fmt"

// funcion para saber si un numero es primo de manera recursiva
func isPrimeNumber(num int, n int) bool {
	if n >= num {
		return true
	} else if num%n != 0 {
		return isPrimeNumber(num, n+1)
	} else {
		return false
	}
}

// Estructuras de datos para mejor control
type twinNumbers interface {
	readData()
	printTwinNumbers()
}

type Data struct {
	Number int
}

// leer entrada del usuario
func (d *Data) readData() {
	fmt.Println("Introduce un numero:")
	fmt.Scanf("%d", &d.Number)
}

// imprimir numeros gemelos si el numero es primo restarlo al anterior y ver si la diferencia es de 2
func (d *Data) printTwinNumbers() {
	var before int
	for i := 1; i < d.Number; i++ {
		if isPrimeNumber(i, 2) {
			dif := i - before
			if dif == 2 {
				fmt.Printf("(%v,%v)", before, i)
			}
			before = i
		}

	}

}

func main() {
	var twins twinNumbers = &Data{}
	twins.readData()
	fmt.Println("Sus numeros primos gemelos")
	twins.printTwinNumbers()
}
