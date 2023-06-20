package main

import (
	"fmt"
	"strings"
)

// mapa de caracteres
var aurebesh = map[string]string{"a": "æ", "b": "“", "c": "¢", "d": "ð", "e": "€", "f": "đ", "g": "ŋ", "h": "ħ", "i": "→", "j": "ˀ", "k": "ĸ", "l": "ł", "m": "µ", "n": "µ", "o": "ø", "p": "þ", "q": "@", "r": "¶", "s": "ß", "t": "ŧ", "u": "↓", "v": "„", "w": "ſ", "x": "»", "y": "←", "z": "«"}
var spanish = reverseMap(aurebesh)

// estructura de datos
type Traslate struct {
	Text   string
	Option string
}

// obtener el lenguaje y texto a traducir
func (t *Traslate) GetText() {
	fmt.Println("What language do you want to translate into? [A]Spanish to Aurebesh [S] Aurebesh to Spanish")
	fmt.Scanf("%s\n", &t.Option)
	fmt.Println("Introduce text to Traslate")
	fmt.Scanf("%s\n", &t.Text)
}

// buscar palabras para traducir a aurebesh
func (t *Traslate) Spanish_to_Aurebesh() {
	newword := t.Text
	for _, w := range t.Text {
		newword = strings.Replace(newword, string(w), aurebesh[string(w)], 1)
	}
	t.Text = newword
}

// buscar palabras para traducir a español
func (t *Traslate) Aurebesh_to_Spanish() {
	newword := t.Text
	for _, w := range t.Text {
		newword = strings.Replace(newword, string(w), spanish[string(w)], 1)
	}
	t.Text = newword
}

func main() {
	fmt.Println(spanish)
	traslate := Traslate{}
	traslate.GetText()
	switch traslate.Option {
	case "A":
		traslate.Spanish_to_Aurebesh()
		fmt.Printf("Result: %v", traslate.Text)
	case "S":
		traslate.Aurebesh_to_Spanish()
		fmt.Printf("Result: %v", traslate.Text)
	}

}

// invertir orden del mapa
func reverseMap(m map[string]string) map[string]string {
	n := make(map[string]string, len(m))
	for k, v := range m {
		n[v] = k
	}
	return n
}
