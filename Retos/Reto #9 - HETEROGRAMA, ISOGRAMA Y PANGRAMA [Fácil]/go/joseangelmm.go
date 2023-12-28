package main

import (
	"fmt"
	"strings"
	"sync"
)

func main() {
	checkPropiedadesPalabra("Testeando el reto")
	checkPropiedadesPalabra("En un lugar de la mancha de cuyo nombre")
	checkPropiedadesPalabra("asdjhqwejksvmsd")
}

func checkPropiedadesPalabra(texto string) {
	letrasMap := frecuenciaLetras(texto)

	var wg sync.WaitGroup

	var esHeterograma, esIsograma, esPangrama bool

	wg.Add(1)
	go func() {
		defer wg.Done()
		esHeterograma = checkHeterograma(letrasMap)
	}()

	wg.Add(1)
	go func() {
		defer wg.Done()
		esIsograma = checkIsograma(letrasMap)
	}()

	wg.Add(1)
	go func() {
		defer wg.Done()
		esPangrama = checkPangrama(letrasMap)
	}()
	wg.Wait()

	resultado := "La cadena " + texto

	if esHeterograma {
		resultado += " es heterogama"
	}

	if esIsograma {
		resultado += " ,es isograma"
	}

	if esPangrama {
		resultado += " y es pangrama"
	}

	fmt.Println(resultado)

}

func frecuenciaLetras(cadenaTexto string) map[string]int8 {
	frecuenciaLetras := make(map[string]int8)

	cadenaTextoMinuscula := strings.ToLower(cadenaTexto)
	cadenaTextoMinuscula = strings.ReplaceAll(cadenaTextoMinuscula, " ", "")

	for _, letra := range cadenaTextoMinuscula {
		if _, ok := frecuenciaLetras[string(letra)]; ok {
			frecuenciaLetras[string(letra)] = frecuenciaLetras[string(letra)] + 1
		} else {
			frecuenciaLetras[string(letra)] = 1
		}
	}
	delete(frecuenciaLetras, " ")
	return frecuenciaLetras
}

func checkHeterograma(frecuenciaLetras map[string]int8) bool {
	for _, frecuenciaLetra := range frecuenciaLetras {
		if frecuenciaLetra > 1 {
			return false
		}
	}
	return true
}

func checkIsograma(frecuenciaLetras map[string]int8) bool {
	var primeraFrecuencia int8
	for _, frecuenciaLetra := range frecuenciaLetras {
		if primeraFrecuencia == 0 {
			primeraFrecuencia = frecuenciaLetra
			continue
		}
		if primeraFrecuencia != frecuenciaLetra {
			return false
		}
	}
	return true
}

func checkPangrama(frecuenciaLetras map[string]int8) bool {

	abecedario := "abcdefghijklmnñopqrstuvwxyz"
	for _, letra := range abecedario {
		fmt.Println(frecuenciaLetras[string(letra)])
		if _, ok := frecuenciaLetras[string(letra)]; !ok {
			return false
		}
	}
	return true

}
