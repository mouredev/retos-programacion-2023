/*
 * Crea un pequeño juego que consista en adivinar palabras en un número máximo de intentos:
 * - El juego comienza proponiendo una palabra aleatoria incompleta
 *   - Por ejemplo "m_ur_d_v", y el número de intentos que le quedan
 * - El usuario puede introducir únicamente una letra o una palabra (de la misma longitud que
 *   la palabra a adivinar)
 *   - Si escribe una letra y acierta, se muestra esa letra en la palabra. Si falla, se resta
 *     uno al número de intentos
 *   - Si escribe una resolución y acierta, finaliza el juego, en caso contrario, se resta uno
 *     al número de intentos
 *   - Si el contador de intentos llega a 0, el jugador pierde
 * - La palabra debe ocultar de forma aleatoria letras, y nunca puede comenzar ocultando más del 60%
 * - Puedes utilizar las palabras que quieras y el número de intentos que consideres
 */

package main

import (
	"fmt"
	"math/rand"
	"strings"
	"time"
)

func selectWord() (string, string) {
	rand.Seed(time.Now().UnixNano())
	//Ten random words to play with
	words := [10]string{"caracola", "caballo", "silla", "telefono", "chubasquero", "violin", "zapatilla", "pelota", "canasta", "almohada"}

	selectedWord := words[rand.Intn(9)]
	letters := strings.Split(selectedWord, "")
	hidden := make([]string, len(letters))

	maxHidden := int(float64(len(letters)) * 0.6)

	//recorremos la palabra letra a letra y decidimos aleatoriamente si ocultamos dicha letra
	hiddenCount := 0
	for i := 0; i < len(letters); i++ {
		if rand.Float64() < 0.5 && hiddenCount < maxHidden {
			hidden[i] = "_"
			hiddenCount++
		} else {
			hidden[i] = letters[i]
		}
	}

	return strings.Join(hidden, ""), selectedWord
}

func main() {
	chances := 5
	fmt.Println("Guess the word!!")
	hiddenWord, clearWord := selectWord()
	// fmt.Println("Puedes introducir una letra o la palabra completa.")
	// fmt.Println("Si la letra está, aparecerá en la palabra buscada, si por")
	// fmt.Println("el contrario no está, perderás un oportunidad. Si las")
	// fmt.Println("oportunidades llegan a 0 (tienes 5 oportunidades), pierdes.")
	// fmt.Println("Si sabes la palabra, puedes introducirla completamente.")
	fmt.Println("Esta es la palabra que tienes que adivinar: ", hiddenWord)
	fmt.Println("Y esta la respuesta: ", clearWord)
	for {
		var input string
		fmt.Print("Enter a letter (or a word if you're brave): ")
		fmt.Scanln(&input)
		if len(input) > 1 {
			if input == clearWord {
				fmt.Println("Wow! You guessed the word! Congrats")
				break
			} else {
				fmt.Println("This is not the word you are looking for...")
				chances--
				if chances == 0 {
					fmt.Println("You haven't more chances... You lose")
					break
				}
				fmt.Println("You have", chances, "chances more. Be careful!")
				continue
			}
		}
		//recorremos la palabra letra a letra y si la letra introducida está, vemos su posicion
		// si esa posición en la palabra oculta es un "_", lo sustituimos por la letra.
		for i := 0; i < len(clearWord); i++ {
			if input == string(clearWord[i]) && string(hiddenWord[i]) == "_" {
				hiddenWord = strings.Replace(hiddenWord, "_", input, 1)
				if hiddenWord == clearWord {
					fmt.Println("Yeah! You guessed the word! Well done!")
					fmt.Println(hiddenWord)
					break
				}
				fmt.Println(hiddenWord)
				continue
			}
			// else {
			// 	fmt.Println("This letter is not hidden...")
			// 	chances--
			// 	if chances == 0 {
			// 		fmt.Println("You haven't more chances... You lose")
			// 		break
			// 	}
			// 	fmt.Println("You have", chances, "chances more. Be careful!")
			// 	continue
			// }
		}

	}
}
