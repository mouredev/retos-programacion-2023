package main

import (
	"errors"
	"fmt"
	"time"
)

type ICounter interface {
	Start()
}

type CounterDown struct {
	InitialCount  int
	PauseDuration int
}

func (c *CounterDown) Start() {
	for c.InitialCount >= 0 {
		fmt.Println(c.InitialCount)

		if c.InitialCount == 0 {
			break
		}

		time.Sleep(time.Duration(c.PauseDuration) * time.Second)

		c.InitialCount -= 1
	}

}

func NewCounterDown(initialCount, pauseDuration int) (*CounterDown, error) {
	if initialCount <= 0 || pauseDuration <= 0 {
		return nil, errors.New("Enter a valid positive number")
	}

	return &CounterDown{InitialCount: initialCount, PauseDuration: pauseDuration}, nil
}

func main() {
	fmt.Println("Hello world")

	counterDown, err := NewCounterDown(10, 1)

	if err != nil {
		panic(err)
	}

	counterDown.Start()

}
