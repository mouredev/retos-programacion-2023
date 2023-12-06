package main

import (
	"fmt"
	"strings"
)

func removeDiacritics(cadena string) string {
	diacriticos := map[string]string{
		"á": "a", "é": "e", "í": "i", "ó": "o", "ú": "u",
		"à": "a", "è": "e", "ì": "i", "ò": "o", "ù": "u",
		"ä": "a", "ë": "e", "ï": "i", "ö": "o", "ü": "u",
		"â": "a", "ê": "e", "î": "i", "ô": "o", "û": "u",
		"ã": "a", "ñ": "n", "õ": "o",
		"ç": "c",
	}

	var cadenaSinDiacriticos strings.Builder
	for _, caracter := range cadena {
		if remplazo, ok := diacriticos[string(caracter)]; ok {
			cadenaSinDiacriticos.WriteString(remplazo)
		} else {
			cadenaSinDiacriticos.WriteRune(caracter)
		}
	}

	return cadenaSinDiacriticos.String()
}

func isHeterogram(cadena string) bool {
	return len(cadena) == len(removeDiacritics(cadena))
}

func isIsogram(cadena string) bool {
	letrasVistas := make(map[rune]bool)
	for _, letra := range removeDiacritics(cadena) {
		if letrasVistas[letra] {
			return false
		}
		letrasVistas[letra] = true
	}
	return true
}

func isPangram(cadena string) bool {
	alfabeto := make(map[rune]bool)
	for _, letra := range "abcdefghijklmnopqrstuvwxyz" {
		alfabeto[letra] = true
	}

	cadena = strings.ToLower(removeDiacritics(cadena))
	for _, letra := range cadena {
		if alfabeto[letra] {
			delete(alfabeto, letra)
		}
		if len(alfabeto) == 0 {
			return true
		}
	}

	return false
}

func main() {
	string1 := "murcielago"
	string2 := "esdrújula"
	string3 := "El veloz murciélago hindú comía feliz cardillo y kiwi. La cigüeña tocaba el saxofón detrás del palenque de paja"

	fmt.Println(isHeterogram(string1)) // true
	fmt.Println(isHeterogram(string2)) // false
	fmt.Println(isIsogram(string1))    // true
	fmt.Println(isIsogram(string2))    // false
	fmt.Println(isPangram(string3))    // true
}
