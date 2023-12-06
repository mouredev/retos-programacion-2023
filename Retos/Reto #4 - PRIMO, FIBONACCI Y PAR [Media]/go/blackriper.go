package main

import "fmt"

// metodos de trabajo
type FactoryTypes interface {
	ReadNumber()
	ShowResult()
}

// implementar metodos
type Number struct {
	Number int
}

func (n *Number) ReadNumber() {
	fmt.Println("Enter a number: ")
	fmt.Scanf("%d", &n.Number)
}
func (n *Number) ShowResult() {
	prime := IsPrimeNumber(n.Number)
	paOrim := IsEvenOrOdd(n.Number)
	fib := IsFib(n.Number)
	fmt.Printf("the number %v %v,%v and %v", n.Number, prime, fib, paOrim)
}

// funciones auxiliares
func IsPrimeNumber(num int) string {
	for n := 2; n < num; n++ {
		if num%n == 0 {
			return " not is prime number"
		}
	}
	return "is prime number"
}

func IsEvenOrOdd(num int) string {
	if num%2 == 0 {
		return "is Even"
	}
	return "is Odd"
}

func IsFib(num int) string {
	for _, fib := range Fibonacci(num) {
		if fib == num {
			return "fibonacci"
		}
	}
	return "not fibonacci"
}

func Fibonacci(n int) []int {
	var (
		c   int
		n1  int
		n2  int = 1
		sum int = 1
		fib []int
	)
	fib = append(fib, n1)
	for c <= n {
		fib = append(fib, sum)
		sum = n1 + n2
		n1 = n2
		n2 = sum
		c++
	}
	fmt.Println(fib)
	return fib
}

func main() {
	var factory FactoryTypes = &Number{}
	factory.ReadNumber()
	factory.ShowResult()
}
