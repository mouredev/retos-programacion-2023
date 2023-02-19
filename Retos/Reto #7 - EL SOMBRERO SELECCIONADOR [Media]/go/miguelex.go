package main

import (
	"fmt"
	"math/rand"
	"time"
)

func HogwartsHatSelector() string {
	fmt.Println("Bienvenido al Test de Clasificación de Casas de Hogwarts!")
	fmt.Println("Responde las siguientes preguntas para saber a qué casa pertenecerías:")

	preguntas := []string{
		"1. ¿Qué cualidad valoras más en ti mismo?",
		"2. ¿Qué criatura mágica te gustaría tener como mascota?",
		"3. ¿Cuál es tu asignatura favorita en Hogwarts?",
		"4. ¿Cuál es tu lugar favorito en el castillo de Hogwarts?",
		"5. ¿Cuál es tu hechizo favorito?",
		"6. ¿Qué objeto mágico te gustaría poseer?",
		"7. ¿Cuál es tu personaje favorito de Harry Potter?",
		"8. ¿Qué harías si te enfrentas a un troll?",
		"9. ¿Qué tipo de clima prefieres?",
		"10. ¿Cuál es tu forma preferida de transporte mágico?",
		"11. ¿Qué color te atrae más?",
		"12. ¿Qué criatura mágica te da más miedo?",
		"13. ¿Cuál es tu golosina mágica favorita?",
		"14. ¿Cuál es tu asignatura menos favorita en Hogwarts?",
		"15. ¿Qué actividad te gustaría hacer en tu tiempo libre en Hogwarts?",
	}

	opciones := [][]string{
		{"a. Coraje", "b. Inteligencia", "c. Lealtad", "d. Astucia"},
		{"a. Búho", "b. Gato", "c. Rata", "d. Lechuza"},
		{"a. Pociones", "b. Transformaciones", "c. Herbología", "d. Defensa contra las Artes Oscuras"},
		{"a. La Sala Común de mi casa", "b. El Gran Comedor", "c. La Biblioteca", "d. Los terrenos del castillo"},
		{"a. Expecto Patronum", "b. Wingardium Leviosa", "c. Expelliarmus", "d. Lumos"},
		{"a. La Capa de Invisibilidad", "b. La Varita de Saúco",
			"c. El Giratiempo", "d. La Piedra Filosofal"},
		{"a. Harry Potter", "b. Hermione Granger",
			"c. Ron Weasley", "d. Neville Longbottom"},
		{"a. Huir", "b. Atacar", "c. Pedir ayuda",
			"d. Intentar razonar con él"},
		{"a. Sol", "b. Lluvia", "c. Nieve", "d. Viento"},
		{"a. Escoba voladora", "b. El Autobús Noctámbulo",
			"c. El Tren Hogwarts Express", "d. Aparición"},
		{"a. Rojo", "b. Azul", "c. Amarillo", "d. Verde"},
		{"a. Dementor", "b. El Basilisco",
			"c. El Hombre Lobo", "d. Las Arpías"},
		{"a. Grageas de Todos los Sabores", "b. Chocolate de la Caja de Bertie Bott",
			"c. Pastel de Calabaza", "d. Caramelos de Menta"},
		{"a. Historia de la Magia", "b. Adivinación",
			"c. Estudio de los Muggles", "d. Runas Antiguas"},
		{"a. Jugar al Quidditch", "b. Explorar el castillo", "c. Leer en la Biblioteca", "d. Pasar tiempo con amigos"},
	}

	rand.Seed(time.Now().UnixNano())
	random_questions := rand.Perm(len(preguntas))[:4]

	respuestas := make([]string, 4)
	for i, idx := range random_questions {
		fmt.Println(preguntas[idx])
		for _, opcion := range opciones[idx] {
			fmt.Println(opcion)
		}
		fmt.Print("Elige una opción (a, b, c o d): ")
		fmt.Scanln(&respuestas[i])
	}

	puntuaciones := map[string]int{
		"Gryffindor": 0,
		"Ravenclaw":  0,
		"Hufflepuff": 0,
		"Slytherin":  0,
	}

	for _, respuesta := range respuestas {
		switch respuesta {
		case "a":
			puntuaciones["Gryffindor"]++
		case "b":
			puntuaciones["Ravenclaw"]++
		case "c":
			puntuaciones["Hufflepuff"]++
		case "d":
			puntuaciones["Slytherin"]++
		}
	}

	var casa string
	maxPuntuacion := 0
	for k, v := range puntuaciones {
		if v > maxPuntuacion {
			casa = k
			maxPuntuacion = v
		}
	}

	return casa
}

func main() {
	fmt.Printf("¡Felicidades! Según tus respuestas, perteneces a la casa de %s.\n", HogwartsHatSelector())
}
