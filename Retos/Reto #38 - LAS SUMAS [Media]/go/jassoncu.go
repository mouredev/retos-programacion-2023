package main

import (
	"fmt"
	"sort"
)

func findCombinations(nums []int, target int) [][]int {
	// Ordenar la lista para manejar duplicados de manera eficiente
	sort.Ints(nums)

	var result [][]int
	var currentCombination []int

	var backtrack func(start, remain int)
	backtrack = func(start, remain int) {
		if remain == 0 {
			// Se encontró una combinación que suma el objetivo
			result = append(result, append([]int{}, currentCombination...))
			return
		}

		for i := start; i < len(nums); i++ {
			// Evitar duplicados
			if i > start && nums[i] == nums[i-1] {
				continue
			}

			// Continuar explorando la combinación actual
			currentCombination = append(currentCombination, nums[i])
			backtrack(i+1, remain-nums[i])
			currentCombination = currentCombination[:len(currentCombination)-1]
		}
	}

	backtrack(0, target)
	return result
}

func main() {
	// Ejemplo de uso
	nums := []int{1, 5, 3, 2}
	target := 6

	result := findCombinations(nums, target)

	if len(result) > 0 {
		fmt.Printf("Soluciones para el objetivo %d: %v\n", target, result)
	} else {
		fmt.Printf("No hay combinaciones que sumen el objetivo %d\n", target)
	}
}
