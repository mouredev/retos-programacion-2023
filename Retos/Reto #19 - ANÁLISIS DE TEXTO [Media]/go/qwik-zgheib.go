package main

import (
	"fmt"
	"strings"
	"unicode"
)

type TextAnalyzer interface {
	Analyze(text string) TextAnalysisResult
}

type TextAnalysisResult struct {
	TotalWords        int
	AverageWordLength float64
	TotalSentences    int
	LongestWord       string
}

type Analyzer struct{}

func NewAnalyzer() *Analyzer {
	return &Analyzer{}
}

func (a *Analyzer) Analyze(text string) TextAnalysisResult {
	words := 0
	wordLengths := 0
	sentences := 0
	longestWord := ""
	currentWord := strings.Builder{}

	for _, char := range text {
		if unicode.IsLetter(char) {
			currentWord.WriteRune(char)
		} else {
			if currentWord.Len() > 0 {
				word := currentWord.String()
				words++
				wordLengths += len(word)
				if len(word) > len(longestWord) {
					longestWord = word
				}
				currentWord.Reset()
			}
			if char == '.' {
				sentences++
			}
		}
	}
	if currentWord.Len() > 0 {
		word := currentWord.String()
		words++
		wordLengths += len(word)
		if len(word) > len(longestWord) {
			longestWord = word
		}
	}

	averageWordLength := 0.0
	if words > 0 {
		averageWordLength = float64(wordLengths) / float64(words)
	}

	return TextAnalysisResult{
		TotalWords:        words,
		AverageWordLength: averageWordLength,
		TotalSentences:    sentences,
		LongestWord:       longestWord,
	}
}

func main() {
	analyzer := NewAnalyzer()
	text := "This is a sample text. It contains several sentences. Each sentence ends with a period."

	result := analyzer.Analyze(text)
	fmt.Printf("Total Words: %d\n", result.TotalWords)
	fmt.Printf("Average Word Length: %.2f\n", result.AverageWordLength)
	fmt.Printf("Total Sentences: %d\n", result.TotalSentences)
	fmt.Printf("Longest Word: %s\n", result.LongestWord)
}
