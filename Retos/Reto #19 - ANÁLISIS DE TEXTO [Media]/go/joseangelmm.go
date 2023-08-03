package main

import "fmt"

func main() {
	checkText("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam vitae orci ut risus consequat hendrerit sit amet quis risus. Fusce ullamcorper volutpat elit, vitae sagittis odio consectetur a. Proin sollicitudin feugiat ipsum quis vestibulum. Morbi enim ex, interdum id ultrices et, mattis vitae velit. Curabitur mi tortor, commodo in quam nec, consectetur pharetra quam. Donec venenatis sapien in ligula accumsan imperdiet. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Donec eu sapien odio. Praesent id leo in sapien sodales vulputate. Mauris aliquet purus elit, vitae vestibulum metus sodales eu. Morbi ut mauris erat. Mauris sem risus, posuere et varius et, tempor eu ex. Praesent tempor metus quam, suscipit viverra ante hendrerit et. Maecenas viverra convallis turpis et luctus. Pellentesque non elementum magna, non blandit velit.")
}

func checkText(text string) {
	numWords := 0
	averageLetterByWord := 0
	numSentences := 0
	largestWord := ""

	numCurrentWord := 0
	currentWord := ""
	totalLetters := 0

	readingWord := false

	for _, letterCode := range text {
		letter := string(letterCode)

		if !readingWord && !(letter == " " || letter == ";" || letter == ",") {
			numWords += 1
			readingWord = true
		}

		if letter == " " || letter == ";" || letter == "," || letter == "." {
			if len(currentWord) > len(largestWord) {
				largestWord = currentWord
			}
			totalLetters += numCurrentWord
			numCurrentWord = 0
			currentWord = ""
			readingWord = false
			if letter == "." {
				numSentences += 1
			}
		} else {
			numCurrentWord += 1
			currentWord += letter
		}
	}

	averageLetterByWord = totalLetters / numWords

	fmt.Println("Number of words:", numWords)
	fmt.Println("Average number of letter by word: ", averageLetterByWord)
	fmt.Println("Number of sentences", numSentences)
	fmt.Println("Largest word: ", largestWord)
}
