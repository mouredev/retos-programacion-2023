package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	reader := bufio.NewReader(os.Stdin)

	fmt.Println("¡Bienvenido al Sombrero Seleccionador de Hogwarts!")
	fmt.Println("Responde a las siguientes preguntas para determinar en qué casa debes estar.")

	var respuestas [5]string

	preguntas := []string{
		"Pregunta 1: ¿Qué cualidad valoras más?\n1. Valentía\n2. Astucia\n3. Lealtad\n4. Inteligencia",
		"Pregunta 2: ¿Qué animal te gustaría tener como mascota?\n1. León\n2. Serpiente\n3. Tejón\n4. Águila",
		"Pregunta 3: ¿Cuál es tu asignatura favorita?\n1. Defensa contra las Artes Oscuras\n2. Pociones\n3. Cuidado de Criaturas Mágicas\n4. Adivinación",
		"Pregunta 4: ¿Qué tipo de magia prefieres?\n1. Hechizos ofensivos\n2. Magia sigilosa\n3. Magia curativa\n4. Magia adivinatoria",
		"Pregunta 5: En una situación de peligro, ¿qué harías?\n1. Enfrentar el peligro de frente\n2. Encontrar una solución astuta\n3. Proteger a tus amigos\n4. Predecir el peligro y evitarlo",
	}

	for i, pregunta := range preguntas {
		fmt.Println(pregunta)
		respuesta, _ := reader.ReadString('\n')
		respuestas[i] = strings.TrimSpace(respuesta)
	}

	casa := determinarCasa(respuestas)
	fmt.Printf("¡Eres un miembro de la casa %s!\n", casa)
}

func determinarCasa(respuestas [5]string) string {
	valorGryffindor := 0
	valorSlytherin := 0
	valorHufflepuff := 0
	valorRavenclaw := 0

	for _, respuesta := range respuestas {
		switch respuesta {
		case "1":
			valorGryffindor++
		case "2":
			valorSlytherin++
		case "3":
			valorHufflepuff++
		case "4":
			valorRavenclaw++
		default:
		}
	}

	maxValor := max(valorGryffindor, valorSlytherin, valorHufflepuff, valorRavenclaw)

	switch maxValor {
	case valorGryffindor:
		return "Gryffindor"
	case valorSlytherin:
		return "Slytherin"
	case valorHufflepuff:
		return "Hufflepuff"
	case valorRavenclaw:
		return "Ravenclaw"
	default:
		return "No se puede determinar la casa"
	}
}

func max(a, b, c, d int) int {
	max := a
	if b > max {
		max = b
	}
	if c > max {
		max = c
	}
	if d > max {
		max = d
	}
	return max
}
