package main

import "fmt"

type PrimeChecker interface {
	IsPrime(n int) bool
}

type TwinPrimeFinder interface {
	FindTwinPrimes(maxRange int) [][2]int
}

type SimplePrimeChecker struct{}

func (pc *SimplePrimeChecker) IsPrime(n int) bool {
	if n <= 1 {
		return false
	}
	for i := 2; i*i <= n; i++ {
		if n%i == 0 {
			return false
		}
	}
	return true
}

type SimpleTwinPrimeFinder struct {
	primeChecker PrimeChecker
}

func NewSimpleTwinPrimeFinder(pc PrimeChecker) *SimpleTwinPrimeFinder {
	return &SimpleTwinPrimeFinder{primeChecker: pc}
}

func (tf *SimpleTwinPrimeFinder) FindTwinPrimes(maxRange int) [][2]int {
	var twinPrimes [][2]int
	for i := 2; i <= maxRange-2; i++ {
		if tf.primeChecker.IsPrime(i) && tf.primeChecker.IsPrime(i+2) {
			twinPrimes = append(twinPrimes, [2]int{i, i + 2})
		}
	}
	return twinPrimes
}

func main() {
	primeChecker := &SimplePrimeChecker{}
	twinPrimeFinder := NewSimpleTwinPrimeFinder(primeChecker)

	maxRange := 14
	twinPrimes := twinPrimeFinder.FindTwinPrimes(maxRange)

	fmt.Printf("Twin primes in range %d:\n", maxRange)
	for _, pair := range twinPrimes {
		fmt.Printf("(%d, %d)\t", pair[0], pair[1])
	}
}
