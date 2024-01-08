package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strings"
)

var dictionary = map[string]string{
	"a":  "aurek",
	"b":  "besh",
	"c":  "cresh",
	"d":  "dorn",
	"e":  "esk",
	"f":  "forn",
	"g":  "grek",
	"h":  "herf",
	"i":  "isk",
	"j":  "jenth",
	"k":  "krill",
	"l":  "leth",
	"m":  "merm",
	"n":  "nern",
	"o":  "osk",
	"p":  "peth",
	"q":  "qek",
	"r":  "resh",
	"s":  "senth",
	"t":  "trill",
	"u":  "usk",
	"v":  "vev",
	"w":  "wesk",
	"x":  "xesh",
	"y":  "yirt",
	"z":  "zerek",
	"ae": "enth",
	"eo": "onith",
	"kh": "krenth",
	"ng": "nen",
	"oo": "orenth",
	"sh": "sen",
	"th": "thesh",
}

func main() {
	fmt.Println("Enter the word you want to translate to 'Aurebesh'")
	reader := bufio.NewReader(os.Stdin)
	wordToTranslate, err := reader.ReadString('\n')
	checkError(err)
	wordToTranslate = strings.Trim(wordToTranslate, "\n")
	translation := translateToAurebesh(strings.ToLower(wordToTranslate))

	fmt.Printf("%s transated to 'Aurebesh' is '%s'", wordToTranslate, translation)
}

func translateToAurebesh(wordToTranslate string) string {
	translation := ""
	for i := 0; i < len(wordToTranslate); {
		if i+2 < len(wordToTranslate) {
			// Check for the two letters in the dictionary
			substr := wordToTranslate[i : i+2]
			if value, ok := dictionary[string(substr)]; ok {
				translation += value
				i = i + 2
			}
			substr = string(wordToTranslate[i])
			translation += dictionary[substr]
			i++
			continue
		}
		s := wordToTranslate[i]
		translation += dictionary[string(s)]
		i++
	}
	return translation
}

func checkError(err error) {
	if err != nil {
		log.Fatal(err)
	}
}
