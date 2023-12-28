package main

var aurebesh = map[rune]string{
	'a': "æ",
	'b': "“",
	'c': "¢",
	'd': "ð",
	'e': "€",
	'f': "đ",
	'g': "ŋ",
	'h': "ħ",
	'i': "→",
	'j': "ˀ",
	'k': "ĸ",
	'l': "ł",
	'm': "µ",
	'n': "µ",
	'o': "ø",
	'p': "þ",
	'q': "@",
	'r': "¶",
	's': "ß",
	't': "ŧ",
	'u': "↓",
	'v': "„",
	'w': "ſ",
	'x': "»",
	'y': "←",
	'z': "«",
}

func main() {
	testSpanish := "¡hola! ¿cómo estás?"
	testAurebesh := "æ“¢ð€đŋħ→ˀĸłµµøþ@¶ßŧ↓„ſ»←«"

	println(SpanishToAurebesh(testSpanish))
	println(AurebeshToSpanish(testAurebesh))
}

func SpanishToAurebesh(s string) string {
	var result string
	for _, c := range s {
		if val, ok := aurebesh[c]; ok {
			result += val
		} else {
			result += string(c)
		}
	}
	return result
}

func AurebeshToSpanish(s string) string {
	var result string
	for _, c := range s {
		for k, v := range aurebesh {
			if v == string(c) {
				result += string(k)
			}
		}
	}
	return result
}
