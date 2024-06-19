package main

import (
	"fmt"
)

func permute(s string) []string {
	var results []string
	var helper func([]rune, int)
	helper = func(arr []rune, n int) {
		if n == 1 {
			results = append(results, string(arr))
		} else {
			for i := 0; i < n; i++ {
				helper(arr, n-1)
				if n%2 == 1 {
					arr[0], arr[n-1] = arr[n-1], arr[0]
				} else {
					arr[i], arr[n-1] = arr[n-1], arr[i]
				}
			}
		}
	}

	helper([]rune(s), len(s))
	return results
}

func main() {
	word := "winter"
	permutations := permute(word)
	fmt.Printf("word permutations '%s':\n", word)
	for _, p := range permutations {
		fmt.Println(p)
	}
}
