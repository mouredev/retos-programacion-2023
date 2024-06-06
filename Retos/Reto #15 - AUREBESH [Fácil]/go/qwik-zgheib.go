package main

import (
	"fmt"
	"strings"
	"unicode"
)

var basicAlphabet = map[string]string{
	"a": "aurek", "b": "besh", "c": "cresh", "d": "dorn", "e": "esk", "f": "forn", "g": "grek", "h": "herf",
	"i": "isk", "j": "jenth", "k": "krill", "l": "leth", "m": "merm", "n": "nern", "o": "osk", "p": "peth", "q": "qek",
	"r": "resh", "s": "senth", "t": "trill", "u": "usk", "v": "vev", "w": "wesk", "x": "xesh", "y": "yirt", "z": "zerek",
	"ae": "enth", "eo": "onith", "kh": "krenth", "ng": "nen", "oo": "orenth", "sh": "sen", "th": "thesh",
}

var aurebeshAlphabet = func() map[string]string {
	aurebeshAlphabet := make(map[string]string)
	for key, value := range basicAlphabet {
		aurebeshAlphabet[value] = key
	}
	return aurebeshAlphabet
}()

func basicAurebeshTranslator(text string, aurebesh bool) string {
	text = strings.ToLower(text)
	translatedText := ""

	unidecodeText := unidecode(text)

	if aurebesh {
		translatedText = text
		for key, value := range aurebeshAlphabet {
			translatedText = strings.ReplaceAll(translatedText, key, value)
		}
	} else {
		characterIndex := 0
		textLen := len(unidecodeText)
		for characterIndex < textLen {
			simpleCharacter := string(unidecodeText[characterIndex])
			doubleCharacter := ""
			if characterIndex < textLen-1 {
				doubleCharacter = simpleCharacter + string(unidecodeText[characterIndex+1])
			}

			if val, ok := basicAlphabet[doubleCharacter]; ok {
				translatedText += val
				characterIndex += 2
			} else if val, ok := basicAlphabet[simpleCharacter]; ok {
				translatedText += val
				characterIndex++
			} else {
				translatedText += simpleCharacter
				characterIndex++
			}
		}
	}

	return translatedText
}

func unidecode(text string) string {
	var result strings.Builder
	for _, r := range text {
		if r == 'ñ' {
			result.WriteString("n")
		} else if r == 'á' {
			result.WriteString("a")
		} else if r == 'é' {
			result.WriteString("e")
		} else if r == 'í' {
			result.WriteString("i")
		} else if r == 'ó' {
			result.WriteString("o")
		} else if r == 'ú' {
			result.WriteString("u")
		} else if unicode.IsLetter(r) || unicode.IsDigit(r) {
			result.WriteRune(r)
		} else {
			result.WriteString("[?]")
		}
	}
	return result.String()
}

func main() {
	fmt.Print("Enter text to translate from Spanish to Aurebesh: ")
	var input string
	fmt.Scanln(&input)

	translatedToAurebesh := basicAurebeshTranslator(input, false)
	fmt.Printf("Translated to Aurebesh: %s\n", translatedToAurebesh)

	fmt.Print("Enter text to translate from Aurebesh to Spanish: ")
	fmt.Scanln(&input)
	translatedToSpanish := basicAurebeshTranslator(input, true)
	fmt.Printf("Translated to Spanish: %s\n", translatedToSpanish)
}
