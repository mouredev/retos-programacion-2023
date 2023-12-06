package main

func main() {
	for i := 1; i <= 100; i++ {
		switch {
		case i%3 == 0 && i%5 == 0:
			println("fizzbuzz")
		case i%3 == 0:
			println("fizz")
		case i%5 == 0:
			println("buzz")
		default:
			println(i)
		}
	}
}
