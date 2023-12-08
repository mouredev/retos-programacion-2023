package main

import "strings"

func main() {
	println(spiral(5))
}

func spiral(side int) string {
	symbols := []string{"═", "║", "╗", "╔", "╝", "╚"}
	result := strings.Repeat(symbols[0], side-1) + symbols[2] + "\n"
	for i := 1; i < side; i++ {
		if i <= side/2 {
			result += strings.Repeat(
				symbols[1],
				i-1,
			) +
				symbols[3] +
				strings.Repeat(
					symbols[0],
					side-(i*2+1),
				) +
				symbols[2] +
				strings.Repeat(
					symbols[1],
					i,
				) +
				"\n"
		} else {
			result += strings.Repeat(
				symbols[1],
				side-i-1,
			) +
				symbols[5] +
				strings.Repeat(
					symbols[0],
					i*2-side,
				) +
				symbols[4] +
				strings.Repeat(
					symbols[1],
					side-i-1,
				) +
				"\n"
		}
	}
	return result
}
