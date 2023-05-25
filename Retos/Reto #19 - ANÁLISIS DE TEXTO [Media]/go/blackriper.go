package main

import (
	"fmt"
	"strings"
)

// la palabra mas larga del texto
func WordMoreLong(word string, long *string, max *int) {
	// al señalar * indicamos que nuestro parametro es un puntero y para acceder al valor del puntero y poder asignar el valor usamos * fuera de los parametros
	if len(word) > *max {
		*max = len(word)
		*long = word
	}
}

// numero de oraciones del texto
func NumberPrayers(word string, prayers *int) {
	if strings.Contains(word, ".") {
		*prayers += 1
	}
}

// calcular suma total para la media
func CalcMediaLongWords(word string, media *int) {
	*media = *media + len(word)
}

func main() {
	const text string = `Dragon Ball es un manga escrito e ilustrado por Akira Toriyama.
                      Fue publicado originalmente en la revista Shōnen Jump, de la editorial japonesa Shūeisha, entre 1984 y 1995.
                      Su trama describe las aventuras de Gokū, un guerrero saiyajin, experto en artes marciales que en su infancia
                      inicia sus viajes y aventuras en las que pone a prueba y mejora sus habilidades de pelea, enfrentando oponentes
                      y protegiendo a la Tierra de otros seres que quieren conquistarla y exterminar a la humanidad.`

	// obtener array de palabras
	words := strings.Fields(text)

	//variables para obtener lo requerido
	var wordlong string
	var max int
	var numberPrayers int
	var media int

	// recorremos las palabras y obtenemos lo requerido usamos puntero para no perder el valor en la funcion
	for _, word := range words {
		WordMoreLong(word, &wordlong, &max)
		NumberPrayers(word, &numberPrayers)
		CalcMediaLongWords(word, &media)
	}

	fmt.Printf("La palabra mas larga es: %v \n", wordlong)
	fmt.Printf("El numero de Oraciones es: %v \n", numberPrayers)
	fmt.Printf("Son un total de %v palabras en el texto\n", len(words))
	fmt.Printf("La longitud media de las palabras es de %v\n", media/len(words))

}
