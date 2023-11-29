package main

import (
	"fmt"
	"math/rand"
	"strings"
	"time"
)

// elementos para pintar la pista  durante el juego
const (
	GOAL    = " 🏁 "
	TREE    = "🌲"
	PLAYER1 = " 🚙 "
	PLAYER2 = " 🚗 "
	SHOCK   = " 💥 "
)

/*definir metodos para el juego*/
type CarRace interface {
	ConfigParams()
	StartRace() bool
}

type Race struct {
	NumTracks int
	PosTree1  []int
	PosTree2  []int
}

// configurar el largo de la pista y generar los obstaculos
func (r *Race) ConfigParams() {
	fmt.Println("How long should the race track be?")
	fmt.Scanf("%d", &r.NumTracks)
	r.PosTree1 = FactoryTree(r.NumTracks)
	r.PosTree2 = FactoryTree(r.NumTracks)
}

// empezar la carrera
func (r *Race) StartRace() bool {
	var (
		posP1    int = r.NumTracks - 1
		posP2    int = r.NumTracks - 1
		numRace  int = 1
		numShock int
		endGame  bool
	)

	fmt.Println("Inicial Race")
	fmt.Println(PaintingCar(r.NumTracks, posP1, PLAYER1, r.PosTree1, false))
	fmt.Println(PaintingCar(r.NumTracks, posP2, PLAYER2, r.PosTree2, false))

	for {
		shock1 := MoveCar(&posP1, &numShock, r.PosTree1)
		shock2 := MoveCar(&posP2, &numShock, r.PosTree2)

		time.Sleep(5 * time.Second)

		fmt.Printf("Race number %v \n", numRace)
		fmt.Println(PaintingCar(r.NumTracks, posP1, PLAYER1, r.PosTree1, shock1))
		fmt.Println(PaintingCar(r.NumTracks, posP2, PLAYER2, r.PosTree2, shock2))
		numRace++

		if posP1 == 0 {
			fmt.Printf("The winner is %v \n", PLAYER1)
			endGame = true
			break
		}

		if posP2 == 0 {
			fmt.Printf("The winner is %v \n", PLAYER2)
			endGame = true
			break
		}

		if posP1 == 0 && posP2 == 0 {
			fmt.Println("Not winner race end  tie!!")
			endGame = true
			break
		}

	}
	return endGame
}

/* funciones auxilares*/

// pintar jugadores en la pista
func PaintingCar(numTracks, positionCar int, emojiCar string, positionTree []int, shock bool) string {
	var car string

	for t := 0; t < numTracks; t++ {

		switch {
		case t == 0:
			car += GOAL
		case t == positionCar:
			if shock {
				car += SHOCK
			} else {
				car += emojiCar
			}
		default:
			if tree := IsTree(t, positionTree); tree == true {
				car += TREE
			} else {
				car += "_"
			}

		}

	}
	return car
}

// saber si hay que pintar un arbol en la posicion actual
func IsTree(numTrack int, positionTree []int) (tree bool) {
	for _, pos := range positionTree {
		if pos == numTrack {
			tree = true
		}
	}
	return tree
}

// generar el numero de arboles y la posicion del mismo
func FactoryTree(numTracks int) []int {
	var posTree []int
	numTrees := rand.Intn(4-1) + 1
	max := numTracks - 1

	for t := 0; t < numTrees; t++ {
		posTree = append(posTree, rand.Intn(max-1)+1)
	}
	return posTree
}

// mover el auto del jugador y comprobar si ha chocado con algun obstaculo
func MoveCar(positionCar, numShock *int, positionTree []int) (colision bool) {

	if shock := IsTree(*positionCar, positionTree); shock == true && *numShock == 0 {
		colision = true
		*numShock++
	} else {
		if *positionCar < 0 {
			*positionCar = 0
		} else {
			*positionCar -= rand.Intn(4-1) + 1
		}
	}
	return colision
}

// controlar el modo de juego
func RaceGame() {
	var option string = "y"
	var f1 CarRace = &Race{}
	for option != "n" {
		f1.ConfigParams()
		endGame := f1.StartRace()
		if endGame {
			fmt.Println("You can play a new race Y/N")
			fmt.Scanf("%s", &option)
			option = strings.ToLower(option)
		}
	}
}

func main() {
	RaceGame()
}
