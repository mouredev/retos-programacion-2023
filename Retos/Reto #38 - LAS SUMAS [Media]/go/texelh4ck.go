/*
================================================

	Author: texelh4ck

================================================
*/
package main

import (
	"fmt"
	"sort"
)

func combinator(list []int, target int) [][]int {
	var result [][]int

	var find func(start int, r int, temp []int)
	find = func(start int, r int, temp []int) {
		// Agrega el resultado correcto a result
		if r == 0 {
			result = append(result, temp)
			return
		}

		if start == len(list) || r < 0 {
			return
		}

		for i := start; i < len(list); i++ {
			if i > 0 && list[i] == list[i-1] {
				continue
			}
			temp = append(temp, list[i])
			find(i+1, r-list[i], temp)
			temp = temp[:len(temp)-1] // Quita el último elemento agregado
		}
	}

	// Ordena la lista
	sort.Ints(list)
	// Ejecuta el algoritmo backtrack
	find(0, target, []int{})
	return result
}

func main() {

	fmt.Println(combinator([]int{1, 3, 4, 2}, 7))
}
