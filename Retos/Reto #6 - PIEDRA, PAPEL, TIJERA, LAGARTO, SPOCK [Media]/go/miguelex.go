package main

import "fmt"

const (
	PIEDRA  = "🗿"
	PAPEL   = "📄"
	TIJERAS = "✂️"
	LAGARTO = "🦎"
	SPOCK   = "🖖"
)

func PiedraPapelTijerasLagartoSpock(juegos [][2]string) string {
	var p1Points, p2Points int

	ganador := map[string][2]string{
		PIEDRA:  [2]string{TIJERAS, LAGARTO},
		PAPEL:   [2]string{PIEDRA, SPOCK},
		TIJERAS: [2]string{PAPEL, LAGARTO},
		LAGARTO: [2]string{PAPEL, SPOCK},
		SPOCK:   [2]string{TIJERAS, PIEDRA},
	}

	for _, juego := range juegos {
		jugador1, jugador2 := juego[0], juego[1]
		if jugador1 == jugador2 {
			p1Points++
			p2Points++
		} else if ganador[jugador1][0] == jugador2 || ganador[jugador1][1] == jugador2 {
			p1Points++
		} else {
			p2Points++
		}
	}

	if p1Points == p2Points {
		return fmt.Sprintf("Empate a %d puntos", p1Points)
	} else if p1Points > p2Points {
		return fmt.Sprintf("Gana el jugador 1 por %d a %d puntos", p1Points, p2Points)
	} else {
		return fmt.Sprintf("Gana el jugador 2 por %d a %d puntos", p2Points, p1Points)
	}
}

func main() {
	fmt.Println(PiedraPapelTijerasLagartoSpock([][2]string{
		{PIEDRA, TIJERAS},
		{PIEDRA, PAPEL},
		{LAGARTO, SPOCK},
	}))

	fmt.Println(PiedraPapelTijerasLagartoSpock([][2]string{
		{TIJERAS, TIJERAS},
		{PIEDRA, PAPEL},
		{LAGARTO, SPOCK},
		{PIEDRA, PAPEL},
		{SPOCK, PAPEL},
		{LAGARTO, LAGARTO},
		{SPOCK, LAGARTO},
	}))
}
