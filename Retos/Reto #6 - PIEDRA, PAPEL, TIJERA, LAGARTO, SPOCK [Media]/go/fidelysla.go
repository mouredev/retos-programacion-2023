package main

import (
	"fmt"
	"math/rand"
	"strings"
	"time"
)

//  * Crea un programa que calcule quien gana más partidas al piedra,
//  * papel, tijera, lagarto, spock.
//  * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
//  * - La función recibe un listado que contiene pares, representando cada jugada.
//  * - El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
//  *   "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
//  * - Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
//  * - Debes buscar información sobre cómo se juega con estas 5 posibilidades.

// * UTILIZO rand.Intn PARA GENERARA ALEATORIAMENTE ENTRADAS DE EMOJIS!!

func gene() (string, string) {
	db := []string{"\U0001F596", "\U0001f98e", "\u2702\uFE0F", "\U0001F4C4", "\U0001F5FF"}
	fp := db[rand.Intn(len(db))]
	sp := db[rand.Intn(len(db))]
	return fp, sp
}

func imp(n int) (int, int) {
	contadorfp := 0
	contadorsp := 0
	var f string = "Player 1"
	var s string = "Player 2"
	for i := 0; i < n; i++ {
		fmt.Println(strings.Repeat("*", 15))
		a, b := gene()
		fmt.Printf("%s: %s\n", f, a)
		fmt.Printf("%s: %s\n", s, b)
		if a == "\U0001F5FF" && b == "\u2702\uFE0F" {
			contadorfp += 1
		}
		if b == "\U0001F5FF" && a == "\u2702\uFE0F" {
			contadorsp += 1
		}
		if a == "\u2702\uFE0F" && b == "\U0001F4C4" {
			contadorfp += 1
		}
		if b == "\u2702\uFE0F" && a == "\U0001F4C4" {
			contadorsp += 1
		}
		if a == "\U0001F4C4" && b == "\U0001F5FF" {
			contadorfp += 1
		}
		if b == "\U0001F4C4" && a == "\U0001F5FF" {
			contadorsp += 1
		}
		if a == "\U0001F5FF" && b == "\U0001f98e" {
			contadorfp += 1
		}
		if b == "\U0001F5FF" && a == "\U0001f98e" {
			contadorsp += 1
		}
		if a == "\U0001f98e" && b == "\U0001F596" {
			contadorfp += 1
		}
		if b == "\U0001f98e" && a == "\U0001F596" {
			contadorsp += 1
		}
		if a == "\U0001F596" && b == "\u2702\uFE0F" {
			contadorfp += 1
		}
		if b == "\U0001F596" && a == "\u2702\uFE0F" {
			contadorsp += 1
		}
		if a == "\u2702\uFE0F" && b == "\U0001f98e" {
			contadorfp += 1
		}
		if b == "\u2702\uFE0F" && a == "\U0001f98e" {
			contadorsp += 1
		}
		if a == "\U0001f98e" && b == "\U0001F4C4" {
			contadorfp += 1
		}
		if b == "\U0001f98e" && a == "\U0001F4C4" {
			contadorsp += 1
		}
		if a == "\U0001F4C4" && b == "\U0001F596" {
			contadorfp += 1
		}
		if b == "\U0001F4C4" && a == "\U0001F596" {
			contadorsp += 1
		}
		if a == "\U0001F596" && b == "\U0001F5FF" {
			contadorfp += 1
		}
		if b == "\U0001F596" && a == "\U0001F5FF" {
			contadorsp += 1
		}

	}
	return contadorfp, contadorsp
}

func comb() {
	salir := 0
	for salir == 0 {
		rand.Seed(time.Now().Unix())
		contadorfp, contadorsp := imp(5)
		if contadorfp > contadorsp {
			fmt.Println(strings.Repeat("*", 15))
			fmt.Println("GANADOR PLAYER 1")
			fmt.Println(strings.Repeat("*", 15))
			break
		}
		if contadorfp < contadorsp {
			fmt.Println(strings.Repeat("*", 15))
			fmt.Println("GANADOR PLAYER 2")
			fmt.Println(strings.Repeat("*", 15))
			break
		}
		for contadorfp == contadorsp {
			fmt.Println(strings.Repeat("*", 15))
			fmt.Println("---EMPATE!!---")
			contadorfp, contadorsp = imp(1)
			if contadorfp > contadorsp {
				fmt.Println(strings.Repeat("*", 15))
				fmt.Println("GANADOR PLAYER 1")
				fmt.Println(strings.Repeat("*", 15))
				break
			}
			if contadorfp < contadorsp {
				fmt.Println(strings.Repeat("*", 15))
				fmt.Println("GANADOR PLAYER 2")
				fmt.Println(strings.Repeat("*", 15))
				break
			}
		}
		salir = 1
	}
}

func main() {
	fmt.Println("JUEGO: PIEDRA, PAPEL, TIJERA, LAGARTO Y SPOCK")
	comb()
}
