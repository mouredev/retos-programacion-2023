package main

// nota : al rotar la pieza vuelve a su posicion inicial
import (
	"fmt"
	"strings"
)

// definir metodos de trabajo
type Tetris interface {
	PlayTetris()
}

/*implementar metodo*/
type Piece struct {
	Position [][]int
}

// funcion para  realizar acciones
func (p *Piece) PlayTetris() {
	var opcion string
	var numRotate int
	DrawTetris(p.Position)
	for opcion != "E" {
		fmt.Println("Select an action for the piece [D]Down [L] Left [R] Right [RT] rotate [E] Exit")
		fmt.Scanf("%s", &opcion)
		opcion = strings.ToUpper(opcion)
		if opcion == "RT" {
			numRotate++
			if numRotate > 4 {
				numRotate = 0
			}
		}
		MoveTetris(opcion, &p.Position, numRotate)
		DrawTetris(p.Position)
	}
}

/*metodos auxiliares*/
// funcion para realizar movimientos
func MoveTetris(option string, cord *[][]int, count int) {
	pos := *cord

	switch {
	case option == "RT":
		RotatePiece(count, &pos)
	case option == "D":
		pos[1][0]++
		pos[1][1]++
		pos[1][2]++
		pos[1][3]++
		if pos[1][0] == 10 || pos[1][1] == 10 || pos[1][2] == 10 || pos[1][3] == 10 {
			pos[1][0]--
			pos[1][1]--
			pos[1][2]--
			pos[1][3]--
		}

	case option == "R":
		MinusOrMax(&pos, false)
		if pos[0][0] == 10 || pos[0][1] == 10 || pos[0][2] == 10 || pos[0][3] == 10 {
			MinusOrMax(&pos, true)
		}
	case option == "L":
		MinusOrMax(&pos, true)
		if pos[0][0] < 0 || pos[0][1] < 0 || pos[0][2] < 0 || pos[0][3] < 0 {
			MinusOrMax(&pos, false)
		}

	}
	*cord = pos
}

// determinar limites
func MinusOrMax(cord *[][]int, minus bool) {
	pos := *cord
	if minus == true {
		pos[0][0]--
		pos[0][1]--
		pos[0][2]--
		pos[0][3]--
	} else if minus == false {
		pos[0][0]++
		pos[0][1]++
		pos[0][2]++
		pos[0][3]++

	}
}

// funcion para rotar la pieza
func RotatePiece(count int, cord *[][]int) {
	if count == 1 {
		*cord = [][]int{{0, 0, 0, 1}, {0, 1, 2, 0}}
	} else if count == 2 {
		*cord = [][]int{{0, 1, 2, 2}, {0, 0, 0, 1}}
	} else if count == 3 {
		*cord = [][]int{{1, 2, 2, 2}, {2, 2, 1, 0}}
	} else {
		*cord = [][]int{{0, 0, 1, 2}, {0, 1, 1, 1}}
	}
}

// dibujar tetris
func DrawTetris(cord [][]int) {
	var file int
	var cube string
	for file < 10 {
		for c := 0; c < 10; c++ {
			switch {
			case cord[0][0] == c && cord[1][0] == file:
				cube = cube + "🔳"
			case cord[0][1] == c && cord[1][1] == file:
				cube = cube + "🔳"
			case cord[0][2] == c && cord[1][2] == file:
				cube = cube + "🔳"
			case cord[0][3] == c && cord[1][3] == file:
				cube = cube + "🔳"
			default:
				cube = cube + "🔲"

			}
		}
		fmt.Println(cube)
		file++
		cube = ""
	}
}

func main() {
	p1 := [][]int{{0, 0, 1, 2}, {0, 1, 1, 1}}
	var tetris Tetris = &Piece{Position: p1}
	tetris.PlayTetris()
}
