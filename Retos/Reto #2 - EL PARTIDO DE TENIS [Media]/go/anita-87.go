package main

import (
	"bufio"
	"errors"
	"fmt"
	"log"
	"os"
	"strings"
)

const msg = "Write the game scoring sequence separated by commas ','. Press enter when the score is finished"

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

var score = map[int]string{
	0: "Love",
	1: "15",
	2: "30",
	3: "40",
}

type Player struct {
	Score int
	Name  string
}

func main() {
	readScore()
}

func readScore() string {
	reader := bufio.NewReader(os.Stdin)
	fmt.Println(msg)
	score, err := reader.ReadString('\n')
	if err != nil {
		log.Fatalf("Failed to read the game score. Reason: %w", err)
	}

	scores, err := validateScore(score)
	if err != nil {
		log.Fatalf(err.Error())
	}

	keepScore(scores)
	return score
}

func validateScore(score string) ([]string, error) {
	elems := strings.Split(score, ",")
	if len(elems) == 0 {
		return nil, errors.New("Invalid score. Score is empty or has an invalid comma delimiter")
	}
	r := make([]string, len(elems))
	for i, elem := range elems {
		elem = strings.TrimSpace(elem)
		if elem != "P1" && elem != "P2" {
			return nil, errors.New("Invalid score. Players are indicated as 'P1' or 'P2'")
		}
		r[i] = elem
	}
	return r, nil
}

func keepScore(score []string) {
	p1 := Player{Score: 0, Name: "P1"}
	p2 := Player{Score: 0, Name: "P2"}

	for _, s := range score {
		switch s {
		case "P1":
			p1.UpScore()
		case "P2":
			p2.UpScore()
		}
		printScore(p1, p2)
	}
}

func (p *Player) UpScore() {
	p.Score = p.Score + 1
}

func printScore(p1, p2 Player) {
	if p1.Score == 3 && p2.Score == 3 || p1.Score > 3 && p2.Score > 3 && p1.Score == p2.Score {
		fmt.Println("Deuce")
		return
	}
	if p1.Score > 3 || p2.Score > 3 {
		if p1.Score > p2.Score {
			if p1.Score == p2.Score+1 {
				fmt.Println(fmt.Sprintf("Ventaja %s", p1.Name))
				return
			} else {
				fmt.Println(fmt.Sprintf("Ha ganado el %s", p1.Name))
				return
			}
		} else {
			if p2.Score == p1.Score+1 {
				fmt.Println(fmt.Sprintf("Ventaja %s", p2.Name))
				return
			} else {
				fmt.Println(fmt.Sprintf("Ha ganado el %s", p2.Name))
				return
			}
		}
	}
	fmt.Println(fmt.Sprintf("%s - %s", score[p1.Score], score[p2.Score]))
}
