package main

import (
	"fmt"
)

/*
 * Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
 * El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
 * gane cada punto del juego.
 *
 * - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
 * - Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
 *   15 - Love
 *   30 - Love
 *   30 - 15
 *   30 - 30
 *   40 - 30
 *   Deuce
 *   Ventaja P1
 *   Ha ganado el P1
 * - Si quieres, puedes controlar errores en la entrada de datos.
 * - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.
 */

func calculateScore(score int) string {
	switch score {
	case 0:
		return "Love"
	case 1:
		return "15"
	case 2:
		return "30"
	case 3:
		return "40"
	default:
		return "Ventaja"
	}
}

func displayScore(player1Score, player2Score int) string {
	if player1Score >= 3 && player2Score >= 3 {
		if player1Score == player2Score {
			return "Deuce"
		} else if player1Score > player2Score {
			if player1Score >= player2Score+2 {
				return "Ha ganado el P1"
			}
			return "Ventaja P1"
		} else {
			if player2Score >= player1Score+2 {
				return "Ha ganado el P2"
			}
			return "Ventaja P2"
		}
	} else {
		return calculateScore(player1Score) + " - " + calculateScore(player2Score)
	}
}

func playTennis(sequence []string) string {
	player1Score, player2Score := 0, 0

	for _, point := range sequence {
		if point == "P1" {
			player1Score++
		} else if point == "P2" {
			player2Score++
		} else {
			return "Error: Entrada inválida"
		}

		currentScore := displayScore(player1Score, player2Score)
		fmt.Println(currentScore)

		if currentScore == "Ha ganado el P1" || currentScore == "Ha ganado el P2" {
			return currentScore
		}
	}

	return ""
}

func main() {
	sequence := []string{"P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"}
	result := playTennis(sequence)
	fmt.Println(result)
}
