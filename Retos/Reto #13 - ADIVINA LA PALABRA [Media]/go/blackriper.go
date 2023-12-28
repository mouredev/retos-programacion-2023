package main

import (
	"fmt"
	"math/rand"
	"strings"
)

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

var intents int = 5

var words = []string{
	"python",
	"golang",
	"typescript",
	"csharp",
	"scala",
	"ruby",
	"kotlin",
	"swift",
	"rust",
	"dart",
	"cobol"}

// sustituir el 60% de la palabra
func ReplaceLetters(wor string) string {
	per := (60 * len(wor)) / 100
	for i := 0; i < per; i++ {
		ra := rand.Intn(len(wor))
		wr := string(wor[ra])
		wor = strings.Replace(wor, wr, "_", 1)
	}

	return wor
}

// reamplazar un _ por una letra y retornar frase
func ReplaceLetter(wor, se, ne string) string {
	for ind, l := range wor {
		if string(l) == se {
			ne = strings.Replace(ne, string(ne[ind]), se, 1)
		}
	}
	return ne
}

// obtener palabra al azar
func GetWord() (string, string) {
	word := words[rand.Intn(11)]
	newword := ReplaceLetters(word)
	return word, newword
}

// restar intententos
func RestIntens() {
	intents -= 1
	fmt.Printf("wrong  word you have %v tries left\n", intents)
	if intents == 0 {
		fmt.Println("You lost!!")
	}
}

// mensajes cuando adivina la palabra
func Winner(word string) {
	fmt.Printf("Answer: %s\n", word)
	fmt.Println("congratulations you guessed the word")
}

func main() {
	var quiz string
	word, newword := GetWord()
	for intents > 0 {
		fmt.Println("Guess the word in go")
		fmt.Println("you can write a word or letter")
		fmt.Printf("guess this word: %s\n", newword)
		fmt.Scanf("%s\n", &quiz)

		if len(quiz) > 1 && quiz == word {
			Winner(word)
			break
		} else if len(quiz) == 1 && strings.Contains(word, quiz) {
			newword = ReplaceLetter(word, quiz, newword)
			if newword == word {
				Winner(word)
				break
			}
		} else {
			RestIntens()
		}

	}
}
