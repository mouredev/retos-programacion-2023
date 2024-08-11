package main

import (
	"fmt"
)

func findCombinations(nums []int, target int) [][]int {
	var results [][]int
	var combination []int
	backtrack(nums, target, 0, combination, &results)
	return results
}

func backtrack(nums []int, target int, start int, combination []int, results *[][]int) {
	if target == 0 {
		temp := make([]int, len(combination))
		copy(temp, combination)
		*results = append(*results, temp)
		return
	}

	for i := start; i < len(nums); i++ {
		if nums[i] > target {
			continue
		}

		combination = append(combination, nums[i])
		backtrack(nums, target-nums[i], i, combination, results)
		combination = combination[:len(combination)-1]
	}
}

func main() {
	nums := []int{1, 5, 3, 2}
	target := 6

	fmt.Printf("list: %v\n", nums)
	fmt.Printf("objective: %d\n", target)

	combinations := findCombinations(nums, target)
	fmt.Println("combinations that add to the objective:")
	for _, combo := range combinations {
		fmt.Println(combo)
	}
}
