package main

import (
	"fmt"
)

// definir metodos de trabajo
type SortingHat interface {
	StartQuesting()
	ShowResults()
}

// estructura para definir preguntas
type HatQuestion struct {
	Question string
	Answers  [][]string
}

func (h HatQuestion) GetQuestion() string {
	return h.Question
}

func (h HatQuestion) GetAnswers() [][]string {
	return h.Answers
}

var Hatquestions []HatQuestion = []HatQuestion{
	{
		Question: "¿Cómo te definirías?",
		Answers: [][]string{
			{"1. Valiente", "gryffindor"},
			{"2. Leal", "hufflepuff"},
			{"3. Sabio", "ravenclaw"},
			{"4. Ambicioso", "slytherin"},
		},
	},
	{
		Question: "¿Cuál es tu clase favorita?",
		Answers: [][]string{
			{"1. Vuelo", "gryffindor"},
			{"2. Pociones", "ravenclaw"},
			{"3. Defensa contra las artes oscuras", "slytherin"},
			{"4. Animales fantásticos", "hufflepuff"},
		},
	},
	{
		Question: "¿Dónde pasarías más tiempo?",
		Answers: [][]string{
			{"1. Invernadero", "hufflepuff"},
			{"2. Biblioteca", "ravenclaw"},
			{"3. En la sala común", "slytherin"},
			{"4. Explorando", "gryffindor"},
		},
	},
	{
		Question: "¿Cuál es tu color favorito?",
		Answers: [][]string{
			{"1. Rojo", "gryffindor"},
			{"2. Azul", "ravenclaw"},
			{"3. Verde", "slytherin"},
			{"4. Amarillo", "hufflepuff"},
		},
	},
	{
		Question: "¿Cuál es tu mascota?",
		Answers: [][]string{
			{"1. Sapo", "ravenclaw"},
			{"2. Lechuza", "gryffindor"},
			{"3. Gato", "hufflepuff"},
			{"4. Serpiente", "slytherin"},
		},
	},
}

type Hat struct {
	Gryffindor int
	Hufflepuff int
	Ravenclaw  int
	Slytherin  int
	Max        int
}

func (h *Hat) StartQuesting() {
	var option int
	fmt.Print("Hola, soy el \"Sombrero Seleccionador\"\nTendrás que responder cinco preguntas para ayudarme a descubrir tu casa de Hogwarts.\n")
	for _, HatQ := range Hatquestions {

		answers := HatQ.GetAnswers()
		fmt.Println(HatQ.GetQuestion())

		for _, ans := range answers {
			fmt.Println(ans[0])
		}
		fmt.Println("Responde  1,2,3 o 4 : ")
		fmt.Scanf("%d", &option)

		switch answers[option-1][1] {
		case "gryffindor":
			h.Gryffindor += 1
		case "hufflepuff":
			h.Hufflepuff += 1
		case "ravenclaw":
			h.Ravenclaw += 1
		case "slytherin":
			h.Slytherin += 1
		}

		if h.Gryffindor > h.Max {
			h.Max = h.Gryffindor
		}
		if h.Hufflepuff > h.Max {
			h.Max = h.Hufflepuff
		}
		if h.Ravenclaw > h.Max {
			h.Max = h.Ravenclaw
		}
		if h.Slytherin > h.Max {
			h.Max = h.Slytherin
		}

	}
}

func (h Hat) ShowResults() {

	fmt.Println("Resultados ")
	fmt.Printf("Gryffindor: %v \n ", h.Gryffindor)
	fmt.Printf("Hufflepuff: %v \n ", h.Hufflepuff)
	fmt.Printf("Ravenclaw: %v  \n", h.Ravenclaw)
	fmt.Printf("Slytherin: %v  \n", h.Slytherin)

	switch {
	case h.Max == h.Gryffindor:
		fmt.Println("Tu casa es Gryffindor")
	case h.Max == h.Hufflepuff:
		fmt.Println("Tu casa es Hufflepuff")
	case h.Max == h.Ravenclaw:
		fmt.Println("Tu casa es Ravenclaw")
	case h.Max == h.Slytherin:
		fmt.Println("Tu casa es Slytherin")
	}

}

func main() {
	var hatShorting SortingHat = &Hat{}
	hatShorting.StartQuesting()
	hatShorting.ShowResults()
}
