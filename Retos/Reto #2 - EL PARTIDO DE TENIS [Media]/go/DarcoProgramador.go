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

// Estructura de Jugadores
type jugador struct {
	Name      string
	Puntacion int
}

func game(PlayersMap map[string]*jugador, jugada map[int]string, secuencia *[]string) {

	for i, name := range *secuencia {

		PlayersMap[name].Puntacion += 1

		if i == len(*secuencia)-1 {
			switch {
			case PlayersMap["P1"].Puntacion == PlayersMap["P2"].Puntacion:
				fmt.Println("Los jugadores empataron")
			case PlayersMap["P1"].Puntacion > PlayersMap["P2"].Puntacion:
				fmt.Println("Ha ganado el", PlayersMap["P1"].Name)
			case PlayersMap["P1"].Puntacion < PlayersMap["P2"].Puntacion:
				fmt.Println("Ha ganado el", PlayersMap["P2"].Name)
			}
			break
		}

		if i > 4 {
			switch {
			case PlayersMap["P1"].Puntacion == PlayersMap["P2"].Puntacion:
				fmt.Println(jugada[4])
			case PlayersMap["P1"].Puntacion > PlayersMap["P2"].Puntacion:
				fmt.Println(jugada[5], PlayersMap["P2"].Name)
			case PlayersMap["P1"].Puntacion < PlayersMap["P2"].Puntacion:
				fmt.Println(jugada[5], PlayersMap["P2"].Name)
			}
		} else {
			fmt.Println(jugada[PlayersMap["P1"].Puntacion], "-", jugada[PlayersMap["P2"].Puntacion])
		}
	}
}

func main() {
	//Tipos de jugada
	jugada := map[int]string{0: "Love", 1: "15", 2: "30", 3: "40", 4: "Deuce", 5: "ventaja"}

	//Jugadores
	Players := []jugador{
		{"P1", 0},
		{"P2", 0},
	}

	//Mapa para la busqueda
	PlayersMap := map[string]*jugador{"P1": &Players[0], "P2": &Players[1]}

	//Secuencia a procesar
	secuencia := []string{"P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"}

	//Procesando la secuencia
	game(PlayersMap, jugada, &secuencia)
}
