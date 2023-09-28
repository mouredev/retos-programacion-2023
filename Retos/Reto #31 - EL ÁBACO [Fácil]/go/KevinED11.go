package main

import (
	"errors"
	"fmt"
	"reflect"
	"strconv"
	"strings"
)

type ICounter interface {
	choiceNumber(number string) int
	Start() (string, error)
}

type AbacoCounter struct {
	Secuence []string
}

func (a *AbacoCounter) choiceNumber(number string) int {
	//secuence := strings.Split(number, "---")[0]
	//counts := strings.Count(secuence, "O")
	sum := 0
	for _, v := range number {
		if string(v) == "-" {
			break
		}
		sum += 1
	}
	return sum

}

func (a *AbacoCounter) Start() (string, error) {
	numbers := []string{}

	for _, v := range a.Secuence {
		numbers = append(numbers, strconv.Itoa(a.choiceNumber(v)))
	}
	conv, err := strconv.Atoi(strings.Join(numbers, ""))

	if err != nil {
		return "", errors.New("Error converting string to int")
	}

	return strconv.FormatInt(int64(conv), 10), nil
}

func NewAbacoCounter(secuence []string) ICounter {
	return &AbacoCounter{Secuence: secuence}

}

func main() {
	secuence := []string{"O---OOOOOOOO",
		"OOO---OOOOOO",
		"---OOOOOOOOO",
		"OO---OOOOOOO",
		"OOOOOOO---OO",
		"OOOOOOOOO---",
		"---OOOOOOOOO"}

	counter := NewAbacoCounter(secuence)
	result, err := counter.Start()

	if err != nil {
		panic(err)
	}
	fmt.Println(reflect.TypeOf(result))
	fmt.Println(result)

}
