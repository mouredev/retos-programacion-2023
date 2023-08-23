package main

import "fmt"

func isPrime(num int) bool {
	for n := 2; n <= num/2; n++ {
		if num < 2 || num%n == 0 {
			return false
		}
	}
	return true

}

func twinPrime(num int) (result [][]int) {
	for i := 2; i <= num; i++ {
		if isPrime(i) && isPrime(i+2) {
			result = append(result, []int{i, i + 2})
		}
	}

	return
}

func main() {
	num := 14
	twinPrimes := twinPrime(num)
	fmt.Println(twinPrimes)

}
