package main

import "strings"

func main() {
	println(triangle(10))
}

func triangle(n int) string {
	s := 0
	tri := strings.Trim(triangleRecursive(n, s), "\n")
	var result string
	for _, v := range strings.Split(tri, "\n") {
		result += strings.Repeat(" ", n) + v + "\n"
	}
	for _, v := range strings.Split(tri, "\n") {
		result += v + " " + v + "\n"
	}
	return strings.Trim(result, "\n")
}

func triangleRecursive(n, s int) string {
	if n == 0 {
		return ""
	}
	return strings.Repeat(" ", n-1) + strings.Repeat("*", 2*s+1) + strings.Repeat(" ", n-1) + "\n" + triangleRecursive(n-1, s+1)
}
