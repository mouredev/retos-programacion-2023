package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
)

type House string

const (
	Gryffindor House = "Gryffindor"
	Hufflepuff       = "Hufflepuff"
	Ravenclaw        = "Ravenclaw"
	Slytherin        = "Slytherin"
)

type Option struct {
	literal     rune
	description string
	houses      []House
}

type Question struct {
	value   string
	options []Option
}

func getHouseFromScores(scores map[House]int) string {
	var bigger = Gryffindor

	for key, value := range scores {
		if value > scores[bigger] {
			bigger = key
		}
	}

	return string(bigger)
}

func main() {
	quiz := makeQuestionare()
	scores := map[House]int{Gryffindor: 0, Hufflepuff: 0, Ravenclaw: 0, Slytherin: 0}
	reader := bufio.NewReader(os.Stdin)

	for index, question := range quiz {
		// Print question
		fmt.Printf("%d. %s\n", index+1, question.value)

		// Print options for that question
		for _, option := range question.options {
			fmt.Printf("%c: %s\n", option.literal, option.description)
		}

		// Read response
		line, err := reader.ReadString('\n')
		response := rune(line[0])
		if err != nil {
			log.Fatal(err)
		}

		// save the result in the scores
		for _, option := range question.options {
			if option.literal == response {
				for _, house := range option.houses {
					scores[house] += 1
				}
			}
		}
	}

	house := getHouseFromScores(scores)
	fmt.Printf("%s!!!\n", house)
}

func makeQuestionare() []Question {
	return []Question{
		{
			value: "Dawn or dusk?",
			options: []Option{
				{'a', "Dawn", []House{Gryffindor, Ravenclaw}},
				{'b', "Dusk", []House{Hufflepuff, Slytherin}},
			},
		},
		{
			value: "Forest or river?",
			options: []Option{
				{'a', "Forest", []House{Gryffindor, Ravenclaw}},
				{'b', "River", []House{Hufflepuff, Slytherin}},
			},
		},
		{
			value: "Which of the following would you most hate people to call you?",
			options: []Option{
				{'a', "Ordinary", []House{Slytherin}},
				{'b', "Ignorant", []House{Ravenclaw}},
				{'c', "Cowardly", []House{Gryffindor}},
				{'d', "Selfish", []House{Hufflepuff}},
			},
		},
		{
			value: "After you have died, what would you most like people to do when they hear your name?",
			options: []Option{
				{'a', "Miss you, but smile", []House{Hufflepuff}},
				{'b', "Ask for more stories about your adventures", []House{Gryffindor}},
				{'c', "Think with admiration of your achievements", []House{Ravenclaw}},
				{'d', "I don't care what people think of me after I'm dead, it's what they think of me while I'm alive that counts", []House{Slytherin}},
			},
		},
		{
			value: "You enter an enchanted garden. What would you be most curious to examine first?",
			options: []Option{
				{'a', "The silver leafed tree bearing golden apples", []House{Ravenclaw}},
				{'b', "The fat red toadstools that appear to be talking to each other", []House{Hufflepuff}},
				{'c', "The bubbling pool, in the depths of which something luminous is swirling", []House{Slytherin}},
				{'d', "The statue of an old wizard with a strangely twinkling eye", []House{Gryffindor}},
			},
		},
	}
}
