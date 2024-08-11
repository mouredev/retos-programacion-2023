package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

type House string

const (
	Gryffindor House = "Gryffindor"
	Slytherin  House = "Slytherin"
	Hufflepuff House = "Hufflepuff"
	Ravenclaw  House = "Ravenclaw"
)

type Question struct {
	Text    string
	Choices map[string]House
}

type Questionnaire interface {
	AskQuestions() House
}

type SortingHat struct {
	questions []Question
}

func NewSortingHat(questions []Question) *SortingHat {
	return &SortingHat{questions: questions}
}

func (sh *SortingHat) AskQuestions() House {
	houseScores := map[House]int{
		Gryffindor: 0,
		Slytherin:  0,
		Hufflepuff: 0,
		Ravenclaw:  0,
	}

	for _, question := range sh.questions {
		answer := sh.askQuestion(question)
		houseScores[answer]++
	}

	return sh.calculateHouse(houseScores)
}

func (sh *SortingHat) askQuestion(question Question) House {
	reader := bufio.NewReader(os.Stdin)

	for {
		fmt.Println(question.Text)
		fmt.Print("Choose an option: ")
		input, _ := reader.ReadString('\n')
		input = strings.TrimSpace(input)

		if house, exists := question.Choices[input]; exists {
			return house
		}

		fmt.Println("Invalid option. Please try again.")
	}
}

func (sh *SortingHat) calculateHouse(houseScores map[House]int) House {
	maxScore := 0
	var selectedHouse House

	for house, score := range houseScores {
		if score > maxScore {
			maxScore = score
			selectedHouse = house
		}
	}

	return selectedHouse
}

/*
Gryffindor:
	Quality: Bravery
	Animal: Lion
	Favorite Subject: Defense Against the Dark Arts
	Type of Magic: Offensive spells
	Dangerous Situation: Face the danger head-on

Slytherin:
	Quality: Cunning
	Animal: Snake
	Favorite Subject: Potions
	Type of Magic: Stealth magic
	Dangerous Situation: Find a cunning solution

Hufflepuff:
	Quality: Loyalty
	Animal: Badger
	Favorite Subject: Care of Magical Creatures
	Type of Magic: Healing magic
	Dangerous Situation: Protect your friends

Ravenclaw:
	Quality: Intelligence
	Animal: Eagle
	Favorite Subject: Divination
	Type of Magic: Divination magic
	Dangerous Situation: Predict the danger and avoid it
*/

func main() {
	questions := []Question{
		{
			Text: "Question 1: What quality do you value the most?\n1. Bravery\n2. Cunning\n3. Loyalty\n4. Intelligence",
			Choices: map[string]House{
				"1": Gryffindor,
				"2": Slytherin,
				"3": Hufflepuff,
				"4": Ravenclaw,
			},
		},
		{
			Text: "Question 2: Which animal would you like to have as a pet?\n1. Lion\n2. Snake\n3. Badger\n4. Eagle",
			Choices: map[string]House{
				"1": Gryffindor,
				"2": Slytherin,
				"3": Hufflepuff,
				"4": Ravenclaw,
			},
		},
		{
			Text: "Question 3: What is your favorite subject?\n1. Defense Against the Dark Arts\n2. Potions\n3. Care of Magical Creatures\n4. Divination",
			Choices: map[string]House{
				"1": Gryffindor,
				"2": Slytherin,
				"3": Hufflepuff,
				"4": Ravenclaw,
			},
		},
		{
			Text: "Question 4: What type of magic do you prefer?\n1. Offensive spells\n2. Stealth magic\n3. Healing magic\n4. Divination magic",
			Choices: map[string]House{
				"1": Gryffindor,
				"2": Slytherin,
				"3": Hufflepuff,
				"4": Ravenclaw,
			},
		},
		{
			Text: "Question 5: In a dangerous situation, what would you do?\n1. Face the danger head-on\n2. Find a cunning solution\n3. Protect your friends\n4. Predict the danger and avoid it",
			Choices: map[string]House{
				"1": Gryffindor,
				"2": Slytherin,
				"3": Hufflepuff,
				"4": Ravenclaw,
			},
		},
	}

	sortingHat := NewSortingHat(questions)
	house := sortingHat.AskQuestions()
	fmt.Printf("The Sorting Hat has placed you in: %s\n", house)
}
