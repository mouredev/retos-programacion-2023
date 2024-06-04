package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

var leetMap = map[rune]string{
	'A': "4", 'a': "4",
	'B': "8", 'b': "8",
	'C': "(", 'c': "(",
	'D': "|)", 'd': "|)",
	'E': "3", 'e': "3",
	'F': "|=", 'f': "|=",
	'G': "6", 'g': "6",
	'H': "#", 'h': "#",
	'I': "!", 'i': "!",
	'J': "]", 'j': "]",
	'K': "|<", 'k': "|<",
	'L': "1", 'l': "1",
	'M': "[]\\/[]", 'm': "[]\\/[]",
	'N': "[]\\[]", 'n': "[]\\[]",
	'O': "0", 'o': "0",
	'P': "|D", 'p': "|D",
	'Q': "(,)", 'q': "(,)",
	'R': "|2", 'r': "|2",
	'S': "5", 's': "5",
	'T': "7", 't': "7",
	'U': "(_)", 'u': "(_)",
	'V': "\\/", 'v': "\\/",
	'W': "\\/\\/", 'w': "\\/\\/",
	'X': "}{", 'x': "}{",
	'Y': "`/", 'y': "`/",
	'Z': "2", 'z': "2",
	'1': "L",
	'2': "R",
	'3': "E",
	'4': "A",
	'5': "S",
	'6': "b",
	'7': "T",
	'8': "B",
	'9': "g",
	'0': "O",
}

func toLeet(text string) string {
	var leetText strings.Builder

	for _, char := range text {
		if leetChar, found := leetMap[char]; found {
			leetText.WriteString(leetChar)
		} else {
			leetText.WriteRune(char)
		}
	}

	return leetText.String()
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	fmt.Print("Enter text to convert to leet: ")
	text, _ := reader.ReadString('\n')
	text = strings.TrimSpace(text)
	fmt.Println(toLeet(text))
}
