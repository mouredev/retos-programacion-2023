package main

import (
	"fmt"
	"strconv"
)

// definir metodos de trabajo
type Find interface {
	ReadData()
	FindObjective()
}

// implementar metodos
type DataSum struct {
	Numbers   []int
	Objective int
}

func (d *DataSum) ReadData() {
	var opcion string
	for {
		fmt.Println("Introduce a positive number [E]End array Numbers ")
		fmt.Scanf("%s", &opcion)

		if opcion == "E" {
			fmt.Println("Introduce a Objective number to find combinate in the array numbers")
			fmt.Scanf("%d", &d.Objective)
			break
		} else {
			num, err := strconv.Atoi(opcion)
			if err != nil {
				panic(err)
			}
			d.Numbers = append(d.Numbers, num)
		}
	}
}
func (d DataSum) FindObjective() {
	var (
		combinations [][]int
		n            int
	)
	// mapa para evitar comb repetidas
	seen := make(map[int]bool)

	for n < len(d.Numbers) {
		for j := 0; j < len(d.Numbers)-1; j++ {
			if (d.Numbers[n] + d.Numbers[j]) == d.Objective {
				if !seen[d.Numbers[j]] {
					seen[d.Numbers[n]] = true
					combination := []int{d.Numbers[n], d.Numbers[j]}
					combinations = append(combinations, combination)
				}
			}

			if (d.Numbers[n] + d.Numbers[j]) < d.Objective {
				acu := d.Numbers[n] + d.Numbers[j]
				if (acu + d.Numbers[j+1]) == d.Objective {
					if !seen[d.Numbers[j]] {
						seen[d.Numbers[j]] = true
						combination := []int{d.Numbers[n], d.Numbers[j], d.Numbers[j+1]}
						combinations = append(combinations, combination)
					}
				}
			}
		}
		n++
	}
	fmt.Printf("Solucions: %v this combinations sum is equals %v", combinations, d.Objective)
}

func main() {
	var sums Find = &DataSum{}
	sums.ReadData()
	sums.FindObjective()
}
