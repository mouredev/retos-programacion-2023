package main

import (
	"fmt"
	"sort"
)

func sumCombinations(candidates []int, target int) [][]int {
	//slice final de resultados
	var result [][]int
	//slice para ir guardando combinaciones validas
	var combination []int
	//ordenar los elementos del slice candidates
	sort.Ints(candidates)

	//funcion recursiva para encontrar combinaciones validas
	//start represent el indice inicial para comenzar la busqueda
	//remain is el valor actual que se esta comparando con el target para verificar la suma
	var backtrack func(start, remain int)
	backtrack = func(start, remain int) {

		//si remain es 0 hemos encontrado una combinacion valida, agregarla al slice de resultados
		if remain == 0 {
			result = append(result, append([]int{}, combination...))
			return
		}
		//loop principal
		for i := start; i < len(candidates); i++ {

			//si target es un valor negativo o se ha alcanzado el final del slice candidates, no hay solucion
			//se interrumpe el ciclo
			if target < 0 || start == len(candidates) {
				break
			}

			//verifico
			if i > start && candidates[i] == candidates[i-1] {
				continue
			}
			//añadir el valor del candidato actual al slice de posibles combinaciones validas
			combination = append(combination, candidates[i])
			//llamada a la funcion recursiva
			backtrack(i+1, remain-candidates[i])
			//remover del slice de combinaciones el ultimo valor añadido
			//NOTA: aqui usamos la sintaxis de go para manipular los indices de un slice, no existe funcion pop()
			combination = combination[:len(combination)-1]
		}
	}

	//llamada a la funcion recursiva con parametros iniciales
	backtrack(0, target)
	return result
}

func main() {
	candidates := []int{1, 2, 1, 1, 1, 1, 3, 1}
	target := 4
	combination := sumCombinations(candidates, target)
	fmt.Println(combination)
}
