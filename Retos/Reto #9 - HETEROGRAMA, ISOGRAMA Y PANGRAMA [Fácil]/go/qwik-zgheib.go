package main

import (
	"fmt"
	"strings"
)

type Detectors struct {
	isHeterogram func(text string) bool
	isIsogram    func(text string) bool
	isPangram    func(text string) bool
}

func NewDetectors() Detectors {
	return Detectors{
		isHeterogram: func(text string) bool {
			set := make(map[rune]bool)
			for _, letter := range text {
				if _, ok := set[letter]; ok {
					return false
				}
				set[letter] = true
			}
			return true
		},
		isIsogram: func(text string) bool {
			lowerText := strings.ToLower(text)
			for _, letter := range lowerText {
				if letter < 'a' || letter > 'z' {
					continue
				}
				if strings.Count(lowerText, string(letter)) > 1 {
					return false
				}
			}
			return true
		},
		isPangram: func(text string) bool {
			set := make(map[rune]bool)
			for _, letter := range strings.ToLower(text) {
				if letter < 'a' || letter > 'z' {
					continue
				}
				set[letter] = true
			}
			for letter := 'a'; letter <= 'z'; letter++ {
				if _, ok := set[letter]; !ok {
					return false
				}
			}
			return true
		},
	}
}

func main() {
	detectors := NewDetectors()

	texts := []string{
		"Hello world",
		"Jump quickly",
		"Fancy a zigzag",
		"Bright vixen",
		"Jackdaws love my big sphinx of quartz",
		"The five boxing wizards jump quickly",
		"Mr Jock, TV quiz PhD, bags few lynx",
		"Pack my box with five dozen liquor jugs",
		"How razorback-jumping frogs can level six piqued gymnasts",
	}

	for _, text := range texts {
		fmt.Printf("Text: %s\n", text)
		fmt.Printf("Is heterogram: %t\n", detectors.isHeterogram(text))
		fmt.Printf("Is isogram: %t\n", detectors.isIsogram(text))
		fmt.Printf("Is pangram: %t\n\n", detectors.isPangram(text))
	}
}
