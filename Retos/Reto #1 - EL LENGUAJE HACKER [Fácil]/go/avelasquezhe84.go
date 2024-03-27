package main

import (
	"fmt"
	"os"
	"strings"
)

func main() {
	// slice of command line arguments, joined by a space to produce a lowercase string
	source := strings.ToLower(strings.Join(os.Args[1:], " "))

	// initialization of a slice with all the alphabet letters
	alphabet := []rune{}
	for ch := 'a'; ch <= 'z'; ch++ {
		alphabet = append(alphabet, ch)
	}

	// slice with all the first substitutions from leet language
	substitution := []string{"4", "I3", "[", ")", "3", "|=", "&", "#", "1", ",_|", ">|", "1", "/\\/\\", "^/", "0", "|*", "(_,)", "I2", "5", "7", "(_)", "\\/", "\\/\\", "><", "j", "2"}

	// initialization of a slice with interleaving join of alphabet letters and their substitutions
	translation := []string{}
	for i, ch := range alphabet {
		translation = append(translation, []string{string(ch), substitution[i]}...)
	}

	// custom replacer
	re := strings.NewReplacer(translation...)
	res := re.Replace(source)

	fmt.Println(res)
}
