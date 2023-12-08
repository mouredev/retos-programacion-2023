package main

import (
	"fmt"
	"math/rand"
	"strings"
)

// posicion de caramelos y fantasmas
var gostPosition [][]int = [][]int{{2, 2}, {3, 3}}
var candyPosition []int = []int{4, 1}

// implementar patron de diseño factory para generar enigmas
type FactoryEnigma struct{}

func (f *FactoryEnigma) NewEnigma() []string {
	enigmas := map[int][]string{
		0: {"¿Lenguaje de programación interpretado cuya filosofía es la legibilidad de su código?", "python"},
		1: {"¿Lenguaje de programación está diseñado para ser totalmente interoperable con Java?", "kotlin"},
		2: {"¿Lenguaje de programación concurrente cuyo tipado estàtico es inspirado en c?", "go"},
		3: {"¿Lenguaje de programación comercializado por primera vez en 1995 por Sun Microsystems?", "java"},
		4: {"¿Manga escrito e ilustrado por Akira Toriyama?", "dragonball"},
		5: {"¿Manga escrito e ilustrado por Masashi Kishimoto?", "naruto"},
		6: {"¿Es una empresa tecnológica multinacional estadounidense con sede en Cupertino?", "apple"},
		7: {"¿Es empresa de tecnología multinacional estadounidense que se centra en inteligencia artificial?", "google"},
		8: {"¿Es una empresa tecnológica multinacional estadounidense que produce software de computadora?", "microsoft"},
	}
	randomindx := rand.Intn(len(enigmas))
	return enigmas[randomindx]

}

// metodo para dibujar la casa y los movimientos del usuario
func DrawHouse(plPosition []int, candy *bool, gosh *bool) string {
	var house string

	for c := 0; c <= 4; c++ {
		for f := 0; f < 4; f++ {
			if f == 0 && c == 0 {
				house += "🚪"
				c = 1
			} else if plPosition[0] == c && plPosition[1] == f {
				house += "👾"
			} else {
				house += "⬜️"
			}

			// toparse con algun item
			switch {
			case plPosition[0] == candyPosition[0] && plPosition[1] == candyPosition[1]:
				*candy = true
			case plPosition[0] == gostPosition[0][0] && plPosition[1] == gostPosition[0][1]:
				*gosh = true
			case plPosition[0] == gostPosition[1][0] && plPosition[1] == gostPosition[1][1]:
				*gosh = true
			}

			if f == 3 {
				house += "\n"
			}
		}
	}
	return house
}

// evaluar movimientos del jugador
func WalkPlayer(position []int) string {
	var text string
	switch {
	case position[0] == 1 && position[1] < 3:
		text = "you can move [s]south [e]east"
		if position[1] == 2 {
			text = "you can move [s]south [e] east [w] west"
		}
	case position[0] == 1 && position[1] == 3:
		text = "you can move [s]south [w] west"

	case position[0] == 2 && position[1] < 3:
		if position[1] == 0 {
			text = "you can move [s]south [e]east"
		} else {
			text = "you can move [n]north [s] south [e]east [w] west"
		}
	case position[0] == 2 && position[1] == 3 || position[0] == 3 && position[1] == 3:
		text = "you can move [n]north [s] south [w] west"

	case position[0] == 3 && position[1] < 3:
		if position[1] == 0 {
			text = "you can move [n]north [s] south [e]east"
		} else {
			text = "you can move [n]north [s] south [e]east [w] west"
		}
	case position[0] == 4 && position[1] < 3:
		if position[1] == 0 {
			text = "you can move [n]north [e]east"
		} else {
			text = "you can move [n]north  [e]east [w] west"
		}
	case position[0] == 4 && position[1] == 3:
		text = "you can move [n]north   [w] west"
	}
	return text
}

// realizar preguntas al usuario
func AskQuestion() bool {
	var (
		correct bool
		answer  string
	)
	factory := &FactoryEnigma{}
	question := factory.NewEnigma()

	for correct != true {
		fmt.Println(question[0])
		fmt.Scanf("%s", &answer)
		answer = strings.ToLower(answer)
		if answer == question[1] {
			correct = true
		}
	}
	return correct

}

// implementar juego
type Hallowen interface {
	Playing()
}

type Pl struct {
	Position []int
}

func (p *Pl) Playing() {
	var (
		gosh  bool
		candy bool
		cord  string
		win   bool
	)

	for {
		fmt.Println(DrawHouse(p.Position, &candy, &gosh))

		correct := AskQuestion()
		if gosh {
			fmt.Println("you find a gosh you can ask other question !!")
			correct1 := AskQuestion()
			if correct1 {
				win = true
				gosh = false
			}
		}
		if correct || win {
			text := WalkPlayer(p.Position)
			fmt.Println(text)
			fmt.Scanf("%s", &cord)
			cord = strings.ToLower(cord)
			switch cord {
			case "s":
				p.Position[0] += 1
			case "n":
				p.Position[0] -= 1
			case "e":
				p.Position[1] += 1
			case "w":
				p.Position[1] -= 1
			default:
				fmt.Println("Inconrrect option !!")
			}
		}
		if candy {
			fmt.Println("you found the candies congratulations 🍭 !!")
			break
		}

	}
}

func main() {
	var hauntedHouse Hallowen = &Pl{Position: []int{1, 0}}
	hauntedHouse.Playing()
}
