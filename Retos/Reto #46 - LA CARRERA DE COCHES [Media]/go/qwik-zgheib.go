package main

import (
	"fmt"
	"math/rand"
	"time"
)

type RaceTrack struct {
	length int
	trees  []int
}

func NewRaceTrack(length int) *RaceTrack {
	numTrees := rand.Intn(3) + 1
	trees := make([]int, numTrees)
	for i := 0; i < numTrees; i++ {
		trees[i] = rand.Intn(length)
	}
	return &RaceTrack{
		length: length,
		trees:  trees,
	}
}

type Car struct {
	symbol     string
	position   int
	crashed    bool
	crashDelay int
}

func NewCar(symbol string, position int) *Car {
	return &Car{
		symbol:   symbol,
		position: position,
		crashed:  false,
	}
}

func (c *Car) Move(maxAdvance int, trees []int) {
	if c.crashed {
		c.crashDelay--
		if c.crashDelay == 0 {
			c.crashed = false
		}
		return
	}

	advance := rand.Intn(maxAdvance) + 1
	newPosition := c.position - advance

	// Ensure the newPosition is not less than 0
	if newPosition < 0 {
		newPosition = 0
	}

	for _, tree := range trees {
		if newPosition == tree {
			c.crashed = true
			c.crashDelay = 1
			fmt.Printf("%s💥\n", c.symbol)
			return
		}
	}

	c.position = newPosition
}

type Game struct {
	trackLength int
	car1        *Car
	car2        *Car
	track1      *RaceTrack
	track2      *RaceTrack
}

func NewGame(trackLength int) *Game {
	return &Game{
		trackLength: trackLength,
		car1:        NewCar("🚙", trackLength-1),
		car2:        NewCar("🚗", trackLength-1),
		track1:      NewRaceTrack(trackLength),
		track2:      NewRaceTrack(trackLength),
	}
}

func (g *Game) PrintTracks() {
	track1 := make([]rune, g.trackLength)
	track2 := make([]rune, g.trackLength)
	for i := 0; i < g.trackLength; i++ {
		track1[i] = '_'
		track2[i] = '_'
	}
	for _, tree := range g.track1.trees {
		track1[tree] = '🌲'
	}
	for _, tree := range g.track2.trees {
		track2[tree] = '🌲'
	}
	track1[g.car1.position] = []rune(g.car1.symbol)[0]
	track2[g.car2.position] = []rune(g.car2.symbol)[0]
	fmt.Printf("🏁%s\n", string(track1))
	fmt.Printf("🏁%s\n", string(track2))
}

func (g *Game) Run() {
	for {
		g.PrintTracks()
		if g.car1.position <= 0 && g.car2.position <= 0 {
			fmt.Println("draw!")
			break
		} else if g.car1.position <= 0 {
			fmt.Println("winner: 🚙!")
			break
		} else if g.car2.position <= 0 {
			fmt.Println("winner: 🚗!")
			break
		}

		g.car1.Move(3, g.track1.trees)
		g.car2.Move(3, g.track2.trees)

		time.Sleep(1 * time.Second)
	}
}

func main() {
	rand.Int()
	game := NewGame(20)
	game.Run()
}
