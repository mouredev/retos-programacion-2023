package main

import "regexp"

func main() {
	str := "Lorem ipsum dolor sit amet, consectetur adipiscing elit. In mattis elementum ultrices. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Proin ullamcorper feugiat diam ultricies dapibus. Donec ut nisl eros. Aliquam cursus interdum enim, eget porttitor neque hendrerit aliquet."
	wordsRe := regexp.MustCompile(`\w+`)
	sentencesRe := regexp.MustCompile(`[.!?]`)

	words := wordsRe.FindAllString(str, -1)
	sentences := sentencesRe.FindAllString(str, -1)

	var maxWord string
	maxLengthWord := 0
	medianLengthWord := 0
	for _, word := range words {
		medianLengthWord += len(word)
		if len(word) > maxLengthWord {
			maxLengthWord = len(word)
			maxWord = word
		}
	}
	medianLengthWord /= len(words)

	println("Total words count:", len(words))
	println("Median words length:", medianLengthWord)
	println("Sentences count:", len(sentences))
	println("Max words count and word:", maxLengthWord, maxWord)
}
