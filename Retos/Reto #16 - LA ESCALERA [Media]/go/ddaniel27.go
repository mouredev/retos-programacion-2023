package main

import "strings"

func main() {
	println(stairs(4))
	println(stairs(0))
	println(stairs(-4))
}

func stairs(n int) string {
	var str string
	switch {
	case n == 0:
		return "__"
	case n > 0:
		str = strings.Repeat(" ", (2*n)) + "_\n"
	case n < 0:
		str = "_\n"
	}
	str += stairsRecursive(n)
	return str
}

func stairsRecursive(n int) string {
	switch {
	case n > 0:
		return strings.Repeat(" ", (2*(n-1))) + "_|\n" + stairsRecursive(n-1)
	case n < 0:
		return stairsRecursive(n+1) + strings.Repeat(" ", -(2*n+1)) + "|_\n"
	default:
		return ""
	}
}
