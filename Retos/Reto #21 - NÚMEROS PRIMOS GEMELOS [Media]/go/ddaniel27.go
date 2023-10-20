package main

func main() {
	max := 14
	twinPrimes := map[int]int{}

	for i := 2; i <= max-2; i++ {
		if IsPrime(i) && IsPrime(i+2) {
			twinPrimes[i] = i + 2
		}
	}

	for key, value := range twinPrimes {
		println(key, value)
	}
}

func IsPrime(num int) bool {
	if num == 1 {
		return false
	}

	for i := 2; i <= num/2; i++ {
		if num%i == 0 {
			return false
		}
	}

	return true
}
